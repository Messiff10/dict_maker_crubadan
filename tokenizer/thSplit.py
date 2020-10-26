import codecs
import os
import re

from utils.reExpression import replace_quotes, replace_clock_time, replace_brackets

"""
th新闻分词  每三个词分一行
分词器前步骤
"""

language = "th"
unigram_path = '/Users/ff/Desktop/train_data/th/th_web.txt'
file_path = '/Users/ff/Desktop/train_data/th/th_web_split.txt'

# 爬取词典数量
regex = re.compile('\s+')
with codecs.open(unigram_path, 'r', encoding='utf-8') as f:
    with codecs.open(file_path, 'w', encoding='utf-8') as f1:
        for line in f:
            t = ''
            s = ''
            fileds = regex.split(line)
            for i in range(int(len(fileds) / 3) + 1):
                t = fileds[3 * i:3 * (i + 1)]
                s = " ".join(t)
                if str(s.strip()) is not "":
                    f1.write(str(s))
                    f1.write('\n')
# line:เมื่อวันที่ 8 ตุลาคม


# 一元词表

# ll = set()
# for i in range(0, 10):
#     # list.insert(i)
#     ll.add(i)
# for l in ll:
#     print(str(l) + "\n")
