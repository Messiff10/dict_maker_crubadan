import codecs
import os
import re

from utils.is_emoji import is_emoji
from utils.reExpression import replace_quotes, replace_clock_time, replace_brackets

##  一元词表与爬取语料比较

language = "ar"
unigram_path = '/Users/ff/Desktop/train_data/' + language + '/' + language + '_unigram'
file_path = '/Users/ff/Desktop/train_data/' + language + '/' + language + '_user_web_train/vocab_word_out'
file_path_true = file_path.replace('_out', '_out_true')
file_path_false = file_path.replace('_out', '_out_false')
# names = []
# for dir_path, subpaths, files in os.walk(data_folder):
#     for name in filter(lambda x: x.endswith('_tok.txt'), files):  # 文件夹下的所有文件
#         file_path = os.path.join(dir_path, name)
#         names.append(name)

# regex = re.compile('\s+')

# lists = [2, 3, 1, 3, 4, 4, 2, 1, 1]
#
# out = sorted(list(set(lists)), key=lists.index)


all_unigram_count = 0
all_crawl_count = 0
true_count = 0
false_count = 0
true_rate = 0.0
crawl_words = set()
unigram_words = set()
# false_words = set()
# true_words = set()
false_words = set()
true_words = set()
# 爬取词典数量
# Characters = re.compile(r"[q1w2e3éèêėëęēr4t5y6u7úùūûüi8ìíîįïīo9òóôöõœøōºp0aàáâäæãåāªsdfghjklzxcvbnm¹½⅓¼⅛²⅔³"
#                         r"¾⅜⁴⅝⅞ⁿ∅@#€₱$¢£¥%‰&_\-—–·+±(<{\[)\]}>*†‡★\"„“”«»'‚‘’‹›:;!¡?¿/,.…~`|•♣♠♪♥♦√πΠ÷×§¶∆≠="
#                         r"≈∞°′″↑↓→←^\\©®™℅≥≤\s]+")
regex = re.compile('\s+')

with codecs.open(file_path, encoding='utf-8') as f1:
    # with codecs.open(file_path.replace('_out', '_dict_uniq.txt'), 'w', encoding='utf-8') as f_uniq:
    for line in f1:
        # line = re.sub("\\[.*?]|\\{.*?}|\\(.*?\\)", " ", line)
        # words = regex.split(line)
        if str(line.strip()) is not "":
            # for w in words:
            # if str(w.strip()) is not "":
            if line.strip() not in crawl_words:
                all_crawl_count += 1
                crawl_words.add(line.strip())
                        # f_uniq.write(str(w).strip())
                        # f_uniq.write('\n')
# 一元词表
with codecs.open(unigram_path, encoding='utf-8') as f2:
    # with codecs.open(unigram_path.replace('_unigram', '_no_emoji_unigram'), 'w', encoding='utf-8') as f_no_emoji:
    for line in f2:
        fileds = line.strip().split('\t')
        if str(line.strip()) is not "":
            if len(fileds) == 2:
                if fileds[0] not in unigram_words:
                    all_unigram_count += 1
                    unigram_words.add(line.strip())
            else:
                if fileds[0] not in unigram_words:
                    all_unigram_count += 1
                    unigram_words.add(line.strip())
                        # f_no_emoji.write(line.strip())
                        # f_no_emoji.write('\n')
                    # if not re.match(Characters, fileds[0]) is None:
                    #     if fileds[0] not in unigram_words:
                    #         all_unigram_count += 1
                    #         unigram_words.add(line.strip())
                    #         f_no_emoji.write(line.strip())
                    #         f_no_emoji.write('\n')
for word in unigram_words:
    fileds = word.strip().split('\t')
    if len(fileds) == 2:
        if fileds[0] in crawl_words:
            true_count += 1
            # print(fileds[0],fileds[1])
            true_words.add((fileds[0], fileds[1]))
        else:
            false_count += 1
            false_words.add((fileds[0], fileds[1]))
    else:
        if fileds[0] in crawl_words:
            print("fileds!=2",word)
            true_count += 1
            true_words.add(fileds[0])
        else:
            print("fileds!=2 fales",word)
            false_count += 1
            false_words.add(fileds[0])
if os.path.exists(file_path_true):
    print("remove", file_path_true)
    os.remove(file_path_true)
if os.path.exists(file_path_false):
    print("remove", file_path_false)
    os.remove(file_path_false)

#### unigram有词频时
with codecs.open(file_path_true, 'w', encoding='utf-8') as f_true:
    # sorted(true_words)

    for t in sorted(true_words, key=lambda x: int(x[1]), reverse=True):
        s1 = t[0]
        # print(int(tuple(t)))
        # s1 = "\t".join(tuple(t))
        f_true.write(s1)
        f_true.write('\n')
with codecs.open(file_path_false, 'w', encoding='utf-8') as f_false:
    for f in sorted(false_words, key=lambda x: int(x[1]), reverse=True):
        # print(f)
        s2 = f[0]
        # s2 = "\t".join(tuple(f))
        f_false.write(s2)
        f_false.write('\n')
#### unigram没有词频时
# with codecs.open(file_path_true, 'w', encoding='utf-8') as f_true:
#     # sorted(true_words)
#     for t in true_words:
#         # s1 = t[0]
#         f_true.write(t)
#         f_true.write('\n')
# with codecs.open(file_path_false, 'w', encoding='utf-8') as f_false:
#     for f in false_words:
#         # print(f)
#         # s2 = f[0]
#         f_false.write(f)
#         f_false.write('\n')

print(str(all_crawl_count) + "\t" + str(all_unigram_count)
      + "\t正确数" + str(true_count) + "\t" + str(false_count) + "\t" + str(float(true_count / all_unigram_count)))
print("Finished!")
