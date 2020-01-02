# file_path="/Users/ff/Desktop/第一优先级语言词表/desc/wy筛选词表"
import codecs
import os
import re
###  对筛选词表进行去重，去emoji 去格式不正确行 去前后空格
from utils.is_emoji import is_emoji

regex = re.compile('\s+')
regex1 = re.compile('')
data_folder = '/Users/ff/Desktop/测评数据/首字母大写'
names = []
for dir_path, subpaths, files in os.walk(data_folder):
    for name in filter(lambda x: x.endswith('.txt'), files):  # 文件夹下的所有文件
        file_path = os.path.join(dir_path, name)
        names.append(name)

for name in names:
    file_path = os.path.join(data_folder, name)
    print(file_path)

    if os.path.exists(file_path.replace('.txt', '_case.txt')):
        print("remove file :", file_path.replace('.txt', '_case.txt'))
        os.remove(file_path.replace('.txt', '_case.txt'))
    with codecs.open(file_path, 'r', encoding='utf-8') as f:
        with codecs.open(file_path.replace('.txt', '_case.txt'), 'w', encoding='utf-8') as f2:
            for line in f:
                line=line.strip().lower()
                line=line.capitalize()
                print(line)
                f2.write(line.strip())
                f2.write('\n')
print("Finish line")
