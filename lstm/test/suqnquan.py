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

    def letters2ids(self, letters):
        # letters_split = re.split("\\s+", letters)
        return [self.token2id_in_letters[self.start_str]] + [self.token2id_in_letters.get(letter.lower(), 0) for letter in
                                                             letters if len(letter) > 0]

    def word2id(self, word, return_word=False, return_processed=False):
        tmp_dict = {}
        _word_processed = word
        word_out = copy.deepcopy(word)
        END_WITH_SYMBOL_REGEX_DEFAULT = re.compile("([a-zA-Z']+)([^a-zA-Z']+$)")
        SYMBOL_SERIAL_REGEX = re.compile("^[^a-z0-9A-Z']+$")
        if re.search(SYMBOL_SERIAL_REGEX, word):
            tmp_dict["id"] = self.token2id_out.get(self.unk_str)
            tmp_dict["out"] = self.unk_str
            tmp_dict["processed"] = word[0]
            return tmp_dict
        if word in self.token2id_out:
            word_out = word
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

        tmp_dict["id"] = rid
        if return_word:
            tmp_dict["out"] = word_out
        if rid == -1:
            tmp_dict["id"] = self.token2id_out[self.unk_str]

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
        words_array = re.split('\\s+', sentence)
        # word_letters = words_array[-1]
        new_words_array = [self.eos_str] + words_array[:-1]
        labels_array = words_array
        # letters = ' '.join(word_letters)
        # words_ids = self.words2ids(words_array)
        # letters_ids = self.letters2ids(letters)
        return new_words_array, labels_array

    def testlite_lstm(self, sess, lm_tflitepath, kc_tflitepath, data, vocab_path):
        records = []
        vocab_int_word = vocab_path + '/vocab_in_words'
        vocab_out_word = vocab_path + '/vocab_out'
        vocab_in_letters = vocab_path + '/vocab_in_letters'
        with open(vocab_int_word, mode="r", encoding="utf-8") as f:
            for line in f:
                token, id = line.split("##")
                id = int(id)
                self.id2token_in_words[id] = token
                self.token2id_in_words[token] = id
        with open(vocab_out_word, mode="r", encoding="utf-8") as f:
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
        lm_interpreter = tf.lite.Interpreter(model_path=lm_tflitepath)
        kc_interpreter = tf.lite.Interpreter(model_path=kc_tflitepath)
        lm_input_details = lm_interpreter.get_input_details()
        lm_output_details = lm_interpreter.get_output_details()
        kc_input_details = kc_interpreter.get_input_details()
        kc_output_details = kc_interpreter.get_output_details()
        lm_interpreter.allocate_tensors()
        kc_interpreter.allocate_tensors()
        print(lm_input_details)
        print(lm_output_details)
        print(kc_input_details)
        print(kc_output_details)

        """Runs the model on the given data."""
        logfile = open('testlite_lstm.log', 'w')
        testfilein = open(data, "r")
        sentence = "Mindy Olander It feels amazing"
        step = 0
        # for sentence in testfilein:

        lm_data_x, labels_array = self.sentence2list(sentence)

        step = step + 1
        print(step)
        length = len(lm_data_x)

        lm_output_state = np.zeros([2, 2, 1, 400], dtype=np.float32)
        kc_output_state = np.zeros([2, 2, 1, 400], dtype=np.float32)
        for i in range((length)):  # 一句话拆成单词读取
            temp_y = labels_array[i]  # 输出
            # logfile.write(temp_y + '\ttarget\n')
            # logfile.write(lm_data_x[i] + '\tnow\n')
            curr_id = self.word2id(lm_data_x[i])  # 输入id
            letters_ids = self.letters2ids(temp_y)  # 输出单词字母转id
            # prediction_made+=1
            if i > 0:  # 去掉起始位
                input_x = curr_id['id']
                # print(input_x)
                input_x = np.array([input_x], dtype=np.int32)

                lm_interpreter.set_tensor(lm_input_details[0]['index'], input_x)
                lm_interpreter.set_tensor(lm_input_details[1]['index'], lm_output_state)

                lm_interpreter.invoke()
                # print('invoke!!!')
                lm_output_state = lm_interpreter.get_tensor(lm_output_details[0]['index'])
            curr = ""
            for j in range(len(letters_ids)):
                input_letter = letters_ids[j]
                curr += self.id2token_in_letters.get(input_letter, 0)
                logfile.write(self.id2token_in_letters.get(input_letter) + '\tnow letter\n')
                input_letter = np.array([input_letter], dtype=np.int32)
                if j == 0 and length > 0:
                    kc_input_state = lm_output_state
                else:
                    kc_input_state = kc_output_state
                kc_interpreter.set_tensor(kc_input_details[0]['index'], input_letter)
                kc_interpreter.set_tensor(kc_input_details[1]['index'], kc_input_state)
                kc_interpreter.set_tensor(kc_input_details[2]['index'], np.array(20, dtype=np.int32))
                # interpreter.set_tensor(input_details[1]['index'], np.array(30, dtype=np.int32))
                kc_interpreter.invoke()
                # print('invoke!!!')
                kc_output_state = kc_interpreter.get_tensor(kc_output_details[0]['index'])
                kc_output_prob = kc_interpreter.get_tensor(kc_output_details[1]['index'])
                kc_output_idx = kc_interpreter.get_tensor(kc_output_details[2]['index'])
                logfile.write("now input: "+curr+'\n')
                for predict in [id for id in kc_output_idx[-1]]:
                    predict_words = self.id2token_out.get(predict, "<unk>")
                    logfile.write(predict_words + '\t')
                    # print(predict_words)
                # print(kc_output_idx)
                # print(kc_output_prob)
        return records
