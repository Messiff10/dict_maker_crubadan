import os
import re

regex1 = re.compile(
    '[\±+_\-—–·&‰%¢$£¥₱€#@†*‡★؟\‚\:;¿?/,….~`|♪•♣♠♥♦√πΠ÷×§¶∆≠=≈∞°↑^←‚\:;¿?/,….~`|♪•♣♠♥♦√πΠ÷×§¶←↓→\\©®™℅,ـًٌٍَُِّْٰٖٕٓٔ¹½⅓¼⅛²⅔³¾⅜⅝⁴⅞@#¢₱€£¥%٪‰&_\-—–·+±\\﴾*★٭\‚›‹:;؛?؟∆≠=≈!∞°،↑)}\]’’>›»”’↓→\±+_\-—–·&‰٪%¢£¥₱€#@†*‡★؟„\©®™℅]')  # ar
regex2 = re.compile('\s+')
inputpath = "/Users/ff/Desktop/测评数据/特殊词汇占比"
# unigrampath = "/Users/ff/Desktop/测评数据/maps/address_unigram"
# outpath = "/Users/ff/Desktop/测评数据/maps/out.txt"
unigramset = ["Nazi", "Nazis", "Nazizeit", "Nazideutschland", "Hitler",
              "Hitlers", "Hitlergruß", "Führer", "Auschwitz", "Neonazi",
              "Minderrassige", "Sonderbehandlung", "Mischehe", "Vergasung",
              "vergasen", "Holocaust", "arisch", "Rassenschande", "Eintopf",
              "Betreuungseinrichtungen", "Konzentrationslager", "Hakenkreuz", "NSDAP",
              "Goebels", "Judenfrei", "Judenfeindlich", "Neonazis"]


def getmorewords(input):
    names = []
    for dir_path, subpaths, files in os.walk(input):
        for name in filter(lambda x: x.endswith('.txt'), files):  # 文件夹下的所有文件
            names.append(name)
    for name in names:
        all_count = 0
        senstive_count = 0
        file_path = os.path.join(input, name)
        with open(file_path, 'r', encoding='utf-8') as f_in:
            for line in f_in:
                line = re.sub(regex1, " ", line)
                line = re.sub("\s+", " ", line)
                words = regex2.split(line.strip())
                for word in words:
                    all_count += 1
                    for s in unigramset:
                        if word.strip().lower() == s.strip().lower():
                            # print(word,s)
                            senstive_count += 1
        print("场景：",name,"总词数",all_count,"敏感词数",senstive_count,"敏感词占比",float(int(senstive_count)/int(all_count)))


if __name__ == '__main__':
    getmorewords(inputpath)
    print("Finish line")
