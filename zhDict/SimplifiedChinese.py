from lib2to3.pgen2.conv import Converter

from config.conf_zh import simplifiedChineseIdiomPath, simplifiedChineseXiehouyuPath, simplifiedChineseProverbPath,\
    simplifiedChinesePoetryPath, simplifiedChineseHotwordPath, simplifiedChinese_out_dir, simplifiedChineseWordPath,\
    simplifiedChineseModifyPath, isNotAWord, freq1, freq2, isModify
# from zhDict.transform.langconv import *
import json
import os
import re
from utils.reExpression import pattern_brackets, pattern_bracket_left, pattern_bracket_right
from pypinyin import lazy_pinyin
from opencc import OpenCC


# 简体中文
def Traditional2Simplified(sentence):
  '''
  将sentence中的繁体字转为简体字
  :param sentence: 待转换的句子
  :return: 将句子中繁体字转换为简体字之后的句子
  '''
  sentence = Converter('zh-hans').convert(sentence)
  return sentence
def Simplified2Traditional(sentence):
  '''
  将sentence中的简体字转为繁体字
  :param sentence: 待转换的句子
  :return: 将句子中简体字转换为繁体字之后的句子
  '''
  sentence = Converter('zh-hant').convert(sentence)
  return sentence

def getPinyinAbbreviation(pinyin):
    # 返回拼音的首字母集合
    # 输入：['a', 'bi', 'di', 'yu'] --> 输出：abdy
    abbr = "".join([item.strip()[0] for item in pinyin])
    return abbr


def getWord():
    word_shortcut = []
    # 读取单个单词　　　文件格式：词　频率　１(繁体)／０（中文）　拼音
    with open(simplifiedChineseWordPath, 'r', encoding='utf-16') as simplifiedChineseWord_file:
        for line in simplifiedChineseWord_file:
            items = line.strip().split(" ", maxsplit=4)
            jianti = items[0].strip()
            pinyin = items[3].strip()
            res_line = jianti + "\t" + isNotAWord + "\t" + freq1 + "\t" + pinyin + "\t" + freq2 + "\n"
            word_shortcut.append(res_line)

    print("word size:", str(len(word_shortcut)))
    return word_shortcut


def getIdiom(add_idiom=None, delete_idiom=None):
    # 成语文件
    # 输出路径
    out_file_path = os.path.join(simplifiedChinese_out_dir, "idiom.txt")
    out_file_path_ft = os.path.join(simplifiedChinese_out_dir, "idiom_ft.txt")
    res = []
    res_ft= []
    res_shortcut = []
    res_shortcut_ft= []
    # 新华成语文件
    with open(simplifiedChineseIdiomPath, 'r', encoding='utf-8') as idiomFile:
        idioms = json.load(idiomFile)
        for idiom_item in idioms:
            word = idiom_item["word"].replace("，", "")
            # 拼音格式 ['a', 'bi', 'di', 'yu']
            pinyin = lazy_pinyin(word)
            # 获得首字母拼接
            pinyinAbbr = getPinyinAbbreviation(pinyin)
            line1 = word + " " + freq1 + " " + freq2 + " " + pinyinAbbr + "\n"
            line1_ft=Simplified2Traditional(word) + " " + freq1 + " " + freq2 + " " + pinyinAbbr + "\n"
            # 拼接格式 单词 100 1  首字母拼接
            res.append(line1)
            res_ft.append(line1_ft)
            line3 = pinyinAbbr + "\t" + isNotAWord + "\t" + freq1 + "\t" + word + "\t" + freq2 + "\n"
            line3_ft=pinyinAbbr + "\t" + isNotAWord + "\t" + freq1 + "\t" + Simplified2Traditional(word) + "\t" + freq2 + "\n"
            # 拼接格式 首字母拼接 true 100 单词 1
            res_shortcut.append(line3)
            res_shortcut_ft.append(line3_ft)

    # 排除掉需要 修改删除 的内容
    res = set(res) - set(delete_idiom)
    # res_ft = set(res_ft) - set(delete_idiom)
    # 拼接需要 修改增加 的内容
    res = res.union(set(add_idiom))
    # res_ft = res.union(set(add_idiom))

    if isModify:
        for item in delete_idiom:
            items = item.strip().split(" ", maxsplit=4)
            # 拼接格式  首字母拼接   true 100 句子 1
            delete_line = items[3] + "\t" + isNotAWord + "\t" + freq1 + "\t" + items[0] + "\t" + freq2 + "\n"
            # 将res_shortcut中在 修改删除 中的内容删除
            if delete_line in res_shortcut:
                res_shortcut.remove(delete_line)
            else:
                print(delete_line)

        for item in add_idiom:
            items = item.strip().split(" ", maxsplit=4)
            # 拼接格式  首字母拼接   true 100 句子 1
            add_line = items[3] + "\t" + isNotAWord + "\t" + freq1 + "\t" + items[0] + "\t" + freq2 + "\n"
            # 在res_shortcut添加 修改添加 中的内容
            res_shortcut.append(add_line)

    # 输出idiom文件中的格式  单词 100 1  首字母拼接
    with open(out_file_path, 'w', encoding='utf-8') as out_file:
        out_file.writelines(res)
    with open(out_file_path_ft, 'w', encoding='utf-8') as out_file_ft:
        out_file_ft.writelines(res_ft)
    print("idiom size:", str(len(res_shortcut)),"idiom_ft.size",str(len(res_shortcut_ft)))
    # 返回 首字母拼接 true 100 单词 1
    return res_shortcut


