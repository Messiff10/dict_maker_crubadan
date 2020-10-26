import os
import re
"""
将emoji词典中的大写字母转换为小写，并去重
"""
# from utils.reExpression import replace_brackets, replace_clock_time, replace_quotes
import sys

language = ["de","en","es","fil","hi_HINGLISH","in","jv","ms_MY","su","vi"]
for l in language:
    data_folder = '/Users/ff/Desktop/data/dict/input/' + l
    names = []

    # file_path="/Users/ff/Desktop/测评数据/去重/hi_bhaskar_0000.txt"
    for dir_path, subpaths, files in os.walk(data_folder):
        for name in filter(lambda x: x.endswith('.txt'), files):  # 文件夹下的所有文件
            file_path = os.path.join(dir_path, name)
            names.append(name)
    for name in names:
        file_path = os.path.join(data_folder, name)
        print(file_path)

        if os.path.exists(file_path.replace('.txt', '.change')):
            print("remove:", file_path.replace('.txt', '.change'))
            os.remove(file_path.replace('.txt', '.change'))
        centence = set()
        with open(file_path, 'r', encoding='utf-8') as f_in:
            with open(file_path.replace('.txt', '.change'), 'w', encoding='utf-8') as f_out:
                for line in f_in:
                    # lines=line.strip().split('\t')
                    line = line.strip().lower()
                    if line.strip() not in centence:
                        centence.add(line.strip())
                        f_out.write(line.strip())
                        f_out.write('\n')
    print("Finsh line")
