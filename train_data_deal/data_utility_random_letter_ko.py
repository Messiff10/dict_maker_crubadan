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
针对韩语等特殊语言的键码匹配处理
韩语
"""
## letter|#|word
regex = re.compile('\s+')
unigrams_data = set()
regex2 = re.compile('')
sequence_new = {}
ko_words = set()
emojiset = set()
first_parts = ("ㄱ", "ㄲ", "ㄴ", "ㄷ", "ㄸ", "ㄹ", "ㅁ", "ㅂ", "ㅃ", "ㅅ", "ㅆ", "ㅇ", "ㅈ", "ㅉ", "ㅊ", "ㅋ", "ㅌ", "ㅍ", "ㅎ")
second_parts = (
    "ㅏ", "ㅐ", "ㅑ", "ㅒ", "ㅓ", "ㅔ", "ㅕ", "ㅖ", "ㅗ", "ㅗㅏ", "ㅗㅐ", "ㅗㅣ", "ㅛ", "ㅜ", "ㅜㅓ", "ㅜㅔ", "ㅜㅣ", "ㅠ", "ㅡ", "ㅡㅣ", "ㅣ")
third_parts = (
    "", "ㄱ", "ㄲ", "ㄳ", "ㄴ", "ㄵ", "ㄶ", "ㄷ", "ㄹ", "ㄺ", "ㄻ", "ㄼ", "ㄽ", "ㄾ", "ㄿ", "ㅀ", "ㅁ", "ㅂ", "ㅄ", "ㅅ", "ㅆ", "ㅇ", "ㅈ",
    "ㅊ", "ㅋ", "ㅌ", "ㅍ", "ㅎ")


def divide_korean(temp_string):
    print(temp_string)
    temp_string_value = ord(temp_string)
    part_1 = (temp_string_value - 44032) // 588
    part_2 = (temp_string_value - 44032 - part_1 * 588) // 28
    part_3 = (temp_string_value - 44032) % 28
    return first_parts[part_1] + second_parts[part_2] + third_parts[part_3]


def is_emoji(content):
    if re.match(emoji.get_emoji_regexp(), content):
        return True
    return False


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
                            ko_alist = [ch for ch in noise_word]
                            ko_alist_ = ""
                            for k_a in ko_alist:
                                if k_a >= u'\uAC00' and k_a <= u'\uD7AF':
                                    # if noise_word.strip() not in ko_words:
                                    ko_words.add(k_a.strip())
                                    divid_line = divide_korean(k_a)
                                else:
                                    divid_line = k_a
                                    alist = [ch for ch in divid_line]
                                    # ko_alist_=ko_alist_+str(alist)
                                    letterslist = letterslist + ''.join(alist)
                            letterslist = " ".join(letterslist)
                            letterslist = letterslist.replace("ㄳ", "ㄱ ㅅ").replace("ㄼ", "ㄹ ㅂ").replace("ㅄ", "ㅂ ㅅ") \
                                .replace("ㄵ", "ㄴ ㅈ").replace("ㄽ", "ㄹ ㅅ").replace("ㄶ", "ㄴ ㅎ").replace("ㄾ", "ㄹ ㅌ") \
                                .replace("ㄺ", "ㄹ ㄱ").replace("ㄿ", "ㄹ ㅍ").replace("ㄻ", "ㄹ ㅁ").replace("ㅀ", "ㄹ ㅎ")
                        else:
                            if word.strip() in emojiset:
                                letterslist = ' '
                            else:
                                ko_alist = [ch for ch in word]
                                alist = ""
                                for k_a in ko_alist:
                                    if k_a >= u'\uAC00' and k_a <= u'\uD7AF':
                                        # if word.strip() not in ko_words:
                                        ko_words.add(k_a.strip())
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
    file_path = "/Users/ff/Desktop/测评数据/转process/ko_user_web.txt"
    # file_path = sys.argv[1]
    # map = sys.argv[2]
    map = "/Users/ff/Desktop/测评数据/转process/ko_map_sort.txt"
    names = []
    emoji_path = "/Users/ff/Desktop/train_data/all_emojis"
    print(file_path)
    getemoji(emoji_path)
    senfile = file_path
    datafile = file_path.replace('.txt', '.proletter')
    wordmap_all = getmap(map)
    sentense2data(senfile, datafile, wordmap_all)
    # sentense2id()
print("Finish Line")
