from config.conf_zh import traditionalChineseIdiomwordPath, traditionalChineseSinglewordPath, \
    traditionalChineseIdiom_min_mwordPath, traditionalChineseHotmwordPath, traditionalChinese_out_dir, isNotAWord, \
    freq1, freq2, isModify,traditionalChineseModifyPath
import os
import json
from opencc import OpenCC
from pypinyin import lazy_pinyin, Style, pinyin
import random


##  格式：
##  普通  词  频率  0/1 拼音
##  shortcut   拼音  true  频率  词  0/1
##  两元词表  词 词 频率

# 繁体中文
def getShortWord():
    oc = OpenCC(conversion='s2twp')  # "出租车" --> "計程車" 带短语
    out_file_path = os.path.join(traditionalChinese_out_dir, "shortcut.txt")

    word_shortcut = []
    # 读取单个单词　　　文件格式：词　频率　１(繁体)／０（中文）　拼音
    with open(traditionalChineseSinglewordPath, 'r', encoding='utf-16') as simplifiedChineseSingleWord_file:
        for line in simplifiedChineseSingleWord_file:
            items = line.strip().split(" ")
            jianti = items[0].strip()
            fanti = oc.convert(jianti)
            # pinyin = items[3].strip()
            begin = line.index(items[3])
            end = line.index("\n")
            pinyin = str(line[begin:end])
            # for i in range(3,len(items)):
            #     pinyin = seq.join(items[i])
                # pinyin.append("".join([items[i]]))
            res_line = pinyin + "\t" + isNotAWord + "\t" + items[1] + "\t" + fanti + "\t" + freq2 + "\n"
            word_shortcut.append(res_line)

    print("word size:", str(len(word_shortcut)))
    return word_shortcut

def getHotword():
    oc = OpenCC(conversion='s2twp')  # "出租车" --> "計程車" 带短语
    out_file_path = os.path.join(traditionalChinese_out_dir, "hotword.txt")
    addfile = os.path.join(traditionalChineseModifyPath, "hot_modify.txt")
    res = []
    hotword_shortcut = []
    hotword_bigram = []
    add_hotword = []
    add_shortcut = []
    add_bigram = []
    with open(traditionalChineseHotmwordPath, 'r', encoding='utf-8') as simplifiedChineseWord_file:
        for line in simplifiedChineseWord_file:
            items = line.strip().split("\t", maxsplit=4)
            jianti = items[0].strip()
            # fanti = HanziConv.toTraditional(jianti)
            fanti = oc.convert(jianti)
            zhuyin = " ".join(lazy_pinyin(fanti, style=Style.BOPOMOFO))

            # res_line = fanti + "\t" + str(random.randint(160, 300)) + "\t" + freq2 + "\t" + zhuyin + "\n"
            res_line = fanti + "\t" + str(random.randint(160, 300)) + "\t" + freq2 + "\t" + zhuyin + "\n"
            res.append(res_line)
            res_line_splits = res_line.split("\t", maxsplit=4)
            res_line2 = zhuyin + "\t" + isNotAWord + "\t" + res_line_splits[1] + "\t" + res_line_splits[0] + "\t" + freq2 + "\n"
            hotword_shortcut.append(res_line2)
            res_line3 = res_line_splits[0] + "\t" + res_line_splits[0] + "\t" + res_line_splits[1] + "\n"
            hotword_bigram.append(res_line3)

    with open(addfile , 'r' , encoding='utf-8') as ft_addfile:
        for line in ft_addfile:
            items = line.strip().split("\t")
            fanti = oc.convert(items[0])
            zhuyin = " ".join(lazy_pinyin(fanti, style=Style.BOPOMOFO))
            add_line = fanti + "\t" + str(random.randint(160, 300)) + "\t" + freq2 + "\t" + zhuyin + "\n"
            res_line_splits = add_line.split("\t", maxsplit=4)
            add_shortcut_line = zhuyin + "\t" + isNotAWord + "\t" + res_line_splits[1] + "\t" + res_line_splits[0] + "\t" + freq2 + "\n"
            add_shortcut.append(add_shortcut_line)
            add_bigram_line = res_line_splits[0] + "\t" + res_line_splits[0] + "\t" + res_line_splits[1] + "\n"
            add_bigram.append(add_bigram_line)
            add_hotword.append(add_line)
    # res = set(res) - set(delete_hotword)
    # res = res.union(set(add_hotword))
    for item in add_shortcut:
            hotword_shortcut.append(item)
    for item in add_bigram:
            hotword_bigram.append(item)
    for item in add_hotword:
            res.append(item)
    # if isModify:
    #     for item in delete_hotword:
    #         items = item.strip().split(" ", maxsplit=4)
    #         delete_line = items[3] + "\t" + isNotAWord + "\t" + items[0] + "\t" + freq2 + "\n"
    #         if delete_line in hotword_shortcut:
    #             hotword_shortcut.remove(delete_line)
    #         else:
    #             print(delete_line)
    #
    #     for item in add_hotword:
    #         items = item.strip().split(" ", maxsplit=4)
    #         add_line = items[3] + "\t" + isNotAWord + "\t" + items[0] + "\t" + freq2 + "\n"
    #         hotword_shortcut.append(add_line)

    with open(out_file_path, 'w', encoding='utf-8') as out_file:
        out_file.writelines(res)
    print("热词 size:", str(len(hotword_shortcut)))
    return hotword_shortcut,hotword_bigram

