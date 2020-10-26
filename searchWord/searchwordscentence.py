"""
查找某个文件包含某个词的句子
"""
import os
import re

# data_folder = '/Users/ff/Desktop/测评数据/查找句子'
import sys

names = []
vocab_set = set()
regex = re.compile('\s+')
file_path = sys.argv[1]
vocab_file = sys.argv[2]
file_out = sys.argv[3]
count = {}
regex2=re.compile('\|#\|')
wordset=set()

# file_path = "/Users/ff/Desktop/test.txt"
def searchSen(file_path, file_out):
    file_out = open(file_out, 'w')
    with open(file_path, 'r', encoding='utf-8') as f_in:
        for line in f_in:
            words = regex2.split(line)[1]
            words = " " + re.sub('\t',' ',words.strip()) + " "
            for se in vocab_set:
                if se in words:
                    if se.strip() in count.keys():
                        if int(count[se.strip()])<1000 and line.strip() not in wordset:
                            wordset.add(line.strip())
                            count[se.strip()] = count[se.strip()] + 1
                            wordset.add(line.strip())
                            file_out.write(line.strip())
                            file_out.write('\n')
                            break
                        else:
                            break
                    else:
                        if line.strip() not in wordset:
                            count[se.strip()] = 1
                            wordset.add(line.strip())
                            file_out.write(line.strip())
                            file_out.write('\n')
                            break
                        else:
                            break
                        # if int(count[se.strip()]) > 1000:
                        #     break
    print(count)

    print("Finish Line")


def getvocab(vocab_file):
    with open(vocab_file, 'r', encoding='utf-8') as f_in:
        for l in f_in:
            words = l.split('\t')[0]
            vocab_set.add(" " + words.strip() + " ")
    # print("111")
    # print(vocab_set,len(vocab_set))


if __name__ == '__main__':
    getvocab(vocab_file)
    searchSen(file_path, file_out)
