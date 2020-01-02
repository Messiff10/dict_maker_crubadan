#!/usr/bin/env python
# -*- coding: utf-8 -*-
import codecs
import os
import re
import sys

import emoji
import numpy as np
from collections import defaultdict

## letter|#|word
regex = re.compile('\s+')
regex2 = re.compile('')
unigrams_data = set()
emojiset = set()


def is_emoji(content):
    if re.match(emoji.get_emoji_regexp(), content):
        return True
    return False


def sentense2data(sentense_file, output_datafile):
    sentense_file_in = open(sentense_file, "r")  # 读文件
    data_file_out = open(output_datafile, 'w')  # 写文件
    for sentence in sentense_file_in:
        words = regex.split(sentence.strip())
        if len(words) > 1:
            # newwords = ''
            newwords = '\t'.join(words)
            # print(words)
            allletterslist = ''
            for word in words:
                if is_emoji(word):
                    letterslist = ' '
                else:
                    # letterslist=''
                    alist = [ch for ch in word.lower()]
                    letterslist = ' '.join(alist)
                allletterslist = allletterslist + '\t' + letterslist
            # allletterslist=allletterslist+'\t'+letterslist
            outputline = allletterslist[allletterslist.index('\t') + 1:] + "|#|" + newwords + '\n'
            # print(outputline)
            data_file_out.write(outputline)
    sentense_file_in.close()
    data_file_out.close()


def getemoji(emoji_path):
    with open(emoji_path, 'r', encoding='utf-8') as f_emoji:
        for line in f_emoji:
            emojis = line.strip().split('\t')
            if emojis[0].strip() not in emojiset:
                emojiset.add(emojis[0])


if __name__ == "__main__":
    language = "fr"
    data_folder = '/Users/ff/Desktop/train_data/' + language + '/coding/'
    # enUSunigram('/Users/ff/Desktop/train_data/'+language+'_unigram')
    # vocabinwords(data_folder+'/vocab_in_words')
    # vocabinout(data_folder+'/vocab_out')
    # data_folder_out = '/Users/ff/Desktop/测评数据/news/test'
    emoji_path = "/Users/ff/Desktop/train_data/emojis"
    names = []
    getemoji(emoji_path)
    for dir_path, subpaths, files in os.walk(data_folder):
        for name in filter(lambda x: x.endswith('test_data'), files):  # 文件夹下的所有文件
            file_path = os.path.join(dir_path, name)
            names.append(name)

    # regex = re.compile('\s+')
    for name in names:
        file_path = os.path.join(data_folder, name)
        print(file_path)

        senfile = file_path
        datafile = file_path.replace('test_data', 'test_data_dev')
        sentense2data(senfile, datafile)
        # sentense2id()
print("Finish Line")
