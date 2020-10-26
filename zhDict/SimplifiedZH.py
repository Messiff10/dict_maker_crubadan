import os

import pypinyin
from pypinyin import lazy_pinyin

from opencc import OpenCC


# 不带声调的(style=pypinyin.NORMAL)
def pinyin(word):
    s = ''
    for i in pypinyin.pinyin(word, style=pypinyin.NORMAL):
        s += ' '.join(i)+" "
    return s


# 带声调的(默认)
def yinjie(word):
    # pinyin = lazy_pinyin(word,)
    # print(pinyin)
    s = ''
    # heteronym=True开启多音字
    # pinyin=pypinyin.pinyin(word, heteronym=True)
    # print(pinyin)
    for i in pypinyin.pinyin(word, heteronym=True):
        s = s + ''.join(i) + " "
    return s


def getShortWord(line):
    oc = OpenCC(conversion='s2twp')  # "出租车" --> "計程車" 带短语

    word_shortcut = []
    items = line.strip().split(" ")
    jianti = items[0].strip()
    fanti = oc.convert(jianti)
    print(jianti, fanti)
    return word_shortcut


if __name__ == "__main__":
    print(getShortWord("出租车"))
    print(pinyin("会计"))
    print(yinjie("会计"))
