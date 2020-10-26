# file_path="/Users/ff/Desktop/第一优先级语言词表/desc/wy筛选词表"
import codecs
import os
import re

"""
对筛选词表进行去重，去emoji 去格式不正确行 去前后空格
文件夹处理
"""
# from utils.is_emoji import is_emoji

regex = re.compile('\s+')
regex1 = re.compile('')
data_folder = '/Users/ff/Desktop/第一优先级语言词表/desc/wy筛选词表'
names = []
for dir_path, subpaths, files in os.walk(data_folder):
    for name in filter(lambda x: x.endswith('.txt'), files):  # 文件夹下的所有文件
        file_path = os.path.join(dir_path, name)
        names.append(name)
sentive_low = set()
for name in names:
    file_path = os.path.join(data_folder, name)
    print(file_path)

    if os.path.exists(file_path.replace('.txt', '_')):
        print("remove file :", file_path.replace('.txt', '_'))
        os.remove(file_path.replace('.txt', '_'))
    unigram = set()
    with codecs.open(file_path, 'r') as f:
        with codecs.open(file_path.replace('.txt', '_'), 'w') as f2:
            for line in f:
                words = line.strip().split('\t')
                if not words[0].strip() is "":
                    if not words[0].strip() in unigram:
                        # if not words[0].lower() in sentive_low:
                        unigram.add(words[0].strip())
                        f2.write(words[0].strip())
                        f2.write('\n')
                    # else:
                    #     print("emoji word:",line)
                    else:
                        # f2.write(str(words[0]).strip())
                        # f2.write('\n')
                        print("distinct:", line)
                else:
                    print("error line :", line)
print("Finish line")
