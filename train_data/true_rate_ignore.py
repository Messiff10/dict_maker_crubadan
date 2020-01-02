#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re

from utils.reExpression import replace_quotes_1, replace_brackets_1, replace_brackets_2 \
    , replace_brackets_3, replace_brackets_4, replace_brackets_5, replace_brackets_6, replace_brackets_7 \
    , replace_brackets_8, replace_brackets_9, replace_clock_time, replace_brackets_1, replace_quotes_2, \
    replace_quotes_3, replace_brackets_10

regex4 = re.compile(
    '[\±+_\-—–·&‰%¢$£¥₱€#@†*‡★؟\‚\:;¿?/,….~`|♪•♣♠♥♦√πΠ÷×§¶∆≠=≈∞°↑^←‚\:;¿?/,….~`|♪•♣♠♥♦√πΠ÷×§¶←↓→\\©®™℅,ـًٌٍَُِّْٰٖٕٓٔ¹½⅓¼⅛²⅔³¾⅜⅝⁴⅞@#¢₱€£¥%٪‰&_\-—–·+±\\﴾*★٭\‚›‹:;؛?؟∆≠=≈!∞°،↑)}\]’’>›»”’↓→\±+_\-—–·&‰٪%¢£¥₱€#@†*‡★؟„\©®™℅]')  # ar

regex = re.compile('\\|#\\|')
regex2 = re.compile('\s+')
regex3 = re.compile('##')
total_vocab = set()
total_unigrams = set()


def goodpercentofdata(data):
    total = 0
    i = 0
    j = 0
    with open(data, 'r', encoding='utf-8') as f_in:
        for lin in f_in:
            fileds = regex.split(lin)
            line = fileds[1].strip()
            # print(line)
            # line = re.sub('\s+', ' ', line)
            # line = replace_brackets_1(line)
            # line = replace_brackets_9(line)
            # line = replace_brackets_8(line)
            # line = replace_brackets_7(line)
            # line = replace_brackets_6(line)
            # line = replace_brackets_5(line)
            # line = replace_brackets_4(line)
            # line = replace_brackets_3(line)
            # line = replace_brackets_2(line)
            # line = replace_brackets_10(line)
            # line = replace_quotes_2(line)
            # line = replace_quotes_3(line)
            # line = replace_clock_time(line)
            # line = replace_quotes_1(line)
            # print(line)

            # line.replace()
            # words=re.find(regex,line)
            # words = re.findall(regex4, line)
            # for w in words:
            #     # line=line.replace(' ','')
            #     # 先去空格
            #     line = re.sub('\s+', ' ', line)
            #     line = line.replace(' ' + w, w)

            words = line.strip().split('\t')
            for w in words:
                total += 1
                if w.strip().lower() in total_vocab:
                    i += 1
                if w.strip().lower() in total_unigrams:
                    j += 1
                    # print("w", w.strip())187744 在2w词表中数： 134794

    print("训练测试集总词数：", total, "在2w词表中数：", i, "正确率：", float(i / total))
    print("训练测试集总词数：", total, "在大词表中数：", j, "正确率：", float(j / total))