def getiIdiomWord():
    oc = OpenCC(conversion='s2twp')  # "出租车" --> "計程車" 带短语
    out_file_path = os.path.join(traditionalChinese_out_dir, "idiom.txt")
    addfile = os.path.join(traditionalChineseModifyPath, "idom_modify.txt")
    res = []
    idiomWord = []
    idiom_bigram = []
    add_hotword = []
    add_shortcut = []
    add_bigram = []
    with open(traditionalChineseIdiom_min_mwordPath, 'r', encoding='utf-8') as traditionalChineseWord_file:
        for line in traditionalChineseWord_file:
            items = line.strip().split("\t", maxsplit=4)
            jianti = items[0].strip()
            # fanti = HanziConv.toTraditional(jianti)
            fanti = oc.convert(jianti)
            zhuyin = " ".join(lazy_pinyin(fanti, style=Style.BOPOMOFO))
            # random.randrange(9000000, 11000000, 5)
            res_line = fanti + "\t" + str(random.randint(160, 300)) + "\t" + freq2 + "\t" + zhuyin + "\n"
            res.append(res_line)
            res_line_splits = res_line.split("\t", maxsplit=4)
            res_line2 = zhuyin + "\t" + isNotAWord + "\t" + res_line_splits[1] + "\t" + res_line_splits[0] + "\t" + freq2 + "\n"
            idiomWord.append(res_line2)
            res_line3 = res_line_splits[0] + "\t" + res_line_splits[0] + "\t" + res_line_splits[1] + "\n"
            idiom_bigram.append(res_line3)
    with open(addfile , 'r' , encoding='utf-8') as ft_addfile:
        for line in ft_addfile:
            items = line.strip().split("\t")
            fanti = oc.convert(items[0])
            zhuyin = " ".join(lazy_pinyin(fanti, style=Style.BOPOMOFO))
            add_line = fanti + "\t" + str(random.randint(160, 300)) + "\t" + freq2 + "\t" + zhuyin + "\n"
            res_line_splits = add_line.split("\t", maxsplit=4)
            add_shortcut_line = zhuyin + "\t" + isNotAWord + "\t" + res_line_splits[1] + "\t" + res_line_splits[0] + "\t" + freq2 + "\n"
            add_shortcut.append(add_shortcut_line)
            add_bigram_line = res_line_splits[0] + "\t" + res_line_splits[0] + "\t" + res_line_splits[1] + "\n"
            add_bigram.append(add_bigram_line)
            add_hotword.append(add_line)
    for item in add_shortcut:
            idiomWord.append(item)
    for item in add_bigram:
            idiom_bigram.append(item)
    for item in add_hotword:
            res.append(item)
    # 排除掉需要 修改删除 的内容
    # res = set(res) - set(delete_idiom)
    # # res_ft = set(res_ft) - set(delete_idiom)
    # # 拼接需要 修改增加 的内容
    # res = res.union(set(add_idiom))
    # res_ft = res.union(set(add_idiom))

    # if isModify:
    #     for item in delete_idiom:
    #         items = item.strip().split(" ", maxsplit=4)
    #         # 拼接格式  首字母拼接   true 100 句子 1
    #         delete_line = items[3] + "\t" + isNotAWord + "\t" + freq1 + "\t" + items[0] + "\t" + freq2 + "\n"
    #         # 将res_shortcut中在 修改删除 中的内容删除
    #         if delete_line in idiomWord:
    #             idiomWord.remove(delete_line)
    #         else:
    #             print(delete_line)
    #
    #     for item in add_idiom:
    #         items = item.strip().split(" ", maxsplit=4)
    #         # 拼接格式  首字母拼接   true 100 句子 1
    #         add_line = items[3] + "\t" + isNotAWord + "\t" + freq1 + "\t" + items[0] + "\t" + freq2 + "\n"
    #         # 在res_shortcut添加 修改添加 中的内容
    #         idiomWord.append(add_line)

    # 输出idiom文件中的格式  单词 100 1  首字母拼接
    with open(out_file_path, 'w', encoding='utf-8') as out_file:
        out_file.writelines(res)
    print("idiom size:", str(len(idiomWord)))
    # 返回 首字母拼接 true 100 单词 1
    return idiomWord,idiom_bigram

