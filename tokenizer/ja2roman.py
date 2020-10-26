import re
import sys

# from pykakasi import kakasi, wakati
from pykakasi import kakasi, wakati

"""
日语转罗马音
"""

## 分词
import MeCab
#
mecab = MeCab.Tagger("-Owakati")
file = "/Users/ff/Desktop/jp_test_token.txt"
file_out = "/Users/ff/Desktop/jp_test_2.txt"
file_out_to = "/Users/ff/Desktop/jp_ori_token_roman.txt"
with open(file, 'r', encoding='utf-8') as f_in:
    with open(file_out, 'w', encoding='utf-8') as f_out:
        for sentence in f_in:
            mecab.parse(sentence)
            result=sentence.strip()+'\t'+str(mecab.parse(sentence)).strip()
            # print(mecab.parse(sentence))
            f_out.write(result.strip())
            f_out.write('\n')
print("Finish line")


## 罗马音转换
kakasi = kakasi()



kakasi.setMode("H", "a")  # Hiragana to ascii, default: no conversion
kakasi.setMode("J", "a")
kakasi.setMode("K", "a")  # Katakana to ascii, default: no conversion
# #

f_out = open(file_out_to, 'w', encoding='utf-8')
for l in open(file_out, 'r', encoding='utf-8'):
    ori, token = l.strip().split('\t')
    result_line = []
    result_line.append(ori)
    result_line.append(token)
    conv = kakasi.getConverter()
    result = conv.do(token)
    result_line.append(result)
    ll = "\n".join(result_line)
    f_out.write(ll)
    f_out.write('\n\n')