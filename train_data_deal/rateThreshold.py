import re
# import sys
import sys

"""
尽量多保留达到过筛滤的语句 如果一句话整句没有达到 那么按照10个词递进 将满足过筛滤的语句保留
目前不用 该操作添加在在最终生成训练数据的java代码中
"""

sys.setrecursionlimit(1000000)

unigram_true = "/Users/ff/Desktop/train_data/en_US/en_US_user_web_train/vocab_words_true"
unigram_true_2w = []
wordsnum = 20000
rateThreshold = 0.8
file = "/Users/ff/Desktop/train_data/en_US/en_US_user_web_no_emoji_case.txt"
file_out = "/Users/ff/Desktop/train_data/en_US/en_US_user_split.txt"
regex = re.compile('\s+')


def chooseline(items, f_out):
    known = 0
    unknown = 0

    for item in items:
        if " " + item + " " in unigram_true_2w:
            known += 1
        else:
            unknown += 1
    if float(int(known) / (int(known) + int(unknown))) >= rateThreshold:  # 整句话达到过筛则保留
        f_out.write(" ".join(items).strip())
        f_out.write('\n')
    else:
        for i in range(0, len(items)):
            if i + 10 <= len(items):  # 剩余词不足10个
                # chooseline(items[i:i + 10],f_out)
                for ite in items[i:i + 10]:
                    if ' ' + ite + ' ' in unigram_true_2w:
                        known += 1
                    else:
                        unknown += 1
                if float(int(known) / (int(known) + int(unknown))) >= rateThreshold:  # 整句话达到过筛则保留
                    f_out.write(" ".join(items[i:i + 10]).strip())
                    f_out.write('\n')
                    break
                else:
                    continue
            else:
                break


def getsentence(file):
    with open(file, 'r', encoding='utf-8') as f_sentence:
        with open(file_out, 'w', encoding='utf-8') as f_out:
            for line in f_sentence:
                if " " in line.strip():  # 至少有两个单词
                    line = " " + re.sub('\s+', " ", line.strip()) + " "
                    for unigram in unigram_true_2w:
                        if unigram in line:  # 先判断是否包含2w词
                            lineresult = line.strip()
                            break
                        else:
                            lineresult = ""
                    if lineresult is not "":  # 包含则去比较过筛
                        items = regex.split(line.strip())
                        chooseline(items, f_out)
                else:
                    continue


def getunigram(unigram_true):
    with open(unigram_true, 'r', encoding='utf-8') as f_unigram:
        for line in f_unigram:
            if len(unigram_true_2w) < wordsnum:
                unigram_true_2w.append(" " + line.strip() + " ")


if __name__ == '__main__':
    # 获取比较为true的前两万词
    getunigram(unigram_true)

    # 读取语句
    getsentence(file)
