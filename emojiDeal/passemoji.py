import sys

from utils.is_emoji import is_emoji
import re
import os
import time

"""
将语料中带表情的语句删除
"""
regex = re.compile('\s+')
emoji_path = sys.argv[1]
file_path = sys.argv[2]
emojiset = set()
with open(emoji_path, 'r', encoding='utf-8') as f_emoji:
    for line in f_emoji:
        emojis = line.strip().split('\t')
        if emojis[0] not in emojiset:
            emojiset.add(emojis[0])
count = 0
# 去表情
with open(file_path, 'r', encoding='utf-8') as add_file:
    with open(file_path.replace('.txt', '.noemoji'), 'w', encoding='utf-8') as out_file:
        for line in add_file:
            centence = line
            words = regex.split(line)
            for word in words:
                if word.strip() in emojiset:
                    centence = ""
                    # print(line)
                    # out_file.writelines(line)
                    break
            if centence is not "":
                count = count + 1
                out_file.writelines(line)
    print(count)
    out_file.close()
    add_file.close()
print("Finish line")
