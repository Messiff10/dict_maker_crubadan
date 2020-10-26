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
无map匹配
letter|#|word
"""

regex = re.compile('\s+')
unigrams_data = set()

sequence_new = {}
emojiset=set()


def sentense2data(sentense_file, output_datafile):
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
        print("false rate",float(ids/count))


maps = {}
gtmaps = {}

def getemoji(emoji_path):
    with open(emoji_path, 'r', encoding='utf-8') as f_emoji:
        for line in f_emoji:
            emojis = line.strip().split('\t')
            if emojis[0].strip() not in emojiset:
                emojiset.add(emojis[0])

if __name__ == "__main__":
    # language = "ms_MY"
    file_path =sys.argv[1]
    # file_path = sys.argv[1]
    # map = sys.argv[2]
    # map = "/Users/ff/Desktop/测评数据/nomap_process/map_sort_null.txt"
    names = []
    emoji_path = sys.argv[2]
    print(file_path)
    getemoji(emoji_path)
    senfile = file_path
    datafile = file_path.replace('.txt', '.proletter')
    # wordmap_all = getmap(map)
    # word_mapall={}
    sentense2data(senfile, datafile)
    # sentense2id()
print("Finish Line")