def getXiehouyu(add_xiehouyu=None, delete_xiehouyu=None):
    out_file_path = os.path.join(simplifiedChinese_out_dir, "xiehouyu.txt")
    res = []
    res_riddle_answer = []
    res_shortcut = []
    with open(simplifiedChineseXiehouyuPath, 'r', encoding='utf-8') as xiehouyuFile:
        xiehouyus = json.load(xiehouyuFile)
        for xiehouyu_item in xiehouyus:
            riddle_ = xiehouyu_item["riddle"].strip().split("；")[0]
            riddle = re.sub(pattern_brackets, "", riddle_)
            riddle = re.sub(pattern_bracket_left, "", riddle)
            riddle = re.sub(pattern_bracket_right, "", riddle)
            riddle_pinyinAbbr = getPinyinAbbreviation(lazy_pinyin(riddle))

            answer_ = xiehouyu_item["answer"].strip().split("；")[0]
            answer = re.sub(pattern_brackets, "", answer_)
            answer = re.sub(pattern_bracket_left, "", answer)
            answer = re.sub(pattern_bracket_right, "", answer)
            answer_pinyinAbbr = getPinyinAbbreviation(lazy_pinyin(answer))

            if riddle == "" or answer == "":
                continue

            line = riddle + "," + answer + " " + freq1 + " " + freq2 + " " + \
                   riddle_pinyinAbbr + " " + answer_pinyinAbbr + "\n"
            res.append(line)
            line2 = riddle + "\t" + answer + "\t" + freq2 + "\n"
            res_riddle_answer.append(line2)
            line3 = riddle_pinyinAbbr + "\t" + isNotAWord + "\t" + freq1 + "\t" + riddle + "\t" + freq2 + "\n"
            res_shortcut.append(line3)

    res = set(res) - set(delete_xiehouyu)
    res = res.union(set(add_xiehouyu))

    if isModify:
        for item in delete_xiehouyu:
            items = item.strip().split(" ", maxsplit=4)
            delete_line = items[3] + "\t" + isNotAWord + "\t" + freq1 + "\t" + items[0] + "\t" + freq2 + "\n"
            if delete_line in res_shortcut:
                res_shortcut.remove(delete_line)
            else:
                print(delete_line)

        for item in add_xiehouyu:
            items = item.strip().split(" ", maxsplit=4)
            add_line = items[3] + "\t" + isNotAWord + "\t" + freq1 + "\t" + items[0] + "\t" + freq2 + "\n"
            res_shortcut.append(add_line)
            riddle_answer = re.split(r',|，', items[0])
            riddle_answer_line = riddle_answer[0] + "\t" + riddle_answer[1] + "\t" + freq2 + "\n"
            res_riddle_answer.append(riddle_answer_line)

    with open(out_file_path, 'w', encoding='utf-8') as out_file:
        out_file.writelines(res)
    print("歇后语 size:", str(len(res_shortcut)))
    return res_riddle_answer, res_shortcut


