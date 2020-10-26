from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from collections import OrderedDict
import os
import math
import time
import numpy as np
import tensorflow as tf
import collections
import sys
import codecs
import re
import copy
import json


# from model import *


class GPT2Model(object):
    # Below is the language model.

    def __init__(self, is_training, past=None):
        self.batch_size = 1
        self.is_training = is_training
        self.start_str = "<start>"
        self.eos_str = "<eos>"
        self.unk_str = "<unk>"
        self.num_str = "<num>"
        self.pun_str = "<pun>"
        self.id2token_in_words, self.id2token_in_letters, self.id2token_out = {}, {}, {}
        self.token2id_in_words, self.token2id_in_letters, self.token2id_out = {}, {}, {}

    def predict(self, sess, features, temperature):
        return sess.run(self.logits, feed_dict={self.input_data: features})

    def letters2ids(self, letters):
        # letters_split = re.split("\\s+", letters)
        return [self.token2id_in_letters.get(letter, 0)
                for letter in letters if len(letter) > 0]

    def word2id(self, word, return_word=False, return_processed=False):
        tmp_dict = {}
        _word_processed = word
        word_out = copy.deepcopy(word)
        END_WITH_SYMBOL_REGEX_DEFAULT = re.compile("([a-zA-Z']+)([^a-zA-Z']+$)")
        SYMBOL_SERIAL_REGEX = re.compile("^[^a-z0-9A-Z']+$")
        # if re.search(SYMBOL_SERIAL_REGEX, word):
        #     tmp_dict["id"] = self.token2id_out.get(self.unk_str)
        #     tmp_dict["out"] = self.unk_str
        #     tmp_dict["processed"] = word[0]
        #     return tmp_dict
        if word in self.token2id_out:
            word_out = word
        elif word.lower() in self.token2id_out:
            word_out = word.lower()
        else:
            word = re.sub(END_WITH_SYMBOL_REGEX_DEFAULT, lambda x: x.group(1), word)

            _word_processed = copy.deepcopy(word)
            if word in self.token2id_out:
                word_out = word
            elif word.lower() in self.token2id_out:
                word_out = word.lower()
            else:
                word_out, word_processed = self.unk_str, word_out
        rid = self.token2id_out.get(word_out, -1)

        if rid == -1:
            tmp_dict["id"] = self.token2id_out[self.unk_str]
        else:
            tmp_dict["id"] = rid
        if return_word:
            tmp_dict["out"] = word_out

        tmp_dict["processed"] = _word_processed
        return tmp_dict

    def words2ids(self, words):
        print("words:", words)
        # return [self.eos_id] + [self.word2id(word) for word in words if len(word) > 0]
        return [self.word2id(word)["id"] for word in words if len(word) > 0]

    def sentence2list(self, sentence):
        words_array = re.split(' ', sentence.strip())
        print(len(words_array), words_array)
        # word_letters = words_array[-1]
        new_words_array = words_array[:-1]  # 去除最后一个词
        labels_array = words_array[1:]  # 去掉第一个词
        print("new_words_array:", new_words_array)
        print("labels_array:", labels_array)
        # letters = ' '.join(word_letters)
        # words_ids = self.words2ids(words_array)
        # letters_ids = self.letters2ids(letters)
        print("finish line")
        return new_words_array, labels_array

    def test_letter(self, sess, lm_path, letter_path, data, vocab_path):
        vocab_word = vocab_path + '/vocab_out'
        vocab_in_letters = vocab_path + '/vocab_in_letters'

        with open(vocab_word, mode="r", encoding="utf-8") as f:
            for line in f:
                token, id = line.split("##")
                id = int(id)
                self.id2token_out[id] = token
                self.token2id_out[token] = id
        with open(vocab_in_letters, mode="r", encoding="utf-8") as f:
            for line in f:
                token, id = line.split("##")
                id = int(id)
                self.id2token_in_letters[id] = token
                self.token2id_in_letters[token] = id
        # print(self.token2id_in_letters)

        interpreter_letter = tf.lite.Interpreter(model_path=letter_path)

        input_details_letter = interpreter_letter.get_input_details()
        output_details_letter = interpreter_letter.get_output_details()

        interpreter_letter.allocate_tensors()

        """Runs the model on the given data."""
        logfile = open('test_letter.log', 'a+')
        start_time = time.time()

        prediction_made = 0.0
        top1_correct_total, top3_correct_total, top5_correct_total = 0.0, 0.0, 0.0
        top1_correct_total_letter, top3_correct_total_letter, top5_correct_total_letter = 0.0, 0.0, 0.0

        total_letters_count = 0.0
        input_letters_count = 0.0

        testfilein = open(data, "r")
        step = 0
        for sentence in testfilein:
            if len(sentence) == 0:
                break
            # print('test sentence is :')
            # print(sentence)
            lm_data_x, labels_array = self.sentence2list(sentence)

            step = step + 1
            print("step:", step)
            length = len(lm_data_x)
            if length > 31:
                length = 31
            for i in range((length - 1)):
                if i == 0:
                    past_ids = [0]
                else:
                    past_ids = [self.token2id_out.get(lm_data_x[i - 1], 0)]
                letters_ids = past_ids + [self.token2id_in_letters.get(letter, 0) for letter in labels_array[i]]
                letters_len = len(letters_ids)
                # continue_predict = True
                total_letters_count = total_letters_count + letters_len
                input_letters_count += 1  # kongge
                # print('input words :')
                # print(lm_data_x[:i+1])

                temp_y = labels_array[i]
                if letters_len > 30:
                    letters_len = 30
                for l in range(letters_len):
                    # print(temp_y)
                    input_letters_count += 1
                    input_letters_ids = np.array(np.hstack(([letters_ids[:l + 1]], np.zeros([1, 30 - l - 1]))),
                                                 dtype=np.int32)
                    # print(input_letters_ids)
                    interpreter_letter.set_tensor(input_details_letter[0]['index'], input_letters_ids)
                    # interpreter.set_tensor(input_details[1]['index'], np.array(30, dtype=np.int32))
                    interpreter_letter.invoke()

                    output_data_letters = interpreter_letter.get_tensor(output_details_letter[0]['index'])

                    top_k_prediction_letters = output_data_letters[l]
                    # print(top_k_prediction_letters)
                    predict_letters = [self.id2token_out.get(k, 0) for k in top_k_prediction_letters]
                    # print(predict_letters)
                    top1_correct_letter = np.sum((predict_letters[0] == temp_y))
                    top3_correct_letter = top1_correct_letter + np.sum((predict_letters[1] == temp_y)) \
                                          + np.sum((predict_letters[2] == temp_y))
                    # top5_correct = top3_correct + np.sum((predict[3] == temp_y) ) \
                    #                + np.sum((predict[4] == temp_y) )
                    if top3_correct_letter > 0:
                        # continue_predict = False
                        # top5_correct_total += top5_correct
                        break
                    # time.sleep(2)

        save_predict = (total_letters_count - input_letters_count) / total_letters_count
        print("saving predict: = {0}".format(save_predict), file=logfile)
        logfile.flush()
        end_time = time.time()
        print("Test time = {0}".format(end_time - start_time), file=logfile)
        logfile.flush()
        logfile.close()

    def test_mix(self, sess, lm_path, letter_path, data, vocab_path):
        outputs = []
        vocab_word = vocab_path + '/vocab_out'
        vocab_in_letters = vocab_path + '/vocab_in_letters'

        with open(vocab_word, mode="r", encoding="utf-8") as f:
            for line in f:
                token, id = line.split("##")
                id = int(id)
                self.id2token_out[id] = token
                self.token2id_out[token] = id
        with open(vocab_in_letters, mode="r", encoding="utf-8") as f:
            for line in f:
                token, id = line.split("##")
                id = int(id)
                self.id2token_in_letters[id] = token
                self.token2id_in_letters[token] = id
        # print(self.token2id_in_letters)
        interpreter = tf.lite.Interpreter(model_path=lm_path)

        input_details = interpreter.get_input_details()
        output_details = interpreter.get_output_details()

        interpreter.allocate_tensors()

        interpreter_letter = tf.lite.Interpreter(model_path=letter_path)

        input_details_letter = interpreter_letter.get_input_details()
        output_details_letter = interpreter_letter.get_output_details()

        interpreter_letter.allocate_tensors()

        """Runs the model on the given data."""
        logfile = open('test_mix.log', 'a+')
        start_time = time.time()

        prediction_made = 0.0
        top1_correct_total, top3_correct_total, top5_correct_total = 0.0, 0.0, 0.0
        top1_correct_total_letter, top3_correct_total_letter, top5_correct_total_letter = 0.0, 0.0, 0.0

        total_letters_count = 0.0
        input_letters_count = 0.0

        testfilein = open(data, "r")
        step = 0
        for sentence in testfilein:
            if len(sentence) == 0:
                break
            # print('test sentence is :')
            print(sentence)
            lm_data_x, labels_array = self.sentence2list(sentence)

            step = step + 1
            print(step)
            length = len(lm_data_x)
            if length > 31:
                length = 31
            for i in range(length - 1):
                letters_ids = [self.token2id_in_letters.get(letter, 0) for letter in labels_array[i]]
                letters_len = len(letters_ids)
                # continue_predict = True
                total_letters_count = total_letters_count + letters_len + 1
                input_letters_count += 1  # kongge
                # print('input words :')
                # print(lm_data_x[:i+1])

                temp_y = labels_array[i]
                if letters_len > 30:
                    letters_len = 30
                for l in range(letters_len):
                    print(temp_y)
                    input_letters_count += 1
                    input_letters_ids = np.array(np.hstack(([letters_ids[:l + 1]], np.zeros([1, 30 - l - 1]))),
                                                 dtype=np.int32)
                    print(input_letters_ids)
                    interpreter_letter.set_tensor(input_details_letter[0]['index'], input_letters_ids)
                    # interpreter.set_tensor(input_details[1]['index'], np.array(30, dtype=np.int32))
                    interpreter_letter.invoke()

                    output_data_letters = interpreter_letter.get_tensor(output_details_letter[0]['index'])

                    top_k_prediction_letters = output_data_letters[l]
                    predict_letters = [self.id2token_out.get(k, 0) for k in top_k_prediction_letters]
                    print(predict_letters)
                    top1_correct_letter = np.sum((predict_letters[0] == temp_y))
                    top3_correct_letter = top1_correct_letter + np.sum((predict_letters[1] == temp_y)) \
                                          + np.sum((predict_letters[2] == temp_y))
                    # top5_correct = top3_correct + np.sum((predict[3] == temp_y) ) \
                    #                + np.sum((predict[4] == temp_y) )
                    if top3_correct_letter > 0:
                        # continue_predict = False
                        # top5_correct_total += top5_correct
                        break
                    # time.sleep(2)
                past_ids = self.words2ids(lm_data_x[:i + 1])
                # if self.word2id(nextword) >36:
                # if self.word2id(lm_data_x[i])>2:
                prediction_made += 1

                input_x = past_ids

                input_x = np.array(input_x, dtype=np.int32)
                # print(input_x)
                pos = len(past_ids)
                temp_x = np.array(np.hstack(([input_x], np.zeros([1, 30 - pos]))), dtype=np.int32)

                interpreter.set_tensor(input_details[0]['index'], temp_x)
                # interpreter.set_tensor(input_details[1]['index'], np.array(30, dtype=np.int32))
                interpreter.invoke()

                output_data = interpreter.get_tensor(output_details[0]['index'])
                # print(output_data)
                top_k_prediction = output_data[i]

                predict = [self.id2token_out.get(i, 0) for i in top_k_prediction]
                # print(predict)
                # print(predict)
                top1_correct = np.sum((predict[0] == temp_y))
                top3_correct = top1_correct + np.sum((predict[1] == temp_y)) \
                               + np.sum((predict[2] == temp_y))
                top4_correct = top3_correct + np.sum((predict[3] == temp_y))
                top5_correct = top3_correct + np.sum((predict[3] == temp_y)) \
                               + np.sum((predict[4] == temp_y))
                # if self.word2id(nextword) >36:
                top1_correct_total += top1_correct
                # top3_correct_total += top3_correct
                if '<unk>' in predict[:3]:
                    if predict[3] is not '<unk>':
                        top3_correct_total += top4_correct
                    elif predict[4] is not '<unk>':
                        top3_correct_total += top5_correct
                else:
                    top3_correct_total += top3_correct
                top5_correct_total += top5_correct

                # if top3_correct>0:
                #     print('hit!')
                #     print(temp_y)
                #     print(predict[:3])

        top1_acc = top1_correct_total / prediction_made
        top3_acc = top3_correct_total / prediction_made
        top5_acc = top5_correct_total / prediction_made

        save_predict = (total_letters_count - input_letters_count) / total_letters_count
        # Prediction accuracy information:
        print(
            "Language model: Top1 accuracy = {0}, top3 accuracy = {1}, top5 accuracy = {2} ".format(top1_acc, top3_acc,
                                                                                                    top5_acc),
            file=logfile)
        print("saving predict: = {0}".format(save_predict), file=logfile)
        logfile.flush()
        end_time = time.time()
        print("Test time = {0}".format(end_time - start_time), file=logfile)
        logfile.flush()
        logfile.close()

    def testlitelm(self, sess, tflitepath, data, vocab_path):
        outputs = OrderedDict()
        targets = []
        vocab_word = vocab_path + '/vocab_out'

        with open(vocab_word, mode="r", encoding="utf-8") as f:
            for line in f:
                token, id = line.split("##")
                id = int(id)
                self.id2token_out[id] = token
                self.token2id_out[token] = id
        interpreter = tf.lite.Interpreter(model_path=tflitepath)

        input_details = interpreter.get_input_details()
        output_details = interpreter.get_output_details()

        interpreter.allocate_tensors()
        """Runs the model on the given data."""
        logfile = open('testlitelm.log', 'a+')
        start_time = time.time()

        prediction_made = 0.0
        top1_correct_total, top3_correct_total, top5_correct_total = 0.0, 0.0, 0.0
        top1_empty_correct_total, top3_empty_correct_total, top5_empty_correct_total = 0.0, 0.0, 0.0
        top1_complete_correct_total, top3_complete_correct_total, top5_complete_correct_total = 0.0, 0.0, 0.0

        testfilein = open(data, "r")
        test_cases = [
            "Faith Emenes Delk Thank you Dan for posting this. We will be watching. Happy Independence Day to you. We love our President and you, as well."]
        test_input_id = [1781, 30, 30, 306, 38, 3668, 43, 2308, 55, 59, 58, 52, 599, 201, 3413, 132, 33, 38, 59, 109,
                         145, 342, 34, 38, 57, 133]
        step = 0
        for __index, sentence in enumerate(test_cases):
            res_dict = {}
            sentence = sentence.strip()
            res_dict[sentence] = {}
            # print('test sentence is :')
            print(sentence.strip())
            lm_data_x, labels_array = self.sentence2list(sentence)  # 读单词  输入/输出

            step = step + 1
            print("step:", step)
            length = len(lm_data_x)
            # if length >31:
            #     length =31
            for i in range((length)):
                # print('input words :')
                # print(lm_data_x[:i+1])
                res_dict[sentence][i] = {}
                temp_y = labels_array[i]
                # print("temp_y:",temp_y)
                id_dict = self.word2id(temp_y, return_word=True, return_processed=True)
                # print(id_dict)
                temp_y = id_dict["processed"]  # 处理后的词汇

                targets.append(temp_y)
                # print(temp_y)
                # print(letter_ids)
                if i < 30:
                    past_ids = self.words2ids(lm_data_x[:i + 1])  # 每次读30个词
                    print("past_ids：", past_ids, i)
                else:
                    past_ids = self.words2ids(lm_data_x[i + 1 - 30:i + 1])
                    print("past_ids：", past_ids, i)
                # if self.word2id(temp_y) >32:
                # if self.word2id(lm_data_x[i])>2:
                prediction_made += 1

                input_x = past_ids

                input_x = np.array(input_x, dtype=np.int32)

                pos = len(past_ids)
                if pos <= 30:
                    temp_x = np.array(np.hstack(([input_x], np.zeros([1, 30 - pos]))), dtype=np.int32)
                else:
                    temp_x = np.array([input_x], dtype=np.int32)
                res_dict[sentence][i]["input_ids"] = temp_x
                res_dict[sentence][i]["target"] = temp_y

                interpreter.set_tensor(input_details[0]['index'], temp_x)
                # interpreter.set_tensor(input_details[1]['index'], np.array(30, dtype=np.int32))
                interpreter.invoke()

                output_data = interpreter.get_tensor(output_details[0]['index'])
                # print(output_data)
                if i < 30:
                    top_k_prediction = output_data[i]
                else:
                    top_k_prediction = output_data[-1]

                predict = [self.id2token_out.get(i, 0) for i in top_k_prediction]
                _input = " ".join([self.id2token_out.get(i, 0) for i in input_x])
                # print(_input," :" ,predict)
                outputs[(_input, __index, i)] = predict
                res_dict[sentence][i]["prediction"] = predict
                # print(_input)
                top1_correct = np.sum((predict[0] == temp_y))
                top3_correct = top1_correct + np.sum((predict[1] == temp_y)) \
                               + np.sum((predict[2] == temp_y))
                top5_correct = top3_correct + np.sum((predict[3] == temp_y)) \
                               + np.sum((predict[4] == temp_y))
                # if self.word2id(temp_y) >32:
                top1_correct_total += top1_correct
                top3_correct_total += top3_correct
                top5_correct_total += top5_correct
                # if '<unk>' in predict[:3]:
                #     if predict[3] is not '<unk>':
                #         top3_correct_total += top4_correct
                #     elif predict[4] is not '<unk>':
                #         top3_correct_total += top5_correct
                # else:
                #     top3_correct_total += top3_correct
                # top5_correct_total += top5_correct
                # time.sleep(1)
                # if top3_correct>0:
                #    #print('hit!')
                #    #print(temp_y)
                #    print(predict[:5])

        top1_acc = top1_correct_total / prediction_made
        top3_acc = top3_correct_total / prediction_made
        top5_acc = top5_correct_total / prediction_made
        # Prediction accuracy information:
        print(
            "Language model: Top1 accuracy = {0}, top3 accuracy = {1}, top5 accuracy = {2} ".format(top1_acc, top3_acc,
                                                                                                    top5_acc),
            file=logfile)
        logfile.flush()
        end_time = time.time()
        print("Test time = {0}".format(end_time - start_time), file=logfile)
        logfile.flush()
        logfile.close()
        return outputs, targets, res_dict

    def testliteletter(self, sess, tflitepath, data, vocab_path):
        vocab_letters = vocab_path + '/vocab_in_letters'
        vocab_word = vocab_path + '/vocab_out'
        with open(vocab_letters, mode="r", encoding="utf-8") as f:
            for line in f:
                token, id = line.strip().split("##")
                id = int(id)
                self.id2token_in_letters[id] = token
                self.token2id_in_letters[token] = id
        with open(vocab_word, mode="r", encoding="utf-8") as f:
            for line in f:
                token, id = line.split("##")
                id = int(id)
                self.id2token_out[id] = token
                self.token2id_out[token] = id
        interpreter = tf.lite.Interpreter(model_path=tflitepath)

        input_details = interpreter.get_input_details()
        output_details = interpreter.get_output_details()
        # print(input_details)
        # print(output_details)
        interpreter.allocate_tensors()
        """Runs the model on the given data."""
        logfile = open('testliteletter.log', 'a+')
        start_time = time.time()
        fetches = {}
        batch_size = self.batch_size

        prediction_made = 0.0
        top1_correct_total, top3_correct_total, top5_correct_total = 0.0, 0.0, 0.0
        top1_empty_correct_total, top3_empty_correct_total, top5_empty_correct_total = 0.0, 0.0, 0.0
        top1_complete_correct_total, top3_complete_correct_total, top5_complete_correct_total = 0.0, 0.0, 0.0

        shufflesize = self.batch_size * 1000
        repeatnum = 1

        lm_in_word_list = []
        with codecs.open(data, "r", encoding="utf-8") as f:
            for line in f.readlines():
                # lm_in,lm_out = line.strip().split("|#|")
                # print(lm_out)
                lm_in_word_list.append(line)

        epoch_size = len(lm_in_word_list)
        step = 1
        epochs = epoch_size
        print(epoch_size)
        while (step < epoch_size):
            lm_data_x = self.sentence2list(lm_in_word_list[step])
            # print(lm_data_x)
            step = step + 1
            print(step)
            if len(lm_data_x) - 1 > 10:
                length = 10
            else:
                length = len(lm_data_x) - 1
            for i in range(0, length):
                # currword = lm_data_x[i]
                nextword = lm_data_x[i]
                letters = [x for x in nextword]
                # print(letters)
                letter_ids = self.letters2ids(letters)
                # print(letter_ids)
                temp_y = nextword
                if i == 0:
                    past_ids = []
                else:
                    past_ids = self.words2ids(lm_data_x[:i])
                # if self.word2id(nextword) >36:
                prediction_made += 1

                if len(letter_ids) > 3:
                    letters_len = 3
                else:
                    letters_len = len(letter_ids)
                for k in range(letters_len):
                    if i == 0:
                        curr_l_ids = letter_ids[:k + 1]
                    else:
                        curr_l_ids = letter_ids[:k]
                    input_x = past_ids + curr_l_ids
                    pos = len(input_x)
                    input_x = np.array(input_x, dtype=np.int32)
                    # print(input_x)

                    temp_x = np.array(np.hstack(([input_x], np.zeros([1, 40 - pos]))), dtype=np.int32)

                    interpreter.set_tensor(input_details[0]['index'], temp_x)
                    # interpreter.set_tensor(input_details[1]['index'], np.array(30, dtype=np.int32))
                    interpreter.invoke()

                    output_data = interpreter.get_tensor(output_details[0]['index'])
                    # print(output_data)
                    top_k_prediction = output_data[pos - 1]

                    predict = [self.id2token_out.get(i, 0) for i in top_k_prediction]
                    # print(predict)
                    top1_correct = np.sum((predict[0] == temp_y))
                    top3_correct = top1_correct + np.sum((predict[1] == temp_y)) \
                                   + np.sum((predict[2] == temp_y))
                    top5_correct = top3_correct + np.sum((predict[3] == temp_y)) \
                                   + np.sum((predict[4] == temp_y))
                    # if self.word2id(nextword) >36:
                    top1_correct_total += top1_correct
                    top3_correct_total += top3_correct
                    top5_correct_total += top5_correct
                    if top3_correct > 0:
                        break

        top1_acc = top1_correct_total / prediction_made
        top3_acc = top3_correct_total / prediction_made
        top5_acc = top5_correct_total / prediction_made
        # Prediction accuracy information:
        print(
            "Language model: Top1 accuracy = {0}, top3 accuracy = {1}, top5 accuracy = {2} ".format(top1_acc, top3_acc,
                                                                                                    top5_acc),
            file=logfile)
        logfile.flush()
        end_time = time.time()
        print("Test time = {0}".format(end_time - start_time), file=logfile)
        logfile.flush()
        logfile.close()
