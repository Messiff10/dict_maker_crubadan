import os
import re

# from utils.reExpression import replace_brackets, replace_clock_time, replace_quotes
import sys

data_folder = '/Users/ff/Desktop/测评数据/去重/'
names = []

# string="hh hh ?? ?! ????AAA    ?  ?  A ??"
# ss=re.findall(regex,string)
# for s in ss:
#     string=string.replace(re.sub('\s+',string),'')
# print(string)
# s='\\])>}{\[<(±+_\-—–·&‰%¢$£¥₱€#@†*‡★؟„\"”“«»‚‹›\:;¡!¿?/,….~`|♪•♣♠♥♦√πΠ÷×§¶∆≠=≈∞′°″↑^←«»‚‹›\:;¡!¿?/,….~`|♪•♣♠♥♦√πΠ÷×§¶←↓→\\©®™℅,ـًٌٍَُِّْٰٖٕٓٔ¹½⅓¼⅛²⅔³¾⅜⅝⁴⅞@#¢₱€£¥%٪‰&_\-—–·+±\)}>﴿\({<﴾*★٭"„“”»«\‚‘’›‹:;؛¡!?؟∆≠=≈∞′°″،↑↓→\\\[\]\)>}{\[<\(±+_\-—–·&‰٪%¢£¥₱€#@†*‡★؟„\"”“©®™℅\'
centence=set()
# file_path=sys.argv[1]
for dir_path, subpaths, files in os.walk(data_folder):
    for name in filter(lambda x: x.endswith('.txt'), files):  # 文件夹下的所有文件
        file_path = os.path.join(dir_path, name)
        names.append(name)
for name in names:
    file_path = os.path.join(data_folder, name)
    print(file_path)

    # if os.path.exists(file_path.replace('.txt', '.space')):
    #     print("remove:", file_path.replace('.txt', '.space'))
    #     os.remove(file_path.replace('.txt', '.space'))
    with open(file_path, 'r', encoding='utf-8') as f_in:
        with open(file_path.replace('.txt', '.distinct'), 'w', encoding='utf-8') as f_out:
            for line in f_in:
                if line.strip() not in centence:
                    centence.add(line.strip())
                    f_out.write(line.strip())
                    f_out.write('\n')
print("Finsh line")
# print(line)
