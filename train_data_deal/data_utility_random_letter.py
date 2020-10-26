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

## letter|#|word
regex = re.compile('\s+')
unigrams_data = set()

sequence_new = {}

emojiset=set()
## 匹配键码生成训练数据

def random_pick_freq(word, sequence, freqs):
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
            ids = 0
            count = 0
            for sentence in sentense_file_in:
                # number = random.randint(0, 10)
                words = regex.split(sentence.strip())
                # newwords = ''
                if len(words) > 1:
                    newwords = '\t'.join(words)
                    # print(words)
                    allletterslist = ''
                    for word in words:
                        count += 1
                        letterslist = ''
                        if word in wordmap_all.keys():
                            # print(word)
                            # values = str(gtmaps[word]).split('@kika')
                            wordmap = random_pick_freq(word, wordmap_all[word].keys(), wordmap_all[word].values())
                            # print(wordmap)
                            noise_word = ''.join(itertools.islice(wordmap, 1))
                            if noise_word.strip() != word.strip():
                                ids += 1
                            alist = [ch for ch in noise_word.lower()]
                            letterslist = ' '.join(alist)
                        else:
                            if word.strip() in emojiset:
                                letterslist = ' '
                            else:
                                alist = [ch for ch in word.lower()]
                                letterslist = ' '.join(alist)
                        allletterslist = allletterslist + '\t' + letterslist
                    linenum += 1
                    outputline = allletterslist[allletterslist.index('\t') + 1:] + "|#|" + newwords + '\n'
                    # print(outputline)
                    data_file_out.write(outputline)
        data_file_out.close()
        sentense_file_in.close()
        print("Line num", linenum)
        print("false rate", float(ids / count))


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
    map_.close()
    return wordmap

def getemoji(emoji_path):
    with open(emoji_path, 'r', encoding='utf-8') as f_emoji:
        for line in f_emoji:
            emojis = line.strip().split('\t')
            if emojis[0].strip() not in emojiset:
                emojiset.add(emojis[0])
if __name__ == "__main__":
    # language = "ms_MY"
    file_path = sys.argv[1]
    # file_path = sys.argv[1]
    # map = sys.argv[2]
    map = sys.argv[2]
    names = []
    emoji_path = sys.argv[3]
    print(file_path)
    getemoji(emoji_path)
    senfile = file_path
    datafile = file_path.replace('.txt', '.proletter')
    wordmap_all = getmap(map)
    sentense2data(senfile, datafile, wordmap_all)
    # sentense2id()
print("Finish Line")
