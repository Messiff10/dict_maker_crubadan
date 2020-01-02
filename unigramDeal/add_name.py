# file_path="/Users/ff/Desktop/第一优先级语言词表/desc/wy筛选词表"
import codecs
import os
import re
###  对筛选词表进行去重，去emoji 去格式不正确行 去前后空格
from utils.is_emoji import is_emoji

regex = re.compile('\s+')
regex1 = re.compile('')
unigram_path = '/Users/ff/Desktop/测评数据/补充人名地名/tr_unigram.txt'
name_path = '/Users/ff/Desktop/测评数据/补充人名地名/name1.tsv'
name_path2 = '/Users/ff/Desktop/测评数据/补充人名地名/name2.tsv'
unigram = {}
with open(unigram_path, 'r', encoding='utf-8') as f_unigram:
    for line in f_unigram:
        fileds = line.strip().split('\t')
        if fileds[0] not in unigram.keys():
            unigram[str(fileds[0]).strip()] = fileds[1].strip()
        else:
            unigram[str(fileds[0]).strip()] = int(unigram[str(fileds[0]).strip()]) + int(fileds[1].strip())
with open(name_path, 'r', encoding='utf-8') as f_name:
    for hline in f_name:
        words = hline.strip().split('\t')
        if words[0] not in unigram.keys():
            unigram[str(words[0]).strip()] = 1
with open(name_path2, 'r', encoding='utf-8') as f_name_2:
    for h2line in f_name_2:
        words2 = h2line.strip().split('\t')
        if words2[0].strip() not in unigram.keys():
            unigram[str(words[0]).strip()] = 1
with open(unigram_path.replace('.txt','_add.txt'),'w',encoding='utf-8') as f_out:

    for out in sorted(unigram.keys()):
        print(out,unigram[out])
        s=out.strip()+"\t"+str(unigram[out]).strip()
        f_out.write(s.strip())
        f_out.write('\n')


print("Finish line")
