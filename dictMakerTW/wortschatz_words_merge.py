# -*- coding: utf-8 -*-
import string
from utils.language_filter import is_latin__all

out_file_path = '/Users/xinmei/Downloads/其他语种/mt马耳他语/unigram/mt_unigram'

out_file = open(out_file_path, 'w')

words_freq = dict()
for i in ['mlt_newscrawl_2012_100K-words.txt', 'mlt_web_2012_300K-words.txt','mlt_wikipedia_2014_30K-words.txt','mlt_wikipedia_2016_30K-words.txt']:
    in_file_path = '/Users/xinmei/Downloads/其他语种/mt马耳他语/unigram/' + i
    in_file = open(in_file_path, 'r', encoding='utf-8')

    for line in in_file:
        words = line.strip().split('\t')[1]
        freq = int(line.strip().split('\t')[-1])
        for word in words.split(' '):
            if word in words_freq:
                words_freq[word] += freq
            else:
                words_freq[word] = freq

for i in sorted(words_freq.items(), key=lambda x: x[1], reverse=True):
    word = i[0]
    freq = str(i[1])
    all_latin = True
    for j in word:
        if not is_latin__all(j) or not str(j).isalpha():
            all_latin = False
            # print(word)
            break
    if all_latin:
        out_file.write(word + '\t' + freq + '\n')

