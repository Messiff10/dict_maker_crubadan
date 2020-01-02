import codecs
import os
import re

from utils.is_emoji import is_emoji
##  一元词表与爬取语料比较 使用爬取语料词频

# language = "fi"
# unigram_path = '/Users/ff/Desktop/train_data/' + language + '/' + language + '_unigram_null'
# file_path = '/Users/ff/Desktop/train_data/' + language + '/' + language + '_user_web_train/vocab_words'
# file_path_true = file_path.replace('_words', '_words_true')
# file_path_false = file_path.replace('_words', '_words_false')
import sys
# 将false字母表和词表比较，排除小写形式在词表中的词
import emoji

data_folder = '/Users/ff/Desktop/测评数据/与词表计较出false/'
names=[]
unigram=set()
crawl_words_sort=set()
s="tr"
file_path=data_folder+s+"_false.txt"
unigram_path=data_folder+s+"_unigram"
with open(unigram_path,'r',encoding='utf-8') as f_unigram:
    for lin in f_unigram:
        fileds=lin.strip().split('\t')
        if fileds[0].strip() not in unigram:
            unigram.add(fileds[0].strip())
with open(file_path,'r',encoding='utf-8') as f_in:
    with open(file_path.replace('.txt','.false'),'w',encoding='utf-8') as f_out:
        for line in f_in:
            fileds=line.split('\t')
            if fileds[0].strip() not in unigram:
                if fileds[0].strip().lower() not in unigram:
                    f_out.write(line.strip())
                    f_out.write('\n')
print("Finish Line")