def goodpercentofsentense(data, s):
    names = []
    for dir_path, subpaths, files in os.walk(data):
        for name in filter(lambda x: x.endswith('.txt'), files):  # 文件夹下的所有文件
            file_path = os.path.join(dir_path, name)
            names.append(name)

    total_facebook = 0
    total_data=0
    total_facebook_huawei=0
    total_im=0
    total_twitter=0
    total_web=0
    i_data = 0
    j_data = 0
    i_facebook = 0
    j_facebook = 0
    i_im = 0
    j_im = 0
    i_facebook_huawei = 0
    j_facebook_huawei = 0
    i_web = 0
    j_web = 0
    i_twitter = 0
    j_twitter = 0
    for name in names:
        file_path = os.path.join(data, name)
        # print(file_path)

        with open(file_path, 'r', encoding='utf-8') as f_in:
            print(file_path)
            if file_path.endswith('_data.txt'):
                for line in f_in:
                    fileds = regex2.split(line)
                    for f in fileds:
                        total_data += 1
                        if f.lower() in total_vocab:
                            i_data += 1
                        if f.lower() in total_unigrams:
                            j_data += 1
            if file_path.endswith('_facebook.txt'):
                for line in f_in:
                    fileds = regex2.split(line)
                    for f in fileds:
                        total_facebook += 1
                        if f.lower() in total_vocab:
                            i_facebook += 1
                        if f.lower() in total_unigrams:
                            j_facebook += 1
            if file_path.endswith('_im.txt'):
                for line in f_in:
                    fileds = regex2.split(line)
                    for f in fileds:
                        total_im += 1
                        if f.lower() in total_vocab:
                            i_im += 1
                        if f.lower() in total_unigrams:
                            j_im += 1
            if file_path.endswith('-facebook.txt'):
                for line in f_in:
                    fileds = regex2.split(line)
                    for f in fileds:
                        total_facebook_huawei += 1
                        if f.lower() in total_vocab:
                            i_facebook_huawei += 1
                        if f.lower() in total_unigrams:
                            j_facebook_huawei += 1
            if file_path.endswith('-web.txt'):
                for line in f_in:
                    fileds = regex2.split(line)
                    for f in fileds:
                        total_web += 1
                        if f.lower() in total_vocab:
                            i_web += 1
                        if f.lower() in total_unigrams:
                            j_web += 1
            if file_path.endswith('-twitter.txt'):
                for line in f_in:
                    fileds = regex2.split(line)
                    for f in fileds:
                        total_twitter += 1
                        if f.lower() in total_vocab:
                            i_twitter += 1
                        if f.lower() in total_unigrams:
                            j_twitter += 1

    print("2w词表", str(float(i_facebook_huawei / total_facebook_huawei)) + "\t" + str(float(i_facebook / total_facebook)) + '\t'
          + str(float(i_im / total_im)) + '\t' + str(float(i_twitter / total_twitter)) + '\t' + str(float(i_web / total_web))+'\t'+str(float(i_data/ total_data)))
    print("大词表", str(float(j_facebook_huawei / total_facebook_huawei)) + "\t" + str(float(j_facebook / total_facebook))
          + '\t' + str(float(j_im / total_im)) + '\t' + str(float(j_twitter / total_twitter)) + '\t' + str(float(j_web / total_web))+'\t'+str(float(j_data / total_data)))


def mathc(s):
    words = regex2.split(s.strip())
    for w in words:
        if w in total_vocab:
            print(w)
        else:
            print("error:", w)


def total_voacab_words(data):
    total = 0

    with open(data, 'r', encoding='utf-8') as f:
        for line in f:
            fileds = regex3.split(line)
            if fileds[0].strip() not in total_vocab:
                total += 1
                total_vocab.add(fileds[0])
    print("词表总数：", total)


def total_unigram(data):
    total_u = 0

    with open(data, 'r', encoding='utf-8') as f:
        for line in f:
            # fileds = regex3.split(line)
            fileds = line.strip().split('\t')
            if fileds[0].strip() not in total_unigrams:
                # print(fileds[0])
                total_u += 1
                total_unigrams.add(fileds[0].strip())
    print("一元词表总数：", total_u)

# 转换大小写
def main():
    s = "en_US"
    arpath = '/Users/ff/Desktop/train_data/' + s + '/' + s + '_user_web_train/train_data_en_US_user_web_no_emoji_develop/'
    ardevdata = arpath + 'dev_data'
    arvocabdata = arpath + 'vocab_in_words'
    ar_unigram = '/Users/ff/Desktop/train_data/' + s + '/' + s + '_unigram'
    arsendata = '/Users/ff/Desktop/train_data/' + s + '/测评语料/华为测评/'
    total_voacab_words(arvocabdata)
    total_unigram(ar_unigram)
    goodpercentofdata(ardevdata)
    goodpercentofsentense(arsendata, s)


if __name__ == "__main__":
    main()