# def getiIdiom_min_Word(add_idiom=None, delete_idiom=None):
#     oc = OpenCC(conversion='s2twp')  # "出租车" --> "計程車" 带短语
#     out_file_path = os.path.join(traditionalChinese_out_dir, "idiom.txt")
#     res = []
#     idiom_min_Word = []
#     idiom_min_bigram = []
#     with open(traditionalChineseIdiomwordPath, 'r', encoding='utf-8') as traditionalChineseWord_file:
#         for line in traditionalChineseWord_file:
#             items = line.strip().split(",", maxsplit=2)
#             jianti = items[0].strip()
#             # fanti = HanziConv.toTraditional(jianti)
#             fanti = oc.convert(jianti)
#             zhuyin = " ".join(lazy_pinyin(fanti, style=Style.BOPOMOFO))
#             # random.randrange(9000000, 11000000, 5)
#             res_line = fanti + "\t" + str(random.randint(160, 300)) + "\t" + freq2 + "\t" + zhuyin + "\n"
#             res.append(res_line)
#             res_line_splits = res_line.split("\t", maxsplit=4)
#             res_line2 = zhuyin + "\t" + isNotAWord + "\t" + res_line_splits[1] + "\t" + fanti + "\t" + freq2 + "\n"
#             idiom_min_Word.append(res_line2)
#             res_line3 = res_line_splits[0]+"\t"+res_line_splits[0]+"\t"+res_line_splits[1] + "\n"
#             idiom_min_bigram.append(res_line3)
#
#     # 排除掉需要 修改删除 的内容
#     res = set(res) - set(delete_idiom)
#     # res_ft = set(res_ft) - set(delete_idiom)
#     # 拼接需要 修改增加 的内容
#     res = res.union(set(add_idiom))
#     # res_ft = res.union(set(add_idiom))
#
#     if isModify:
#         for item in delete_idiom:
#             items = item.strip().split(" ", maxsplit=4)
#             # 拼接格式  首字母拼接   true 100 句子 1
#             delete_line = items[3] + "\t" + isNotAWord + "\t" + freq1 + "\t" + items[0] + "\t" + freq2 + "\n"
#             # 将res_shortcut中在 修改删除 中的内容删除
#             if delete_line in idiom_min_Word:
#                 idiom_min_Word.remove(delete_line)
#             else:
#                 print(delete_line)
#
#         for item in add_idiom:
#             items = item.strip().split(" ", maxsplit=4)
#             # 拼接格式  首字母拼接   true 100 句子 1
#             add_line = items[3] + "\t" + isNotAWord + "\t" + freq1 + "\t" + items[0] + "\t" + freq2 + "\n"
#             # 在res_shortcut添加 修改添加 中的内容
#             idiom_min_Word.append(add_line)
#
#     # 输出idiom文件中的格式  单词 100 1  首字母拼接
#     with open(out_file_path, 'w', encoding='utf-8') as out_file:
#         out_file.writelines(res)
#     print("idiom size:", str(len(idiom_min_Word)))
#     # 返回 首字母拼接 true 100 单词 1
#     return idiom_min_Word,idiom_min_bigram

