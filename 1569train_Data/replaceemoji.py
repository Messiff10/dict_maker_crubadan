import emoji

from utils.is_emoji import is_emoji
import re
import os
import time

regex = re.compile('\s+')
data_folder = '/Users/ff/Desktop/测评数据/替换表情'
names = []

# 替换表情
emoji_path = "/Users/ff/Desktop/测评数据/wordcount/emojis"
emojiset = set()
with open(emoji_path, 'r', encoding='utf-8') as f_emoji:
    for line in f_emoji:
        emojis = line.strip().split('\t')
        if emojis[0] not in emojiset:
            emojiset.add(emojis[0])
for dir_path, subpaths, files in os.walk(data_folder):
    for name in filter(lambda x: x.endswith('.txt'), files):  # 文件夹下的所有文件
        file_path = os.path.join(dir_path, name)
        names.append(name)
for name in names:
    file_path = os.path.join(data_folder, name)
    print(file_path)

    if os.path.exists(file_path.replace('.txt', '.noemoji')):
        print("remove:", file_path.replace('.txt', '.noemoji'))
        os.remove(file_path.replace('.txt', '.noemoji'))

    count = 0
    # 去表情
    with open(file_path, 'r', encoding='utf-8') as add_file:
        with open(file_path.replace('.txt', '.noemoji'), 'w', encoding='utf-8') as out_file:
            for line in add_file:
                centence = line
                line = re.sub(emoji.get_emoji_regexp(), ' ', line)
                line = re.sub('\s+', ' ', line.strip())
                if not line.strip() is "":
                    out_file.write(line.strip())
                    out_file.write('\n')
        print(count)
        out_file.close()
        add_file.close()
print("Finish line")
