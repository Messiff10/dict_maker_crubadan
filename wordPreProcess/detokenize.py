import codecs
import os
import re

from utils.reExpression import replace_quotes, replace_clock_time, replace_brackets
regex = re.compile(
    '[\])>}{\[<(±+_\-—–·&‰%¢$£¥₱€#@†*‡★؟„\"”“«»‚‹›\:;¡!¿?/,….~`|♪•♣♠♥♦√πΠ÷×§¶∆≠=≈∞′°″↑^←↓→\\©®™℅]')  # ar
regex2 = re.compile('\s+')
names=[]
# data_folder = '/Users/ff/Desktop/data/word/runword/notAddNoise/scenes/1/'
data_folder='/Users/ff/Desktop/data/word/runword/notAddNoise/scenes/1'
for dir_path, subpaths, files in os.walk(data_folder):
    for name in filter(lambda x: x.endswith('.txt'), files):  # 文件夹下的所有文件
        file_path = os.path.join(dir_path, name)
        names.append(name)
for name in names:
    file_path = os.path.join(data_folder, name)
    print(file_path)

    if os.path.exists(file_path.replace('_tok.txt', '.txt')):
        print("remove:", file_path.replace('_tok.txt', '.txt'))
        os.remove(file_path.replace('_tok.txt', '.txt'))
    with open(file_path, 'r', encoding='utf-8') as f_in:
        with open(file_path.replace('_tok.txt', '.txt'), 'w', encoding='utf-8') as f_out:
            for line in f_in:
                line = line.strip()
                line = replace_brackets(line)
                line = replace_clock_time(line)
                line = replace_quotes(line)
                # print(line)

                # line.replace()
                # words=re.find(regex,line)
                words = re.findall(regex, line)
                for w in words:
                    # line=line.replace(' ','')
                    # 先去空格
                    # line = line.replace(' '+w , w)
                    line = line.replace(' ' + w + ' ', w)
                    line = line.replace('  ' + w + '  ', w)
                    line = line.replace('   ' + w + '   ', w)
                    line = line.replace('\t' + w + '\t', w)
                    line = line.replace(' '+w , w)
                    line = line.replace(w+' ' , w)
                    # line = line.replace('  ', '')
                    # 加空格
                    line = line.replace(w, ' ' + w + ' ')  # 加空格
                    line = re.sub('\s+', ' ', line)
                # print(line)
                f_out.write(line.strip())
                f_out.write('\n')
print("Finsh line")