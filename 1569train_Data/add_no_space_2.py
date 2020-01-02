import codecs
import os
import re
import sys

import emoji


def is_emoji(content):
    if re.match(emoji.get_emoji_regexp(), content):
        return True
    return False


regex = re.compile(
    '[\])>}{\[<(±+_\-—–·&‰%¢$£¥₱€#@†*‡★؟„\"”“«»‚‹›\:;¡!¿?/,….~`|♪•♣♠♥♦√πΠ÷×§¶∆≠=≈∞′°″↑^←«»‚‹›\:;¡!¿?/,….~`|♪•♣♠♥♦√πΠ÷×§¶←↓→\\©®™℅,ـًٌٍَُِّْٰٖٕٓٔ¹½⅓¼⅛²⅔³¾⅜⅝⁴⅞@#¢₱€£¥%٪‰&_\-—–·+±\)}>﴿\({<﴾*★٭"„“”»«\‚‘’›‹:;؛¡!?؟∆≠=≈∞′°″،↑↓→\\\[\]\)>}{\[<\(±+_\-—–·&‰٪%¢£¥₱€#@†*‡★؟„\"”“©®™℅]')  # ar
# regex = re.compile(
#     '\[\]\)>}{\[<\(±+_\-—–·&‰٪%¢£¥₱€#@†*‡★؟„\"”“'
#     '«»‚‹›\:;¡!¿?/,….~`|♪•♣♠♥♦√πΠ÷×§¶∆≠=≈∞′°″،↑]'
#     '\\[←↓→\\©®™℅,ـًٌٍَُِّْٰٖٕٓٔ¹½⅓¼⅛²⅔³¾⅜⅝⁴⅞@#¢₱€£¥%٪‰&_\-—–·+±\)}>﴿\({<﴾*★٭"„“”»«\‚‘’›‹:;؛¡!?؟')

# regex2 = re.compile('\s+')
# regex3 = re.compile('')
file_path = sys.argv[1]
# names = []
#
# string = "hh hh ?? ?! ????AA؛A  ؟  ?  ?  A ??"
# ss = re.findall(regex, string)
# for s in ss:
#     print(s)
#     string = string.replace(' ' + s + ' ', s)
#     string=string.replace(s,' '+s+' ')
# print(string)

# for dir_path, subpaths, files in os.walk(data_folder):
#     for name in filter(lambda x: x.endswith('.txt'), files):  # 文件夹下的所有文件
#         file_path = os.path.join(dir_path, name)
#         names.append(name)
# file_path = os.path.join(data_folder, name)
print(file_path)

if os.path.exists(file_path.replace('.txt', '.space')):
    print("remove:", file_path.replace('.txt', '.space'))
    os.remove(file_path.replace('.txt', '.space'))
with open(file_path, 'r', encoding='utf-8') as f_in:
    with open(file_path.replace('.txt', '.space'), 'w', encoding='utf-8') as f_out:
        for line in f_in:
            # print(line)

            # line.replace()
            # words=re.find(regex,line)
            # allwords = regex3.split(line)
            alist = [ch for ch in line]
            for allw in alist:
                if is_emoji(allw):
                    line = line.replace(allw, ' ' + allw + ' ')
                    line = re.sub('\s+', ' ', line)
            words = re.findall(regex, line)
            for w in words:
                # line=line.replace(' ','')
                # 先去空格
                # line = line.replace(' '+w , w)
                line = re.sub('\s+', ' ', line)
                line = line.replace(' ' + w + ' ', w)
                line = line.replace(' ' + w, w)
                line = line.replace(w + ' ', w)
                # line = line.replace('  ', '')
                # 加空格
                line = line.replace(w, ' ' + w + ' ')  # 加空格
                line = line.replace(' \' ', '\'')
            line = re.sub('\s+', ' ', line)
            # print(line)
            f_out.write(line.strip())
            f_out.write('\n')
print("Finsh line")
# print(line)
