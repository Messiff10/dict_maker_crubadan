import codecs
import os
import re

from utils.reExpression import replace_quotes, replace_clock_time, replace_brackets
## 去空格
file_path = '/Users/ff/Desktop/train_data/it/it_web_split.txt'
file_out_path = '/Users/ff/Desktop/train_data/it/it_web_token.txt'
names = []
# for dir_path, subpaths, files in os.walk(data_folder):
#     for name in filter(lambda x: x.endswith('_tok.txt'), files):  # 文件夹下的所有文件
#         file_path = os.path.join(dir_path, name)
#         names.append(name)

regex = re.compile('\s+')


with codecs.open(file_path, encoding='utf-8') as f:
    with codecs.open(file_out_path, 'w', encoding='utf-8') as f2:
        # print(f2)
        for line in f:
            line = line.lstrip()
            line = replace_brackets(line)
            line = replace_clock_time(line)
            line = replace_quotes(line)

            article = line.replace('p . m .', 'p.m.').replace('a . m .', 'a.m.')\
                .replace('i . e .', 'i.e.').replace('e . g .', 'e.g.') \
                .replace(' , ', ',').replace(' . ', '.') \
                .replace(' : ', ':').replace(' ; ', ';') \
                .replace(' ? ', '?').replace(' ! ', '!') \
                .replace(' ( ', '(').replace(' ) ', ')') \
                .replace(' ! ', '!').replace(' { ', '{') \
                .replace(' } ', '}').replace(' < ', '<') \
                .replace(' > ', '>').replace(' ’ ', '’') \
                .replace(' / ', '/').replace(' - ', '-') \
                .replace(' $ ', '$').replace(' + ', '+') \
                .replace(' * ', '*').replace(' / ', '/') \
                .replace(' " ', '"').replace(' % ', '%') \
                .replace(' & ', '&').replace(' + ', "+") \
                .replace(' - ', '-').replace(' = ', '=')\
                .replace(' %', '%')

            words = regex.split(article)
            if(len(words)>2):
                # print("line:" + article + "len:" + str(len(words)))
                f2.writelines(article)
            else:
                print("line:" + article + "len:" + str(len(words)))
print("Finished!")
