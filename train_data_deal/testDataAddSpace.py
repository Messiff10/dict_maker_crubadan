import codecs
import os
import re
"""
测评标点前后加空格
"""
from utils.reExpression import replace_quotes, replace_clock_time, replace_brackets

regex=re.compile('\s+')
## 训练语料新闻加空格
# /Users/ff/Desktop/train_data/测评语料加空格处理
# /Users/ff/Desktop/data/word/runword/notAddNoise/scenes/1
data_folder = '/Users/ff/Desktop/train_data/测评语料加空格处理'
names = []
for dir_path, subpaths, files in os.walk(data_folder):
    for name in filter(lambda x: x.endswith('.txt'), files):  # 文件夹下的所有文件
        file_path = os.path.join(dir_path, name)
        names.append(name)

for name in names:
    file_path = os.path.join(data_folder, name)
    print(file_path)

    if os.path.exists(file_path.replace('.txt', '.txt.addtoken')):
        print("remove:",file_path.replace('.txt', '.txt.addtoken'))
        os.remove(file_path.replace('.txt', '.txt.addtoken'))

    with codecs.open(file_path, encoding='utf-8') as f:
        with codecs.open(file_path.replace('.txt', '.txt.addtoken'), 'w', encoding='utf-8') as f2:
            # print(f2)
            centent=set()
            for line in f:
                line = line.lstrip()
                line = replace_brackets(line)
                line = replace_clock_time(line)
                line = replace_quotes(line)
                if line.strip().startswith('©') | line.strip().startswith('2019') | line.strip().startswith('Copyright'):
                    continue
                fileds=regex.split(line.strip())
                if len(fileds)>3:
                    if line.strip() not in centent:
                        # line.replaceAll("\\{.*?}", "")
                        article = line.strip().replace(',', ' , ').replace('.', ' . ')\
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
                        centent.add(line.strip())
                        f2.write(article)
                        f2.write('\n')
print("Finished!")
