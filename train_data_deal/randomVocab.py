import re
import sys

import numpy


"""
随机抽样 保留比较为true的前num个词  其余根据是否存在测试语料决定
"""
true_vocab = sys.argv[1]
test_file = sys.argv[2]
file_out = sys.argv[3]

num = sys.argv[4]
allnum = sys.argv[5]
previous_vocab = []

other_freq = {}
otherFalse_freq = {}
regex = re.compile("\s+")
regex_test = re.compile('\|#\|')
test_freq = []


def getPrevious(num, file, freqNum):
    print("取前", num, "个数")
    with open(file, 'r', encoding='utf-8') as f_in:
        for _ in f_in:
            freqNum += 1
            words = _.split('\t')
            if len(words) == 2:
                word = words[0]
                freq = words[1]
                if len(previous_vocab) < int(num):
                    previous_vocab.append(word)
                else:
                    other_freq[word] = freq  # 不在1.5万的词放入词典
                    # allfreq += freq
            else:
                word = _.strip()
                if len(previous_vocab) < int(num):
                    previous_vocab.append(word)
                else:
                    other_freq[word] = 300000 - int(freqNum)  # 不在1.5万的词放入词典
                    # allfreq += freq
    print("提前取的数", len(previous_vocab))


def getTestVocab(test_file):
    with open(test_file, 'r', encoding='utf-8') as f_in:
        for _ in f_in:
            words = regex_test.split(_.strip())[1].split('\t')
            for w in words:
                test_freq.append(w.lower())
    print("test vocab", len(test_freq))


def getOtherVocab(allfreq):
    for _ in other_freq.keys():
        # print(_)
        if str(_).lower() in test_freq:
            # print(str(_))
            previous_vocab.append(str(_))
        else:
            otherFalse_freq[_] = other_freq[_]
            allfreq += int(other_freq[_])
    print("true", len(previous_vocab))
    return allfreq


numpy.random.seed(1)


def getRandom1(otherFalse_freq, allfreq):
    for _ in otherFalse_freq.keys():
        ran = numpy.random.randint(len(otherFalse_freq))
        # print(ran, allfreq, otherFalse_freq[_])
        otherFalse_freq[_] = pow(ran, 1 / float(int(allfreq) / int(otherFalse_freq[_])))
    for o in sorted(otherFalse_freq.items(), key=lambda x: -float(x[1])):
        if len(previous_vocab) < int(allnum):
            previous_vocab.append(o[0])
        else:
            break


def getRandom2(otherFalse_freq):
    for _ in sorted(otherFalse_freq.items(), key=lambda x: -int(x[1])):
        if len(previous_vocab) < int(allnum):
            previous_vocab.append(_[0])
        else:
            break


def writeVocab(file_out):
    f_out = open(file_out, 'w', encoding='utf-8')
    for _ in previous_vocab:
        f_out.write(str(_).strip())
        f_out.write('\n')


if __name__ == '__main__':
    allfreq = 0
    freqNum = 0
    getPrevious(num, true_vocab, freqNum)
    getTestVocab(test_file)
    allfreq = getOtherVocab(allfreq)
    if len(previous_vocab) < int(allnum):
        getRandom1(otherFalse_freq, allfreq)
        # getRandom2(otherFalse_freq)
    writeVocab(file_out)
    print("Finish line")
