import os


# 从文件中读取所有unigram的词频，结果格式为{ word: freq }
def getUnigram(unigram_name):
# def getUnigram(language):
#     unigram_dir = "/Users/grace/data/dict/online_0_0/"
#     unigram_name = os.path.join(unigram_dir, language + ".txt")

    unigram = {}

    if not os.path.exists(unigram_name):
        print(unigram_name, "does not exists!")
        return unigram

    with open(unigram_name, 'r', encoding="utf-8") as unigram_file:
        for line in unigram_file:
            items = line.strip().split("\t")
            if len(items)==2:
                word = items[0].strip()
                freq = items[1].strip()
                unigram[word] = freq
            else:
                word = items[0].strip()
                unigram[word] = 0

    return unigram
def getVocab(unigram_name):
# def getUnigram(language):
#     unigram_dir = "/Users/grace/data/dict/online_0_0/"
#     unigram_name = os.path.join(unigram_dir, language + ".txt")

    unigram = {}

    if not os.path.exists(unigram_name):
        print(unigram_name, "does not exists!")
        return unigram

    with open(unigram_name, 'r', encoding="utf-8") as unigram_file:
        for line in unigram_file:
            items = line.strip().split("##")
            if len(items)==2:
                word = items[0].strip()
                freq = items[1].strip()
                unigram[word] = freq

    return unigram
