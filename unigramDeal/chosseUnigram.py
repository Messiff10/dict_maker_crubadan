import codecs
import os
import re
#### 将所有词表与已筛选过词表分开
data_folder = '/Users/ff/Desktop/第一优先级语言词表/词表对照'
names = []

# string="hh hh ?? ?! ????AAA    ?  ?  A ??"
# ss=re.findall(regex,string)
# for s in ss:
#     string=string.replace(re.sub('\s+',string),'')
# print(string)
language = "pl"
unigram_path = '/Users/ff/Desktop/测评数据/'+language+'_unigram'
file_path = '/Users/ff/Desktop/测评数据/'+language+'_unigram.txt'
file_path_true = file_path.replace('_unigram.txt', '_unigram_have.txt')
file_path_false = file_path.replace('_unigram.txt', '_unigram_none.txt')

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
# regex2 = re.compile(',')
with codecs.open(file_path, encoding='utf-8') as f1:  #筛选过
    # with codecs.open(file_path.replace('_out', '_dict_uniq.txt'), 'w', encoding='utf-8') as f_uniq:
    for line in f1:
        if str(line.strip()) is not "":
            words=line.strip().split('\t')
            if words[0].strip() not in crawl_words:
                all_crawl_count += 1
                crawl_words.add(words[0].strip())
# 一元词表
with codecs.open(unigram_path, encoding='utf-8') as f2:  # 在unigram
    # with codecs.open(unigram_path.replace('_unigram', '_no_emoji_unigram'), 'w', encoding='utf-8') as f_no_emoji:
    for line in f2:
        fileds = line.strip().split('\t')
        if str(line.strip()) is not "":
            if len(fileds) == 2:
                if fileds[0].strip() not in unigram_words:
                    all_unigram_count += 1
                    unigram_words.add(line)
            else:
                if fileds[0].strip() not in unigram_words:
                    all_unigram_count += 1
                    unigram_words.add(line)
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
    # print()
    for t in sorted(true_words, key=lambda x: int(x[1]), reverse=True):
        # s1 = t[0]
        # print(int(tuple(t)))
        s1 = "\t".join(tuple(t))
        # print(s1)
        f_true.write(s1)
        f_true.write('\n')
with codecs.open(file_path_false, 'w', encoding='utf-8') as f_false:
    for f in sorted(false_words, key=lambda x: int(x[1]), reverse=True):
        # print(f)
        # s2 = f[0]
        s2 = "\t".join(tuple(f))
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
