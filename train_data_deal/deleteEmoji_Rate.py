from utils.is_emoji import is_emoji
import re
import os
import time
"""
将一句话中带表情或者不满足过筛的语句删除
"""
regex = re.compile('\s+')
data_folder = '/Users/ff/Desktop/测评数据/去表情'
names = []
emojiset = set()
unigramset=set()

def getemoji(emoji_path):
    with open(emoji_path, 'r', encoding='utf-8') as f_emoji:
        for line in f_emoji:
            emojis = line.strip().split('\t')
            if emojis[0].strip() not in emojiset:
                emojiset.add(emojis[0])

def getunigram(file):
    with open(file,'r',encoding='utf-8') as f_uni:
        for uni in f_uni:
            unigrams=uni.strip().split('\t')
            if unigrams[0].strip() not in unigramset:
                unigramset.add(unigrams[0].strip())

def emojichoose():
    for dir_path, subpaths, files in os.walk(data_folder):
        for name in filter(lambda x: x.endswith('.txt'), files):  # 文件夹下的所有文件
            file_path = os.path.join(dir_path, name)
            names.append(name)
    for name in names:
        file_path = os.path.join(data_folder, name)
        print(file_path)

        if os.path.exists(file_path.replace('.txt', '.emoji')):
            print("remove:", file_path.replace('.txt', '.emoji'))
            os.remove(file_path.replace('.txt', '.emoji'))

        # 去表情
        with open(file_path, 'r', encoding='utf-8') as add_file:
            with open(file_path.replace('.txt', '.emoji'), 'w', encoding='utf-8') as out_file:

                for line in add_file:
                    count = 0
                    truecount=0
                    centence = line
                    words = regex.split(line)
                    for word in words:
                        if word in emojiset:
                            centence = ""
                            break
                    if centence is "":
                        words = regex.split(line)
                        for wo in words:
                            count += 1
                            if wo in unigramset:
                                truecount+=1
                        if float(truecount/count)>0.8:
                            print(truecount,count,float(truecount/count))
                            # print("true line",line)
                            out_file.writelines(line)
            print(count)
            out_file.close()
            add_file.close()


if __name__ == '__main__':
    emoji_path = "/Users/ff/Desktop/train_data/emojis"
    unigram_path="/Users/ff/Desktop/train_data/ar/ar_unigram"
    getemoji(emoji_path)
    getunigram(unigram_path)
    emojichoose()
    print("Finish line")