def getPoetry(add_poetry=None, delete_poetry=None):
    out_file_path = os.path.join(simplifiedChinese_out_dir, "poetry.txt")
    res = []
    res_bigram = []
    res_shortcut = []
    with open(simplifiedChinesePoetryPath, 'r', encoding='utf-8') as poetryFile:
        for poetry in poetryFile:
            poetry = poetry.strip()
            items = poetry.split("，")
            first = items[0]
            first_pinyinAbbr = getPinyinAbbreviation(lazy_pinyin(first))
            line = poetry + " " + freq1 + " " + freq2 + " " + first_pinyinAbbr + "\n"

            if len(items) == 2:
                second = items[1]
                second_pinyinAbbr = getPinyinAbbreviation(lazy_pinyin(second))

                line_bigram = first + "\t" + second + "\t" + freq2 + "\n"
                res_bigram.append(line_bigram)

                line = poetry + " " + freq1 + " " + freq2 + " " + \
                       first_pinyinAbbr + " " + second_pinyinAbbr + "\n"

            res.append(line)
            line_shortcut = first + "\t" + isNotAWord + "\t" + freq1 + "\t" + first_pinyinAbbr + "\t" + freq2 + "\n"
            res_shortcut.append(line_shortcut)
            pass

    res = set(res) - set(delete_poetry)
    res = res.union(set(add_poetry))

    if isModify:
        for item in delete_poetry:
            items = item.strip().split(" ", maxsplit=4)
            delete_line = items[3] + "\t" + isNotAWord + "\t" + freq1 + "\t" + items[0] + "\t" + freq2 + "\n"
            if delete_line in res_shortcut:
                res_shortcut.remove(delete_line)
            else:
                print(delete_line)

            first_second = re.split(r',|，', items[0])
            line_bigram = first_second[0] + "\t" + first_second[1] + "\t" + freq2 + "\n"
            res_bigram.remove(line_bigram)

        for item in add_poetry:
            items = item.strip().split(" ", maxsplit=4)
            add_line = items[3] + "\t" + isNotAWord + "\t" + freq1 + "\t" + items[0] + "\t" + freq2 + "\n"
            res_shortcut.append(add_line)
            first_second = re.split(r',|，', items[0])
            line_bigram = first_second[0] + "\t" + first_second[1] + "\t" + freq2 + "\n"
            res_bigram.append(line_bigram)

    with open(out_file_path, 'w', encoding='utf-8') as out_file:
        out_file.writelines(res)
    print("诗歌 size:", str(len(res_shortcut)))
    return res_bigram, res_shortcut


