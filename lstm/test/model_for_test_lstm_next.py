from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

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


# from model import *


class LSTMModel(object):
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

    def ifneedpredict(self, curr):
        flag = False
        if curr.strip() == "":
            flag = True
        else:
            END_WITH_SYMBOL_REGEX_DEFAULT = re.compile("([a-zA-Z']+)([^a-zA-Z']+$)")
            if re.sub(END_WITH_SYMBOL_REGEX_DEFAULT, lambda x: x.group(1), curr.strip()) != curr.strip():
                flag = True
        return flag

    def letters2ids(self, letters):
        # letters_split = re.split("\\s+", letters)
        return [self.token2id_in_letters[self.start_str]] + [self.token2id_in_letters.get(letter, 0) for letter in
                                                             letters]

    def word2id_in(self, word, return_word=False, return_processed=False):
        # print("this this this ")
        tmp_dict = {}
        _word_processed = word
        word_in = copy.deepcopy(word)
        END_WITH_SYMBOL_REGEX_DEFAULT = re.compile("([a-zA-Z']+)([^a-zA-Z']+$)")
        # SYMBOL_SERIAL_REGEX = re.compile("^[^a-z0-9A-Z']+$")
        NUM_REGEX = re.compile("[+-]*[0-9]+.*[0-9]*")
        PUN_REGEX = re.compile("[^a-zA-Z0-9']")
        # if re.search(SYMBOL_SERIAL_REGEX, word):
        #     tmp_dict["id"] = self.token2id_out.get(self.unk_str)
        #     tmp_dict["out"] = self.unk_str
        #     tmp_dict["processed"] = word[0]
        #     return tmp_dict
        if word in self.token2id_in_words:
            word_in = word
        elif word.lower() in self.token2id_in_words:
            # _word_processed = copy.deepcopy(word.lower())
            word_in = word.lower()
        else:
            # _word_processed = copy.deepcopy(word)
            word = re.sub(END_WITH_SYMBOL_REGEX_DEFAULT, lambda x: x.group(1), word)
            # _word_processed = copy.deepcopy(word)
            if word in self.token2id_in_words:
                word_in = word
            elif word.lower() in self.token2id_in_words:
                word_in = word.lower()
            elif re.match(NUM_REGEX, word):
                word_in = self.token2id_in_words[self.num_str]
            elif re.match(PUN_REGEX, word):
                word_in = self.token2id_in_words[self.pun_str]
            else:
                word_in, word_processed = self.unk_str, word_in

        rid = self.token2id_in_words.get(word_in, -1)

        if rid == -1:
            tmp_dict["id"] = self.token2id_in_words[self.unk_str]
        else:
            tmp_dict["id"] = rid
        if return_word:
            tmp_dict["out"] = word_in

        tmp_dict["processed"] = _word_processed
        return tmp_dict

    def word2id_out(self, word, return_word=False, return_processed=False):
        tmp_dict = {}
        _word_processed = word
        word_out = copy.deepcopy(word)
        END_WITH_SYMBOL_REGEX_DEFAULT = re.compile("([a-zA-Z']+)([^a-zA-Z']+$)")
        # SYMBOL_SERIAL_REGEX = re.compile("^[^a-z0-9A-Z']+$")

        if word in self.token2id_out:
            word_out = word
        elif word.lower() in self.token2id_out:
            word_out = word.lower()
        else:
            word = re.sub(END_WITH_SYMBOL_REGEX_DEFAULT, lambda x: x.group(1), word)

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
        # return [self.eos_id] + [self.word2id(word) for word in words if len(word) > 0]
        return [self.word2id(word) for word in words if len(word) > 0]

    def sentence2list(self, sentence):
        words_array = re.split(' ', sentence)
        # word_letters = words_array[-1]
        new_words_array = [self.eos_str] + words_array[:-1]  # 去掉最后一个单词 +起始位标识符
        labels_array = words_array  # 所有单词
        # letters = ' '.join(word_letters)
        # words_ids = self.words2ids(words_array)
        # letters_ids = self.letters2ids(letters)
        return new_words_array, labels_array

    def testlite_lstm(self, sess, lm_tflitepath, kc_tflitepath, data, vocab_path):  ###读取文件
        records = []
        all_correct = 0
        all_count = 0
        logfile = open('testlite_lstm.log', 'w')
        vocab_in_word = vocab_path + '/vocab_in_words'
        vocab_out_word = vocab_path + '/vocab_out'
        vocab_in_letters = vocab_path + '/vocab_in_letters'
        with open(vocab_in_word, mode="r", encoding="utf-8") as f:
            for line in f:
                token, id = line.split("##")
                id = int(id)
                self.id2token_in_words[id] = token
                self.token2id_in_words[token] = id
                # logfile.write(line.strip())
        # print("token2id_in_words len:",len(self.token2id_in_words),self.token2id_in_words)
        with open(vocab_out_word, mode="r", encoding="utf-8") as f:
            for line in f:
                token, id = line.split("##")
                id = int(id)
                self.id2token_out[id] = token
                self.token2id_out[token] = id
        # print("token2id_out len:", len(self.token2id_out))
        with open(vocab_in_letters, mode="r", encoding="utf-8") as f:
            for line in f:
                token, id = line.split("##")
                id = int(id)
                self.id2token_in_letters[id] = token
                self.token2id_in_letters[token] = id
        lm_interpreter = tf.lite.Interpreter(model_path=lm_tflitepath)
        kc_interpreter = tf.lite.Interpreter(model_path=kc_tflitepath)
        lm_input_details = lm_interpreter.get_input_details()
        lm_output_details = lm_interpreter.get_output_details()
        kc_input_details = kc_interpreter.get_input_details()
        kc_output_details = kc_interpreter.get_output_details()
        lm_interpreter.allocate_tensors()
        kc_interpreter.allocate_tensors()
        # print(lm_input_details)
        # print(lm_output_details)
        # print(kc_input_details)
        # print(kc_output_details)
        """Runs the model on the given data."""

        testfilein = open(data, "r")  # 读取测试文件
        sentence = "Mindy Olander It feels amazing to have a president who brings a massive sense of "

        testfileout_id = []
        step = 0

        # for sentence in testfilein:
        correct = 0
        count = 0
        tmp_dict = {}
        testfilein_id = []
        tmp_dict[sentence] = {}
        lm_data_x, labels_array = self.sentence2list(sentence.strip())  # 读取输入输出
        count += len(labels_array)
        step = step + 1
        # print(step)  # 语句行数
        length = len(lm_data_x)  # 读取输入

        lm_output_state = np.zeros([2, 2, 1, 400], dtype=np.float32)
        kc_output_state = np.zeros([2, 2, 1, 400], dtype=np.float32)
        for i in range((length)):
            temp_y = labels_array[i]  # 输出
            curr_id = self.word2id_in(lm_data_x[i], return_word=True)  # 输入转id  按照vocab_in_words Faith
            temp_id = self.word2id_out(temp_y, return_word=True)
            letters_ids = self.letters2ids(temp_y)  # 将输出的单词转换为键码形式 Emenes
            if i > 0:  # 语句正式输入 去掉标识位
                input_x = curr_id['id']  ## 当前词id
                testfilein_id.append(input_x)
                input_x = np.array([input_x], dtype=np.int32)

                lm_interpreter.set_tensor(lm_input_details[0]['index'], input_x)
                lm_interpreter.set_tensor(lm_input_details[1]['index'], lm_output_state)

                lm_interpreter.invoke()
                # print('invoke!!!')
                lm_output_state = lm_interpreter.get_tensor(lm_output_details[0]['index'])

                #  键码模型
                input_letter = letters_ids[0]  # 如果是起始位 键码输入第一个单词 否则顺延
                input_letter = np.array([input_letter], dtype=np.int32)
                # if length > 0:  # 是正式单词的起始位
                kc_input_state = lm_output_state  # 先用语言模型

                kc_interpreter.set_tensor(kc_input_details[0]['index'], input_letter)
                kc_interpreter.set_tensor(kc_input_details[1]['index'], kc_input_state)
                kc_interpreter.set_tensor(kc_input_details[2]['index'], np.array(20, dtype=np.int32))
                kc_interpreter.invoke()
                # print('invoke!!!')
                kc_output_state = kc_interpreter.get_tensor(kc_output_details[0]['index'])
                kc_output_prob = kc_interpreter.get_tensor(kc_output_details[1]['index'])

                kc_output_idx = kc_interpreter.get_tensor(kc_output_details[2]['index'])
                predict_top10 = []
                predict_top10_id = []
                for predict in [id for id in kc_output_idx[-1]]:
                    predict_words = self.id2token_out.get(predict, "<unk>")
                    if len(predict_top10) < 10:
                        if predict_words in ["<eos>", "<und>", "<unk>"]:
                            continue
                        else:
                            predict_top10.append(predict_words)
                            predict_top10_id.append(str(predict))
                    else:
                        break
                logfile.write("currword :" + str(lm_data_x[i]).strip() + '\t')
                logfile.write("currword id :" + str(curr_id["id"]).strip() + '\n')
                logfile.write("top 10 id :\t[" + str(",".join(predict_top10_id)).strip() + ']\n')
                logfile.write("top 10 :\t[" + str(",".join(predict_top10)).strip() + ']\n')
                flag = False
                #  碰到有空的情况
                if temp_y == "":
                    flag = self.ifneedpredict(curr_id["processed"])
                if flag:  # 直接预测成功
                    logfile.write("target:为空 并且前一个词以标点结尾" + '\t')
                    # logfile.write("target id:" + str(target_id["id"]).strip() + '\n')
                    # logfile.write("为空 并且前一个词以标点结尾\n")
                    print("为空 并且前一个词以标点结尾")
                    correct += 1
                    logfile.write("correctly" + '\n')
                    continue
                else:  # 在进行比较
                    target_id = self.word2id_out(temp_y)
                    logfile.write("target:" + str(temp_y).strip() + '\t')
                    logfile.write("target id:" + str(target_id["id"]).strip() + '\n')
                    # print("target:", temp_y)
                    # print("target id:", target_id["id"])
                    if str(target_id["id"]) in predict_top10_id[:3]:
                        correct += 1
                        logfile.write("correctly" + '\n')
                        # print("correctly")
                    else:
                        logfile.write("got wrong" + '\n')
                        # print("got wrong")
        testfilein_id.append(target_id["id"])
        result = "line input id :\t" + str(testfilein_id) + "\t总词数：\t" + str(count) + "\t预测成功词数：\t" + str(correct)
        logfile.write(result.strip() + '\n')
        print("line input id :", testfilein_id, "总词数：", count, "预测成功词数：", correct)
        all_count += count
        all_correct += correct
        all_result = "line count:\t" + str(step) + "\tall count:\t" + str(
            all_count - step) + "\tall correct count:\t" + str(all_correct)
        logfile.write(all_result.strip() + '\n')
        print("line count:", step, "all count:", all_count - step, "all correct count:", all_correct)
        return records

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
            print(sentence)
            lm_data_x, labels_array = self.sentence2list(sentence)

            step = step + 1
            print(step)
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
        step = 0
        for sentence in testfilein:
            # print('test sentence is :')
            # print(sentence)
            lm_data_x, labels_array = self.sentence2list(sentence)

            step = step + 1
            print(step)
            length = len(lm_data_x)
            # if length >31:
            #     length =31
            for i in range((length - 1)):
                # print('input words :')
                # print(lm_data_x[:i+1])

                temp_y = labels_array[i]
                # print(temp_y)
                # print(letter_ids)
                if i < 30:
                    past_ids = self.words2ids(lm_data_x[:i + 1])
                else:
                    past_ids = self.words2ids(lm_data_x[i + 1 - 30:i + 1])
                # if self.word2id(temp_y) >32:
                # if self.word2id(lm_data_x[i])>2:
                prediction_made += 1

                input_x = past_ids

                input_x = np.array(input_x, dtype=np.int32)
                # print(input_x)
                pos = len(past_ids)
                if pos <= 30:
                    temp_x = np.array(np.hstack(([input_x], np.zeros([1, 30 - pos]))), dtype=np.int32)
                else:
                    temp_x = np.array([input_x], dtype=np.int32)

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
                # print(predict)
                # print(predict)
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
                if top3_correct > 0:
                    print('hit!')
                    print(temp_y)
                    print(predict[:3])

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
