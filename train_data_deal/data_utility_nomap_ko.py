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
韩语
无键码匹配生成特殊语言训练数据
"""
regex = re.compile('\s+')
unigrams_data = set()

sequence_new = {}
emojiset=set()
ko_words=set()
first_parts = ("ㄱ", "ㄲ", "ㄴ", "ㄷ", "ㄸ", "ㄹ", "ㅁ", "ㅂ", "ㅃ", "ㅅ", "ㅆ", "ㅇ", "ㅈ", "ㅉ", "ㅊ", "ㅋ", "ㅌ", "ㅍ", "ㅎ")
second_parts = (
    "ㅏ", "ㅐ", "ㅑ", "ㅒ", "ㅓ", "ㅔ", "ㅕ", "ㅖ", "ㅗ", "ㅗㅏ", "ㅗㅐ", "ㅗㅣ", "ㅛ", "ㅜ", "ㅜㅓ", "ㅜㅔ", "ㅜㅣ", "ㅠ", "ㅡ", "ㅡㅣ", "ㅣ")
third_parts = (
    "", "ㄱ", "ㄲ", "ㄳ", "ㄴ", "ㄵ", "ㄶ", "ㄷ", "ㄹ", "ㄺ", "ㄻ", "ㄼ", "ㄽ", "ㄾ", "ㄿ", "ㅀ", "ㅁ", "ㅂ", "ㅄ", "ㅅ", "ㅆ", "ㅇ", "ㅈ",
    "ㅊ", "ㅋ", "ㅌ", "ㅍ", "ㅎ")

def is_emoji(content):
    if re.match(emoji.get_emoji_regexp(), content):
        return True
    return False

def divide_korean(temp_string):
    # print(temp_string)
    temp_string_value = ord(temp_string)
    part_1 = (temp_string_value - 44032) // 588
    part_2 = (temp_string_value - 44032 - part_1 * 588) // 28
    part_3 = (temp_string_value - 44032) % 28
    return first_parts[part_1] + second_parts[part_2] + third_parts[part_3]

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
                        ko_alist_ = ""
                        if word.strip() in emojiset:
                            letterslist = ' '
                        else:
                            ko_alist = [ch for ch in word]
                            alist = ""
                            for k_a in ko_alist:
                                if k_a >= u'\uAC00' and k_a <= u'\uD7AF':
                                    # if word.strip() not in ko_words:
                                    # ko_words.add(k_a.strip())
                                    divid_line = divide_korean(k_a)
                                else:
                                    divid_line = k_a
                                alist = [ch for ch in divid_line]
                                letterslist = letterslist + ''.join(alist)
                            letterslist = " ".join(letterslist)
                            letterslist = letterslist.replace("ㄳ", "ㄱ ㅅ").replace("ㄼ", "ㄹ ㅂ").replace("ㅄ", "ㅂ ㅅ") \
                                    .replace("ㄵ", "ㄴ ㅈ").replace("ㄽ", "ㄹ ㅅ").replace("ㄶ", "ㄴ ㅎ").replace("ㄾ", "ㄹ ㅌ") \
                                    .replace("ㄺ", "ㄹ ㄱ").replace("ㄿ", "ㄹ ㅍ").replace("ㄻ", "ㄹ ㅁ").replace("ㅀ", "ㄹ ㅎ")
                        allletterslist = allletterslist + '\t' + letterslist
                    linenum += 1
                    outputline = allletterslist[allletterslist.index('\t') + 1:] + "|#|" + newwords + '\n'
                    # print(outputline)
                    data_file_out.write(outputline)
        data_file_out.close()
        sentense_file_in.close()
        print("Line num", linenum)
        print("false rate",float(ids/count))

def getemoji(emoji_path):
    with open(emoji_path, 'r', encoding='utf-8') as f_emoji:
        for line in f_emoji:
            emojis = line.strip().split('\t')
            if emojis[0].strip() not in emojiset:
                emojiset.add(emojis[0])

if __name__ == "__main__":
    file_path = "/Users/ff/Desktop/测评数据/nomap/ko_user_web.txt"
    names = []
    emoji_path = "/Users/ff/Desktop/train_data/all_emojis"
    print(file_path)
    getemoji(emoji_path)
    senfile = file_path
    datafile = file_path.replace('.txt', '.proletter')
    sentense2data(senfile, datafile)
print("Finish Line")
