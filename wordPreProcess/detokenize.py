import codecs
import os
import re

from utils.reExpression import replace_quotes, replace_clock_time, replace_brackets

# data_folder = '/Users/ff/Desktop/data/word/runword/notAddNoise/scenes/1/'
data_folder='/Users/ff/Documents'
names = []
for dir_path, subpaths, files in os.walk(data_folder):
    for name in filter(lambda x: x.endswith('.txt'), files):  # 文件夹下的所有文件
        file_path = os.path.join(dir_path, name)
        names.append(name)

# regex = re.compile('\s+')
for name in names:
    file_path = os.path.join(data_folder, name)
    print(file_path)

    with codecs.open(file_path, encoding='utf-8') as f:
        with codecs.open(file_path.replace('.txt', '_detok.txt'), 'w', encoding='utf-8') as f2:
            # print(f2)
            for line in f:
                line = line.lstrip()
                line = replace_brackets(line)
                line = replace_clock_time(line)
                line = replace_quotes(line)

                article = line.replace('p . m .', 'p.m.').replace('a . m .', 'a.m.')\
                    .replace('i . e .', 'i.e.').replace('e . g .', 'e.g.') \
                    .replace(' ,', ',').replace(' .', '.') \
                    .replace(' :', ':').replace(' ;', ';') \
                    .replace(' ?', '?').replace(' !', '!') \
                    .replace(' (', '(').replace(' )', ')') \
                    .replace(' !', '!').replace(' {', '{') \
                    .replace(' }', '}').replace(' <', '<') \
                    .replace(' >', '>').replace(' ’', '’') \
                    .replace(' /', '/').replace(' -', '-') \
                    .replace(' $', '$').replace(' +', '+') \
                    .replace(' *', '*').replace(' /', '/') \
                    .replace(' "', '"').replace(' %', '%') \
                    .replace(' &', '&').replace(' +', "+") \
                    .replace(' -', '-').replace(' =', '=')

                f2.writelines(article)
print("Finished!")