def getProverb(add_proverb=None, delete_proverb=None):
    oc = OpenCC(conversion="t2s")
    out_file_path = os.path.join(simplifiedChinese_out_dir, "proverb.txt")
    res = []
    res_shortcut = []
    with open(simplifiedChineseProverbPath, 'r', encoding='utf-8') as proverbFile:
        for proverb_tradition in proverbFile:
            proverb_tradition = proverb_tradition.strip()
            proverb = oc.convert(proverb_tradition)
            pinyin = lazy_pinyin(proverb)
            pinyinAbbr = getPinyinAbbreviation(pinyin)
            line = proverb + " " + freq1 + " " + freq2 + " " + pinyinAbbr + "\n"
            res.append(line)
            line3 = pinyinAbbr + "\t" + isNotAWord + "\t" + freq1 + "\t" + proverb + "\t" + freq2 + "\n"
            res_shortcut.append(line3)

    res = set(res) - set(delete_proverb)
    res = res.union(set(add_proverb))

    if isModify:
        for item in delete_proverb:
            items = item.strip().split(" ", maxsplit=4)
            delete_line = items[3] + "\t" + isNotAWord + "\t" + freq1 + "\t" + items[0] + "\t" + freq2 + "\n"
            if delete_line in res_shortcut:
                res_shortcut.remove(delete_line)
            else:
                print(delete_line)

        for item in add_proverb:
            items = item.strip().split(" ", maxsplit=4)
            add_line = items[3] + "\t" + isNotAWord + "\t" + freq1 + "\t" + items[0] + "\t" + freq2 + "\n"
            res_shortcut.append(add_line)

    with open(out_file_path, 'w', encoding='utf-8') as out_file:
        out_file.writelines(res)
    print("谚语 size:", str(len(res_shortcut)))
    return res_shortcut


def getHotword(add_hotword=None, delete_hotword=None):
    out_file_path = os.path.join(simplifiedChinese_out_dir, "hotword.txt")
    res = []
    res_shortcut = []
    count = 0
    with open(simplifiedChineseHotwordPath, 'r', encoding='utf-8') as hotwordFile:
        for hotword in hotwordFile:
            count += 1
            if count == 1:
                continue
            hotword = hotword.split("\t")[1].strip()
            pinyin = lazy_pinyin(hotword)
            pinyinAbbr = getPinyinAbbreviation(pinyin)
            line = hotword + " " + freq1 + " " + freq2 + " " + pinyinAbbr + "\n"
            res.append(line)
            line3 = pinyinAbbr + "\t" + isNotAWord + "\t" + freq1 + "\t" + hotword + "\t" + freq2 + "\n"
            res_shortcut.append(line3)

    res = set(res) - set(delete_hotword)
    res = res.union(set(add_hotword))

    if isModify:
        for item in delete_hotword:
            items = item.strip().split(" ", maxsplit=4)
            delete_line = items[3] + "\t" + isNotAWord + "\t" + freq1 + "\t" + items[0] + "\t" + freq2 + "\n"
            if delete_line in res_shortcut:
                res_shortcut.remove(delete_line)
            else:
                print(delete_line)

        for item in add_hotword:
            items = item.strip().split(" ", maxsplit=4)
            add_line = items[3] + "\t" + isNotAWord + "\t" + freq1 + "\t" + items[0] + "\t" + freq2 + "\n"
            res_shortcut.append(add_line)

    with open(out_file_path, 'w', encoding='utf-8') as out_file:
        out_file.writelines(res)
    print("热词 size:", str(len(res_shortcut)))
    return res_shortcut


