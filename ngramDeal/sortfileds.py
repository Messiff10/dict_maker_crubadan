import codecs
import os
import re

"""
按照指定字段排序
"""

# language = "fi"
# unigram_path = '/Users/ff/Desktop/train_data/' + language + '/' + language + '_unigram_null'
# file_path = '/Users/ff/Desktop/train_data/' + language + '/' + language + '_user_web_train/vocab_words'
# file_path_true = file_path.replace('_words', '_words_true')
# file_path_false = file_path.replace('_words', '_words_false')
import sys

#
data_folder = '/Users/ff/Desktop/测评数据/按照指定字段排序'
names = []
regex = re.compile('\s+')

for dir_path, subpaths, files in os.walk(data_folder):
    for name in filter(lambda x: x.endswith('.txt'), files):  # 文件夹下的所有文件
        file_path = os.path.join(dir_path, name)
        names.append(name)
for name in names:
    file_path = os.path.join(data_folder, name)
    print(file_path)
    crawl_words = set()
    crawl_words_sort = set()
    ##  一元词表
    with open(file_path, 'r', encoding='utf-8') as f_in:
        for line in f_in:
            if str(line.strip()) is not "":
                fileds = line.strip().split('\t')
                # bigram=fileds[0]+'\t'+fileds[1]
                if line not in crawl_words:
                    crawl_words.add(line)
                    # crawl_words_sort[fileds[0]]=line
                    crawl_words_sort.add((fileds[1], line))
    # 词表
    with codecs.open(file_path.replace('.txt', '_sort'), 'w', encoding='utf-8') as f_out:
        # with codecs.open(unigram_path.replace('_unigram', '_no_emoji_unigram'), 'w', encoding='utf-8') as f_no_emoji:

        for t in sorted(crawl_words_sort, key=lambda x: -int(x[0])):
            s1 = t[1]
            f_out.write(s1.strip())
            f_out.write('\n')

    ## 二元词表
    # with open(file_path,'r',encoding='utf-8') as f_in:
    #     for line in f_in:
    #         if str(line.strip()) is not "":
    #             fileds=line.split('\t')
    #             # bigram=fileds[0]+'\t'+fileds[1]
    #             # if fileds[0] not in crawl_words:
    #             # crawl_words.add(fileds[0])
    #             crawl_words_sort.add((fileds[0],fileds[2],line))
    # with codecs.open(file_path.replace('.txt','_sort'),'w', encoding='utf-8') as f_out:
    #     # with codecs.open(unigram_path.replace('_unigram', '_no_emoji_unigram'), 'w', encoding='utf-8') as f_no_emoji:
    #
    #     for t in sorted(crawl_words_sort,key=lambda x: (x[0], -int(x[1]))):
    #         s1 = t[2]
    #         # print(int(tuple(t)))
    #         # s1 = "\t".join(tuple(t))
    #         # print(s1)
    #         f_out.write(s1.strip())
    #         f_out.write('\n')
    print("Finished!")
