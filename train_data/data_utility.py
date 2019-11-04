#!/usr/bin/env python
# -*- coding: utf-8 -*-
import codecs
import os
import re
import sys
import numpy as np
from collections import defaultdict
## letter|#|word

# class DataUtility:
#     def __init__(self, vocab_file_in_words=None, vocab_file_in_letters=None, vocab_file_out=None,
#                  full_vocab_file_in_words=None):
#
#         self.start_str = "<start>"
#         self.eos_str = "<eos>"
#         self.unk_str = "<unk>"
#         self.num_str = "<num>"
#         self.pun_str = "<pun>"
#         self.fullvocab_set = None
#         self.pad_id = 0
#
#         if vocab_file_in_words and vocab_file_in_letters and vocab_file_out:
#             self.id2token_in_words, self.id2token_in_letters, self.id2token_out = {}, {}, {}
#             self.token2id_in_words, self.token2id_in_letters, self.token2id_out = {}, {}, {}
#             with open(vocab_file_in_words, mode="r", encoding="utf-8") as f:
#                 for line in f:
#                     token, id = line.strip().split("##")
#                     id = int(id)
#                     self.id2token_in_words[id] = token
#                     self.token2id_in_words[token] = id
#             self.in_words_count = len(self.token2id_in_words)
#             self.eos_id = self.token2id_in_words[self.eos_str]
#
#             with open(vocab_file_in_letters, mode="r", encoding="utf-8") as f:
#                 for line in f:
#                     token, id = line.strip().split("##")
#                     id = int(id)
#                     self.id2token_in_letters[id] = token
#                     self.token2id_in_letters[token] = id
#             self.start_id = self.token2id_in_letters[self.start_str]
#             self.in_letters_count = len(self.token2id_in_letters)
#
#             with open(vocab_file_out, mode="r", encoding="utf-8") as f:
#                 for line in f:
#                     token, id = line.split("##")
#                     id = int(id)
#                     self.id2token_out[id] = token
#                     self.token2id_out[token] = id
#             self.out_words_count = len(self.token2id_out)
#
#         if full_vocab_file_in_words:
#             self.fullvocab_set = set()
#             with open(full_vocab_file_in_words, "r", encoding="utf-8") as f:
#                 for line in f:
#                     token, freq = line.split()
#                     self.fullvocab_set.add(token)
#             sys.stderr.write("Full vocabulary size: %d " % len(self.fullvocab_set))
#
#         #self.head_mask = defaultdict(lambda: np.zeros(shape=(self.phrase_count,), dtype=np.float32))
#         self.head_pick_id = None
#
#
#
#     def softmax(self, logits):
#         exp_logits = np.exp(logits)
#         exp_sum = np.expand_dims(np.sum(exp_logits, -1), -1)
#         return exp_logits / exp_sum
#
#     def word2id(self, word):
#         if re.match("^[a-zA-Z]$", word) or (word in self.token2id_in_words):
#             word_out = word
#         elif word.lower() in self.token2id_in_words:
#             word_out = word.lower()
#         elif re.match("^[+-]*[0-9]+.*[0-9]*$", word):
#             word_out = self.num_str
#         elif re.match("^[^a-zA-Z0-9']*$", word):
#             word_out = self.pun_str
#         else:
#             word_out = self.unk_str
#         rid = self.token2id_in_words.get(word_out, -1)
#         if rid == -1:
#             return self.token2id_in_words[self.unk_str]
#         return rid
#
#     def words2ids(self, words):
#         return [self.eos_id] + [self.word2id(word) for word in words if len(word) > 0]
#
#     def letters2ids(self, letters):
#         letters_split = re.split("\\s+", letters)
#         return [self.start_id] + [self.token2id_in_letters.get(letter, self.token2id_in_letters[self.unk_str])
#                                   for letter in letters_split if len(letter) > 0]
#
#     def outword2id(self, outword):
#         return self.token2id_out.get(outword, self.token2id_out[self.unk_str])
#
#     def ids2outwords(self, ids_out):
#         return [self.id2token_out.get(id, self.unk_str) for id in ids_out]
#
#     def ids2inwords(self, ids_in):
#         return [self.id2token_in_words.get(int(id), self.unk_str) for id in ids_in]
#
#     def data2ids_line(self, data_line):
#         data_line_split = re.split("\\|#\\|", data_line)
#         letters_line = data_line_split[0].split("\t")
#         words_line = data_line_split[1].strip().split("\t")
#         words_ids = self.words2ids(words_line)
#         letters_ids = [self.letters2ids(letters) for letters in letters_line]
#         words_num = len(words_ids)
#         letters_num = [len(letter_ids) for letter_ids in letters_ids]
#         return words_line, letters_line, words_ids, letters_ids, words_num, letters_num
#
#     def sentence2ids(self, sentence):
#         words_array = re.split('\\s+', sentence)
#         word_letters = words_array[-1]
#         words_array = words_array[:-1]
#         letters = ' '.join(word_letters)
#         words_ids = self.words2ids(words_array)
#         letters_ids = self.letters2ids(letters)
#         return words_ids, letters_ids, word_letters

def sentense2data(sentense_file,output_datafile):
    sentense_file_in = open(sentense_file, "r")
    data_file_out = open(output_datafile, 'w')
    for sentence in sentense_file_in:
        words = sentence.strip().split(' ')
        #print(words)
        letterslist=''
        i = 0
        newwords =''
        for word in words:
            if(word.strip() is not ""):
                newwords = newwords+word
                print(newwords)
                letters=''
                k = 0
                for le in word:
                    letters+=le
                    if k < (len(word)-1):
                        letters+=' '
                letterslist+=letters.lower()
                if i < (len(words)-1):
                    newwords+='\t'
                    letterslist+='\t'
                i+=1
        outputline = letterslist.strip()+"|#|"+newwords.strip()+'\n'
        data_file_out.write(outputline)
    sentense_file_in.close()
    data_file_out.close()

if __name__ == "__main__":
    data_folder = '/Users/ff/Desktop/测评数据/news/detok/'
    # data_folder_out = '/Users/ff/Desktop/测评数据/news/test'
    names = []
    for dir_path, subpaths, files in os.walk(data_folder):
        for name in filter(lambda x: x.endswith('.txt'), files):  # 文件夹下的所有文件
            file_path = os.path.join(dir_path, name)
            names.append(name)

    # regex = re.compile('\s+')
    for name in names:
        file_path = os.path.join(data_folder, name)
        print(file_path)

        senfile = file_path
        datafile = file_path.replace('.txt', '_test_data.txt')
        sentense2data(senfile,datafile)