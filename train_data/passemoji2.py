from utils.is_emoji import is_emoji
import re
import os
import time
regex = re.compile('\s+')
data_folder = '/Users/ff/Desktop/测评数据/去表情'
names = []

# string="hh hh ?? ?! ????AAA    ?  ?  A ??"
# ss=re.findall(regex,string)
# for s in ss:
#     string=string.replace(re.sub('\s+',string),'')
# print(string)
emoji_path="/Users/ff/Desktop/测评数据/wordcount/emojis"
emojiset=set()
with open(emoji_path ,'r',encoding='utf-8') as f_emoji:
    for line in f_emoji:
        emojis=line.strip().split('\t')
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
                words = regex.split(line)
                for word in words:
                    if word.strip() in emojiset:
                        centence=""
                        # print(line)
                        # out_file.writelines(line)
                        break
                if centence is not "":
                    count = count + 1
                    out_file.writelines(line)
                    # if count>=10000:
                    #     break
        print(count)
        out_file.close()
        add_file.close()
print("Finish line")