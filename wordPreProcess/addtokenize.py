import codecs
import os
from utils.reExpression import replace_quotes, replace_clock_time, replace_brackets


## 训练语料新闻加空格
data_folder = '/Users/ff/Desktop/train_data/ru/ru_user_detok_more30.txt'
names = []
# for dir_path, subpaths, files in os.walk(data_folder):
#     for name in filter(lambda x: x.endswith('_tok.txt'), files):  # 文件夹下的所有文件
#         file_path = os.path.join(dir_path, name)
#         names.append(name)

# for name in data_folder:
# file_path = os.path.join(data_folder, name)
print(data_folder)

with codecs.open(data_folder, encoding='utf-8') as f:
    with codecs.open(data_folder.replace('.txt', '_addtoken.txt'), 'w', encoding='utf-8') as f2:
        # print(f2)
        for line in f:
            line = line.lstrip()
            line = replace_brackets(line)
            line = replace_clock_time(line)
            line = replace_quotes(line)

            # line.replaceAll("\\{.*?}", "")
            article = line.replace(',', ' , ').replace('.', ' . ')\
                .replace(':', ' : ').replace(';', ' ; ')\
                .replace('?', ' ? ').replace('!', ' ! ')\
                .replace('(', ' ( ').replace(')', ' ) ')\
                .replace('!', ' ! ').replace('{', ' { ')\
                .replace('}', ' } ').replace('<', ' < ')\
                .replace('>', ' > ')\
                .replace('/', ' / ').replace('-', ' - ')\
                .replace('$', ' $ ').replace('+', ' + ')\
                .replace('*', ' * ').replace('/', ' / ')\
                .replace('"',' " ').replace('%',' % ')\
                .replace('&',' & ').replace('+'," + ")\
                .replace('-',' - ').replace('=',' = ')\
                .replace('%',' % ')
            f2.writelines(article)
print("Finished!")
