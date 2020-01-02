import codecs
import re

import emoji

from utils.is_emoji import is_emoji


def is_emoji(content):
    if re.match(emoji.get_emoji_regexp(), content):
        return True
    return False


data_folder = "/Users/ff/Desktop/测评数据/文件对比"
file_path1 = data_folder + '/tr_unigram_30_sort'  # 少
file_path2 = data_folder + '/tr_unigram_web_20200102'  # 多
file_out_path1 = data_folder + '/vocab_in_new_not_in_old'  # 在新不在新
file_out_path2 = data_folder + '/vocab_in_old_not_in_new'  # 在新不在旧
file1 = {}
file2 = {}
regex = re.compile('##')
with codecs.open(file_path1, 'r', encoding='utf-8') as f:
    for line in f:
        words = line.strip().split('\t')
        if words[0].strip() not in file1.keys():
            # print(words[0].strip())
            file1[words[0]] = 1
            # file1.add((words[0],line))
            # file1[words[0]] = words[1]
with codecs.open(file_path2, 'r', encoding='utf-8') as f2:
    for line in f2:
        words = line.strip().split('\t')
        if words[0].strip() not in file2.keys():
            # print(words[0].strip())
            file2[words[0]] = 1
            # file2.add((words[0],line))
            # file2[words[0]] = words[1]
with open(file_out_path1, 'w', encoding='utf-8') as f_in_old:
    for w1 in file1.keys():
        if w1 not in file2.keys():
            # print(w1)
            # print(w1+"\t"+str(file1[w1]))
            f_in_old.write(w1.strip())
            f_in_old.write('\n')
with open(file_out_path2, 'w', encoding='utf-8') as f_in_new:
    for w1 in file2.keys():
        if w1 not in file1.keys():
            # print(w1)
            ww=w1+"\t"+str(1)
            f_in_new.write(ww.strip())
            f_in_new.write('\n')

print("Finished!")