def getModifyList():
    # 读取需要修改的词，并进行拼接  格式：类别 句子  100  1 拼音
    add_path = traditionalChineseModifyPath + "traditional_add.tsv"
    delete_path = traditionalChineseModifyPath + "traditional_delete.tsv"
    add_idiom, add_minidiom,add_hotword = [], [], [], [], []
    delete_idiom,delete_minidiom, delete_hotword = [], [], [], [], []

    add_index, delete_index = None, None

    with open(add_path, 'r', encoding='utf-8') as add_file:
        count = 0
        for line in add_file:
            # 第一行是表头
            count += 1
            if count == 1:
                continue
            items = [item.strip() for item in line.strip().split("\t")]

            if len(items) == 2:
                if items[0] == "hotword":
                    add_index = "hotword"
                    add_hotword.append(items[1])
                elif items[0] == "idiom":
                    add_index = "idiom"
                    add_idiom.append(items[1])
                elif items[0] == "idiom_min":
                    add_index = "idiom_min"
                    add_minidiom.append(items[1])
            elif len(items) == 1 and items[0] != "":
                if add_index == "idiom":
                    add_idiom.append(items[0])
                elif add_index == "hotword":
                    add_hotword.append(items[0])
                elif add_index == "idiom_min":
                    add_minidiom.append(items[0])
    with open(delete_path, 'r', encoding='utf-8') as delete_file:
        count = 0
        for line in delete_file:
            count += 1
            if count == 1:
                continue
            items = [item.strip() for item in line.strip().split("\t")]

            if len(items) == 2:
                if items[0] == "hotword":
                    delete_index = "hotword"
                    delete_hotword.append(items[1])
                elif items[0] == "idiom":
                    delete_index = "idiom"
                    delete_idiom.append(items[1])
                elif items[0] == "idiom_min":
                    delete_index = "idiom_min"
                    delete_minidiom.append(items[1])
            elif len(items) == 1 and items[0] != "":
                if delete_index =="idiom":
                    delete_idiom.append(items[0])
                elif delete_index == "idiom_min":
                    delete_minidiom.append(items[0])
                elif delete_index == "hotword":
                    delete_hotword.append(items[0])

    print(len(add_idiom), len(add_minidiom), len(add_hotword),
        len(delete_idiom), len(delete_minidiom), len(delete_hotword))
    return add_idiom, add_minidiom,add_hotword,\
           delete_idiom, delete_minidiom,delete_hotword

if __name__ == "__main__":
    # if isModify == True:
    #     add_idiom, add_minidiom, add_hotword, \
    #     delete_idiom, delete_minidiom, delete_hotword = getModifyList()
    idiom_shortcut,idiom_bigram = getiIdiomWord()  #长材小试 100 1 ccxs
    # idiom_min_shortcut,idiom_min_bigram = getiIdiom_min_Word()
    hotword_shortcut,hotword_bigram = getHotword()  #吃热狗 100 1 crg
    word_shortcut = getShortWord()  #鼥	true	100	ba	1

    unigram_out_file_path = os.path.join(traditionalChinese_out_dir, "unigram.txt")
    bigram_out_file_path = os.path.join(traditionalChinese_out_dir, "bigram.txt")
    shortcut_out_file_path = os.path.join(traditionalChinese_out_dir, "shortcut.txt")

    if os.path.exists(unigram_out_file_path):
        print("remove", unigram_out_file_path)
        os.remove(unigram_out_file_path)
    if os.path.exists(bigram_out_file_path):
        print("remove", bigram_out_file_path)
        os.remove(bigram_out_file_path)
    if os.path.exists(shortcut_out_file_path):
        print("remove", shortcut_out_file_path)
        os.remove(shortcut_out_file_path)

    with open(unigram_out_file_path, 'a', encoding='utf-8') as unigram_file:
        unigram_file.writelines({})
    with open(bigram_out_file_path, 'a', encoding='utf-8') as bigram_file:
        bigram_file.writelines(idiom_bigram)
        # bigram_file.writelines(idiom_min_bigram)
        bigram_file.writelines(hotword_bigram)
    with open(shortcut_out_file_path, 'a', encoding='utf-8') as shortcut_file:
        shortcut_file.writelines(word_shortcut)
        shortcut_file.writelines(idiom_shortcut)
        # shortcut_file.writelines(idiom_min_shortcut)
        shortcut_file.writelines(hotword_shortcut)

    print("Finished!")




##  格式：
##  普通  词  频率  0/1 拼音
##  shortcut   拼音  true  频率  词  0/1
##  两元词表  词 词 频率