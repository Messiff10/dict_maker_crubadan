import random
import re
import sys

"""
统计词表覆盖率
python3 /data/zzf/on-line_data_process/dataDel/unkRate.py /data/zzf/language/test_data/roData_huawei /data/zzf/language/ro/train_data/ro_unigram 1 4 8 20000 false
相关脚本存在1569
"""


file = sys.argv[1]
vocab_data = sys.argv[2]
i = sys.argv[3]
j = sys.argv[4]
k = sys.argv[5]
# file = "/Users/ff/Desktop/测评数据/nomap/urData.proletter"
# vocab_data = "/Users/ff/Downloads/ur_unigram.txt"
# vocab_data_out = "/Users/ff/Desktop/测评数据/nomap/urData.false"
regex = re.compile('\|#\|')
regex_vocab = re.compile('##')
regex_space = re.compile('\\s+')
vocab_set = []
count = 0
true_count = 0
num = sys.argv[6]
outEither = sys.argv[7]
# line_num=sys.argv[4]
line_count = 0
false_dict = {}
with open(vocab_data, 'r', encoding='utf-8') as f_vocab:
    for vocab in f_vocab:
        if int(i) == 1:
            words = vocab.strip().split('\t')[0]
        else:
            words = regex_vocab.split(vocab.strip())[0]
        if int(j) == 3:
            if words not in vocab_set and len(vocab_set) < int(num):
                vocab_set.append(words.lower())
            elif len(vocab_set) >= int(num):
                break
        else:
            vocab_set.append(words.lower())
        # elif  words not in vocab_set and random.randint(10)>5:

    print("vocab size", len(vocab_set))

with open(file, 'r', encoding='utf-8') as f_in:
    for l in f_in:
        if int(k) == 8:
            words = regex.split(l.strip())[1].split('\t')
            count += len(words)
            for w in words:
                if w.lower() in vocab_set:
                    true_count += 1
                elif w in false_dict.keys():
                    false_dict[w] = false_dict[w] + 1
                else:
                    false_dict[w] = 1
        else:
            if not l.startswith("==="):
                words = l.strip().split(" ")
                count += len(words)
                for w in words:
                    if w.lower() in vocab_set:
                        true_count += 1
                    elif w in false_dict.keys():
                        false_dict[w] = false_dict[w] + 1
                    else:
                        false_dict[w] = 1
            else:
                continue
        # 去除首单词 不去除前后空格
        # l = re.sub("\\s+", " ", l)
        # words = regex_space.split(l.strip())
        # count += len(words) - 1  ##总数
        # if l.endswith(" "):
        #     for w in words:
        #         # count += 1
        #         if w.lower() in vocab_set:
        #             true_count += 1
        #         elif w in false_dict.keys():
        #             false_dict[w] = false_dict[w] + 1
        #         else:
        #             false_dict[w] = 1
        # else:
        #     for w in range(1, len(words)):
        #         if words[w].lower() in vocab_set:
        #             true_count += 1
        #         elif words[w] in false_dict.keys():
        #             false_dict[w] = false_dict[w] + 1
        #         else:
        #             false_dict[w] = 1
if outEither == "true":
    vocab_data_out = sys.argv[8]
    f_out = open(vocab_data_out, 'w', encoding='utf-8')
    for fa in sorted(false_dict.items(), key=lambda x: -int(x[1])):
        f_out.write(fa[0] + "\t" + str(fa[1]))
        f_out.write('\n')

print("all count\t" + str(count) + "\ttrue count\t" + str(true_count) + "\ttrue rate\t" + str(
    float(true_count / count)))