def getModifyList():
    # 读取需要修改的词，并进行拼接  格式：类别 句子  100  1 拼音
    add_path = simplifiedChineseModifyPath + "simplified_add.tsv"
    delete_path = simplifiedChineseModifyPath + "simplified_delete.tsv"
    add_idiom, add_xiehouyu, add_poetry, add_proverb, add_hotword = [], [], [], [], []
    delete_idiom, delete_xiehouyu, delete_poetry, delete_proverb, delete_hotword = [], [], [], [], []

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
                if items[0] == "xiehouyu":
                    add_index = "xiehouyu"
                    add_xiehouyu.append(items[1])
                elif items[0] == "hotword":
                    add_index = "hotword"
                    add_hotword.append(items[1])
                elif items[0] == "proverb":
                    add_index = "proverb"
                    add_proverb.append(items[1])
                elif items[0] == "idiom":
                    add_index = "idiom"
                    add_idiom.append(items[1])
                elif items[0] == "poetry":
                    add_index = "poetry"
                    add_poetry.append(items[1])
            elif len(items) == 1 and items[0] != "":
                if add_index == "idiom":
                    add_idiom.append(items[0])
                elif add_index == "xiehouyu":
                    add_xiehouyu.append(items[0])
                elif add_index == "poetry":
                    add_poetry.append(items[0])
                elif add_index == "proverb":
                    add_proverb.append(items[0])
                elif add_index == "hotword":
                    add_hotword.append(items[0])
    with open(delete_path, 'r', encoding='utf-8') as delete_file:
        count = 0
        for line in delete_file:
            count += 1
            if count == 1:
                continue
            items = [item.strip() for item in line.strip().split("\t")]

            if len(items) == 2:
                if items[0] == "xiehou":
                    delete_index = "xiehou"
                    delete_xiehouyu.append(items[1])
                elif items[0] == "hotword":
                    delete_index = "hotword"
                    delete_hotword.append(items[1])
                elif items[0] == "proverb":
                    delete_index = "proverb"
                    delete_proverb.append(items[1])
                elif items[0] == "idiom":
                    delete_index = "idiom"
                    delete_idiom.append(items[1])
                elif items[0] == "poetry":
                    delete_index = "poetry"
                    delete_poetry.append(items[1])
            elif len(items) == 1 and items[0] != "":
                if delete_index =="idiom":
                    delete_idiom.append(items[0])
                elif delete_index == "xiehou":
                    delete_xiehouyu.append(items[0])
                elif delete_index == "poetry":
                    delete_poetry.append(items[0])
                elif delete_index == "proverb":
                    delete_proverb.append(items[0])
                elif delete_index == "hotword":
                    delete_hotword.append(items[0])

    print(len(add_idiom), len(add_xiehouyu), len(add_poetry), len(add_proverb), len(add_hotword),
        len(delete_idiom), len(delete_xiehouyu), len(delete_poetry), len(delete_proverb), len(delete_hotword))
    return add_idiom, add_xiehouyu, add_poetry, add_proverb, add_hotword,\
           delete_idiom, delete_xiehouyu, delete_poetry, delete_proverb, delete_hotword


if __name__ == "__main__":
    # 返回各个需要修改的类型的内容拼接
    if isModify == True:
        add_idiom, add_xiehouyu, add_poetry, add_proverb, add_hotword, \
        delete_idiom, delete_xiehouyu, delete_poetry, delete_proverb, delete_hotword = getModifyList()


    #  执行单个词的文件  返回 jianti + "\t" + true + "\t" + 100 + "\t" + pinyin + "\t" + 1 + "\n"
    word_shortcut = getWord()
    # 返回成语 首字母拼接 true 100 单词 1
    idiom_shortcut = getIdiom(add_idiom, delete_idiom)

    xiehouyu_bigram, xiehouyu_shortcut = getXiehouyu(add_xiehouyu, delete_xiehouyu)
    poetry_bigram, poetry_shortcut = getPoetry(add_poetry, delete_poetry)
    hotword_shortcut = getHotword(add_hotword, delete_hotword)
    proverb_shortcut = getProverb(add_proverb, delete_proverb)

    unigram_out_file_path = os.path.join(simplifiedChinese_out_dir, "unigram.txt")
    bigram_out_file_path = os.path.join(simplifiedChinese_out_dir, "bigram.txt")
    shortcut_out_file_path = os.path.join(simplifiedChinese_out_dir, "shortcut.txt")

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
        bigram_file.writelines(xiehouyu_bigram)
        bigram_file.writelines(poetry_bigram)
    with open(shortcut_out_file_path, 'a', encoding='utf-8') as shortcut_file:
        shortcut_file.writelines(word_shortcut)
        shortcut_file.writelines(idiom_shortcut)
        shortcut_file.writelines(xiehouyu_shortcut)
        shortcut_file.writelines(poetry_shortcut)
        shortcut_file.writelines(hotword_shortcut)
        shortcut_file.writelines(proverb_shortcut)

    print("Finished!")
