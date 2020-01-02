import codecs
import os
import re

from utils.is_emoji import is_emoji
# from utils.reExpression import replace_quotes, replace_clock_time, replace_brackets

##  一元词表与爬取语料比较

language = "cs"
unigram_path = '/Users/ff/Desktop/第一优先级语言词表/desc/第一优先级词表所有降序/' + language + '_unigram'
file_path = '/Users/ff/Desktop/第一优先级语言词表/desc/dictionary_crawl/' + language + '_dict.txt'
file_path_true = '/Users/ff/Desktop/第一优先级语言词表/desc/dictionary_crawl/' + language + '_true_unigram.txt'
file_path_false = '/Users/ff/Desktop/第一优先级语言词表/desc/dictionary_crawl/' + language + '_false_unigram.txt'
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
    with codecs.open(file_path.replace('_dict.txt', '_dict_uniq.txt'), 'w', encoding='utf-8') as f_uniq:
        for line in f1:
            line = re.sub("\\[.*?]|\\{.*?}|\\(.*?\\)", " ", line)
            line=line.replace(':',' ').replace(',',' ').replace('/',' ').replace('\\',' ')\
                .replace('?',' ').replace(';',' ').replace('.',' ').replace('|',' ')\
                .replace('<',' ').replace('>','').replace('{',' ').replace('}',' ')\
                .replace('[',' ').replace(']',' ').replace('~',' ')
            words = regex.split(line)
            if str(line.strip()) is not "":
                for w in words:
                    if str(w.strip()) is not "":
                        if w.strip() not in crawl_words:
                            all_crawl_count += 1
                            crawl_words.add(w.strip())
                            f_uniq.write(str(w).strip())
                            f_uniq.write('\n')
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
for word in unigram_words:
    fileds = word.strip().split('\t')
    if len(fileds) == 2:
        if fileds[0] in crawl_words:
            true_count += 1
            true_words.add((fileds[0], fileds[1]))
        else:
            false_count += 1
            false_words.add((fileds[0], fileds[1]))
    else:
        if fileds[0] in crawl_words:
            print(fileds[0])
            true_count += 1
            true_words.add(fileds[0])
        else:
            print(fileds[0])
            false_count += 1
            false_words.add(fileds[0])
if os.path.exists(file_path_true):
    print("remove", file_path_true)
    os.remove(file_path_true)
if os.path.exists(file_path_false):
    print("remove", file_path_false)
    os.remove(file_path_false)
with codecs.open(file_path_true, 'w', encoding='utf-8') as f_true:
    # sorted(true_words)
    for t in sorted(true_words, key=lambda x: int(x[1]), reverse=True):
        s1 = "\t".join(tuple(t))
        f_true.write(s1)
        f_true.write('\n')
with codecs.open(file_path_false, 'w', encoding='utf-8') as f_false:
    for f in sorted(false_words, key=lambda x: int(x[1]), reverse=True):
        # print(f)
        s2 = "\t".join(tuple(f))
        f_false.write(s2)
        f_false.write('\n')

print(str(all_crawl_count) + "\t" + str(all_unigram_count)
      + "\t" + str(true_count) + "\t" + str(false_count) + "\t" + str(float(true_count / all_unigram_count)))
print("Finished!")
