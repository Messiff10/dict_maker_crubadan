import re
import sys

import thulac
import pypinyin


def token(s):
    thu1 = thulac.thulac(seg_only=True)  # 默认模式
    text = thu1.cut(s, text=True)  # 进行一句话分词
    pinyins = pinyin(text)
    result = pinyins + '|#|' + re.sub('\s+', '\t', text)
    print(result)
    return result


# 不带声调的(style=pypinyin.NORMAL)
def pinyin(word):
    s = ''
    for i in pypinyin.pinyin(word, style=pypinyin.NORMAL):
        s += ''.join(i)
    s = re.sub('\s+', '\t', s)
    s = re.sub('\s*\t\s*', '\t', ' '.join(s))
    return s


if __name__ == '__main__':
    file = sys.argv[1]
    file_out = sys.argv[2]
    with open(file, 'r', encoding='utf-8') as f_in:
        with open(file_out, 'w', encoding='utf-8') as f_out:
            for l in f_in:
                l = re.sub('【(\w+)】', '', l.strip())
                l = re.sub('#(\w+)#', '', l.strip())
                l = re.sub('\(完\)', '', l.strip())
                l = l.strip()
                if len(l) > 2:
                    test = token(l)
                    f_out.write(test.strip())
                    f_out.write('\n')
    print("finish line")
