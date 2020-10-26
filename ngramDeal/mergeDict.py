import random
import re
import sys

"""
将没有词频的大词表加入到有词频的大词表中，词频按照是否在测试语料中决定
"""
file = "/Users/ff/Desktop/data/dict/input/ur/ur_huawei"
vocab_data_nofreq = "/Users/ff/Desktop/data/dict/input/ur/ur_unigram"
vocab_data = "/Users/ff/Desktop/data/dict/input/ur/ur_unigram.txt"
vocab_data_out = "/Users/ff/Desktop/data/dict/input/ur/ur_unigram_out"
regex = re.compile('\|#\|')
regex_vocab = re.compile('##')
vocab_set = set()
vocab_dict = {}
count = 0
true_count = 0
# num = sys.argv[3]
# line_num=sys.argv[4]
line_count = 0

with open(vocab_data, 'r', encoding='utf-8') as f_vocab:
    for vocab in f_vocab:
        words = vocab.strip().split('\t')
        # words = regex_vocab.split(vocab.strip())[0]
        if words[0] not in vocab_dict.keys():
            vocab_dict[words[0]] = words[1]
        # elif  words not in vocab_set and random.randint(10)>5:
    print("vocab size", len(vocab_dict))
with open(vocab_data_nofreq, 'r', encoding='utf-8') as f_vocab:
    for vocab in f_vocab:
        words = vocab.strip().split('\t')[0]
        # words = regex_vocab.split(vocab.strip())[0]
        if words not in vocab_set and words not in vocab_dict.keys():
            vocab_set.add(words)
        # elif  words not in vocab_set and random.randint(10)>5:
    print("vocab_nofreq size", len(vocab_set))
with open(file, 'r', encoding='utf-8') as f_in:
    for l in f_in:
        # line_count+=1
        # if line_count < int(line_num):
        words = regex.split(l.strip())[1].split('\t')
        for w in words:
            # count += 1
            if w in vocab_set:
                vocab_dict[w] = 100
                # else:
        #     break
    # print("vocab_nofreq size", len(vocab_dict))
for vs in vocab_set:
    if vs not in vocab_dict.keys():
        vocab_dict[vs] = 1
with open(vocab_data_out, 'w', encoding='utf-8') as f_out:
    for l in sorted(vocab_dict.items(),key=lambda x:-int(x[1])):
        f_out.write(l[0]+"\t"+str(l[1]))
        f_out.write('\n')
    # print("all count\t" + str(count) + "\ttrue count\t" + str(true_count) + "\ttrue rate\t" + str(
    #     float(true_count / count)))
