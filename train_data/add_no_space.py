import codecs
import os
import re

import emoji


def is_emoji(content):
    if re.match(emoji.get_emoji_regexp(), content):
        return True
    return False


regex = re.compile(
    '[\])>}{\[<(±+_\-—–·&‰%¢$£¥₱€#@†*‡★؟„\”“«»‚‹›\:;¡!¿?/,….~`|♪•♣♠♥♦√πΠ÷×§¶∆≠=≈∞′°″↑^←«»‚‹›\:;¡!¿?/,….~`|♪•♣♠♥♦√πΠ÷×§¶←↓→\\©®™℅,ـًٌٍَُِّْٰٖٕٓٔ¹½⅓¼⅛²⅔³¾⅜⅝⁴⅞@#¢₱€£¥%٪‰&_\-—–·+±\)}>﴿\({<﴾*★٭"„“”»«\‚‘’›‹:;؛¡!?؟∆≠=≈∞′°″،↑↓→\\\[\]\)>}{\[<\(±+_\-—–·&‰٪%¢£¥₱€#@†*‡★؟„\”“©®™℅]')  # ar

regex2 = re.compile('\s+')
regex3 = re.compile('')
data_folder = '/Users/ff/Desktop/测评数据/加空格'
names = []
emojiset = set()
centence=set()

def getemoji(emoji_path):
    with open(emoji_path, 'r', encoding='utf-8') as f_emoji:
        for line in f_emoji:
            emojis = line.strip().split('\t')
            if emojis[0].strip() not in emojiset:
                emojiset.add(emojis[0])


def addspace():
    for dir_path, subpaths, files in os.walk(data_folder):
        for name in filter(lambda x: x.endswith('.txt'), files):  # 文件夹下的所有文件
            file_path = os.path.join(dir_path, name)
            names.append(name)
    for name in names:
        file_path = os.path.join(data_folder, name)
        print(file_path)

        if os.path.exists(file_path.replace('.txt', '.space_pass_distinct')):
            print("remove:", file_path.replace('.txt', '.space_pass_distinct'))
            os.remove(file_path.replace('.txt', '.space'))
        with open(file_path, 'r', encoding='utf-8') as f_in:
            with open(file_path.replace('.txt', '.space_pass_distinct'), 'w', encoding='utf-8') as f_out:
                for line in f_in:
                    # print(line)

                    # line.replace()
                    # words=re.find(regex,line)
                    allwords = regex3.split(line)
                    for allw in allwords:
                        if allw.strip() in emojiset:
                            line = ""
                            # print(line)
                            break
                            # line = line.replace(allw, ' ' + allw + ' ')
                            # line = re.sub('\s+', ' ', line)
                    if line is not "":
                        if line not in centence:
                            centence.add(line)
                            words = re.findall(regex, line)
                            for w in words:
                                # line=line.replace(' ','')
                                # 先去空格
                                # line = line.replace(' '+w , w)
                                line = re.sub('\s+', ' ', line)
                                line = line.replace(' ' + w + ' ', w)
                                line = line.replace(' ' + w, w)
                                line = line.replace(w + ' ', w)
                                # line = line.replace('  ', '')
                                # 加空格
                                line = line.replace(w, ' ' + w + ' ')  # 加空格
                                line=re.sub(r"(\w+) ?\' (\w+)?",r"\1'\2",line)
                                # line = line.replace('\'', '\'')
                            line = re.sub('\s+', ' ', line)
                            # print(line)
                            f_out.write(line.strip())
                            f_out.write('\n')


if __name__ == '__main__':
    emoji_path = "/Users/ff/Desktop/train_data/all_emojis"
    getemoji(emoji_path)
    addspace()
    print("Finsh line")
# print(line)
