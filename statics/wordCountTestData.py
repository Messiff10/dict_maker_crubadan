import os
import re
"""
统计测评语料词数

"""
regex_pun = re.compile(
    '[\±+_·&‰%¢$£¥₱€#@†*‡★؟\‚\:;/,….~`|♪•♣♠♥♦√πΠ÷×§¶∆≠=≈∞°↑^←‚\:;?/,….~`|♪•♣♠♥♦√πΠ÷×§¶←↓→\\©®™℅,ـًٌٍَُِّْٰٖٕٓٔ¹½⅓¼⅛²⅔³¾⅜⅝⁴⅞@#¢₱€£¥%٪‰&_·+±\\﴾*★٭\‚‹:;؛∆≠=≈!∞°،↑)}\]’’>›»’↓→\±+_\·&‰٪%¢£¥₱€#@†*‡★\©®™℅]')  # ar
regex = re.compile('\s+')
data_folder = "/Users/ff/Desktop/测评数据/统计测评语料词个数"
names = []
for dir_path, subpaths, files in os.walk(data_folder):
    for name in filter(lambda x: not x.endswith('.txt'), files):  # 文件夹下的所有文件
        file_path = os.path.join(dir_path, name)
        names.append(name)
for name in names:
    file_path = os.path.join(data_folder, name)
    print(file_path)

    # if os.path.exists(file_path.replace('.txt', '.distinct')):
    #     print("remove:", file_path.replace('.txt', '.distinct'))
    #     os.remove(file_path.replace('.txt', '.distinct'))
    centence = {}
    count = 0
    with open(file_path, 'r', encoding='utf-8') as f_in:
        for line in f_in:
            line = re.sub(regex_pun, ' ', line.strip())
            line = re.sub('\s+', ' ', line)
            if len(line.strip())>1:
                words = regex.split(line)
                for w in words:
                    # lines=line.strip().split('\t')
                    if w.strip() in centence.keys():
                        centence[w] = centence[w] + 1
                    else:
                        centence[w] = 1
    print("总词数", len(centence))
    with open(file_path.replace(name, name + '.txt'), 'w', encoding='utf-8') as f_out:
        for ce in sorted(centence.items(), key=lambda x: -int(x[1])):
            result = str(ce[0]) + "\t" + str(ce[1])
            f_out.write(result.strip())
            f_out.write('\n')
            # f_out.write('\n')

print("Finsh line")
