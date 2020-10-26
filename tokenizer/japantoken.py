import sys

import MeCab

"""
日语分词  带词性
"""
mecab = MeCab.Tagger("-Ochasen")
file = "/Users/ff/Desktop/jp_test_token.txt"
file_out = "/Users/ff/Desktop/jp_test_2.txt"


def format_tag_result(x):
    pieces = []
    for i in x.splitlines()[:-1]:  # 结尾的"EOS"顺手去掉
        i = i.split()
        pieces.append(str(i[0]) + "--" + i[-1])  # 选择需要的内容
    return pieces


# mecab_wrapper = JapaneseTokenizer.MecabWrapper(dictType='neologd')
with open(file, 'r', encoding='utf-8') as f_in:
    with open(file_out, 'w', encoding='utf-8') as f_out:
        for sentence in f_in:
            mecab.parse(sentence)
            pieces = format_tag_result(mecab.parse(sentence))

            f_out.write(" ".join(pieces).strip())
            f_out.write('\n')
