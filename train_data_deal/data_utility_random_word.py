#!/usr/bin/env python
# -*- coding: utf-8 -*-
import codecs
import itertools
import os
import random
import re
import sys

import emoji
import numpy as np
from collections import defaultdict
"""
键码匹配
单词和键码同时改变
"""
## letter|#|word
## 匹配键码和单词生成训练数据
regex = re.compile('\s+')
unigrams_data = set()
sequence_new = {}
#
def is_emoji(content):
    if re.match(emoji.get_emoji_regexp(), content):
        return True
    return False


def random_pick_freq(word,sequence, freqs):
    if word not in sequence_new.keys():
        # print(1)
        sequence_new[word] = []
        for x, y in zip(sequence, freqs):
            for z in [x] * int(y):
                sequence_new[word].append(z)
    while True:
        yield random.choice(sequence_new[word])


def sentense2data(sentense_file, output_datafile, wordmap_all):
    linenum = 0
    with open(sentense_file, "r", encoding='utf-8') as sentense_file_in:
        with open(output_datafile, 'w', encoding='utf-8') as data_file_out:
            for sentence in sentense_file_in:
                # number = random.randint(0, 10)
                words = regex.split(sentence.strip())
                # newwords = ''
                if len(words) > 1:
                    # newwords = '\t'.join(words)
                    # newwords = ''
                    # print(words)
                    allletterslist = ''
                    alllwordsslist = ''
                    for word in words:
                        letterslist = ''
                        if word in wordmap_all.keys():
                            # print(word)
                            # values = str(gtmaps[word]).split('@kika')
                            wordmap = random_pick_freq(word,wordmap_all[word].keys(), wordmap_all[word].values())
                            # print(wordmap)
                            noise_word = ''.join(itertools.islice(wordmap, 1))
                            # if word != noise_word:
                            #     print(word,noise_word)
                            alist = [ch for ch in noise_word.lower()]
                            letterslist = ' '.join(alist)
                            wordlist = noise_word
                        else:
                            if is_emoji(word):
                                letterslist = ' '
                                wordlist = word
                            else:
                                alist = [ch for ch in word.lower()]
                                letterslist = ' '.join(alist)
                                wordlist = word
                        allletterslist = allletterslist + '\t' + letterslist
                        alllwordsslist = alllwordsslist + '\t' + wordlist
                    linenum += 1
                    outputline = allletterslist[allletterslist.index('\t') + 1:] + "|#|" + alllwordsslist.strip() + '\n'
                    # print(sentence)
                    # print(outputline)
                    data_file_out.write(outputline)
        print("Line num", linenum)


maps = {}
gtmaps = {}


def getmap(map):
    wordmap = {}
    with open(map, 'r', encoding='utf-8') as map_:
        current_word = ""
        current_map = {}
        for line in map_:
            items = line.split("\t")
            desired_word = items[0].strip()
            keys = items[1].strip()
            freq = items[2].strip()

            if keys == "":  # 推荐正确，直接空格上屏
                continue

            if current_word == desired_word:
                current_map[keys] = freq
            else:
                if current_word != "":
                    wordmap[current_word] = current_map

                current_word = desired_word
                current_map = {}
                current_map[keys] = freq

        wordmap[current_word] = current_map
        # for word in wordmap.keys():
        #     print(word,wordmap[word])

    return wordmap


if __name__ == "__main__":
    # language = "ms_MY"
    file_path = "/Users/ff/Desktop/测评数据/转process/es_US_2q_no_emoji.txt"
    # file_path=sys.argv[1]
    # map = sys.argv[2]
    map = "/Users/ff/Desktop/测评数据/转process/es_US_map_sort.txt"
    names = []

    print(file_path)

    senfile = file_path
    datafile = file_path.replace('.txt', '.proword')
    wordmap_all = getmap(map)
    sentense2data(senfile, datafile, wordmap_all)
    # sentense2id()
print("Finish Line")
