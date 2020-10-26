import os
import random
import re
import sys
import shutil
"""
python版本生成训练数据，速度较慢
目前不用 使用java
"""
# language = sys.argv[1]
language="nb"
if language == 'en_US':
    WORD_REGEX = re.compile(r"[a-zA-Z']+")
    NUM_REGEX = re.compile(r"[^\[+-]*[0-9]+.*[0-9]]*")
    PUN_REREX = re.compile(r"[^a-zA-Z0-9']")
elif language == 'es_US':
    WORD_REGEX = re.compile(r"[qwertyuiopasdfghjklñzxcvbnmQWERTYUIOPASDFGHJKLÑZXCVBNM']+")
    NUM_REGEX = re.compile(r"[^\[+-]*[0-9]+.*[0-9]]*")
    PUN_REREX = re.compile(r"[^qwertyuiopasdfghjklñzxcvbnmQWERTYUIOPASDFGHJKLÑZXCVBNM0-9']")
elif language == 'sv':
    WORD_REGEX = re.compile(r"[abcdefghijklmnopqrstuvwxyzåäöABCDEFGHIJKLMNOPQRSTUVWXYZAÅÄOÖ']+")
    NUM_REGEX = re.compile(r"[^\[+-]*[0-9]+.*[0-9]]*")
    PUN_REREX = re.compile(r"[^abcdefghijklmnopqrstuvwxyzåäöABCDEFGHIJKLMNOPQRSTUVWXYZAÅÄOÖ0-9']")
elif language == 'de':
    WORD_REGEX = re.compile(r"[qwertzuiopüasdfghjklöäyxcvbnmßQWERTZUIOPÜASDFGHJKLÖÄYXCVBNMẞ']+")
    NUM_REGEX = re.compile(r"[^\[+-]*[0-9]+.*[0-9]]*")
    PUN_REREX = re.compile(r"[^qwertzuiopüasdfghjklöäyxcvbnmßQWERTZUIOPÜASDFGHJKLÖÄYXCVBNMẞ0-9']")
elif language == 'ms_MY':
    WORD_REGEX = re.compile(r"[qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM']+")
    NUM_REGEX = re.compile(r"[^\[+-]*[0-9]+.*[0-9]]*")
    PUN_REREX = re.compile(r"[^qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0-9']")
elif language == 'nb':
    WORD_REGEX = re.compile(r"[qwertyuiopåasdfghjkløæzxcvbnmQWERTYUIOPÅASDFGHJKLØÆZXCVBNM']+")
    NUM_REGEX = re.compile(r"[^\[+-]*[0-9]+.*[0-9]]*")
    PUN_REREX = re.compile(r"[^qwertyuiopåasdfghjkløæzxcvbnmQWERTYUIOPÅASDFGHJKLØÆZXCVBNM0-9']")
elif language == 'da':
    WORD_REGEX = re.compile(r"[qwertyuiopåasdfghjkløæzxcvbnmQWERTYUIOPÅASDFGHJKLØÆZXCVBNM']+")
    NUM_REGEX = re.compile(r"[^\[+-]*[0-9]+.*[0-9]]*")
    PUN_REREX = re.compile(r"[^qwertyuiopåasdfghjkløæzxcvbnmQWERTYUIOPÅASDFGHJKLØÆZXCVBNM0-9']")
elif language == 'th':
    WORD_REGEX = re.compile(r"[\\u0E01\\u0E02\\u0E03\\u0E04\\u0E05\\u0E06\\u0E07\\u0E08\\u0E09" +
                            "\\u0E0A\\u0E0B\\u0E0C\\u0E0D\\u0E0E\\u0E0F\\u0E10\\u0E11\\u0E12\\u0E13\\u0E14\\u0E15\\u0E16\\u0E17" +
                            "\\u0E18\\u0E19\\u0E1A\\u0E1B\\u0E1C\\u0E1D\\u0E1E\\u0E1F\\u0E20\\u0E21\\u0E22\\u0E23\\u0E24\\u0E25" +
                            "\\u0E26\\u0E27\\u0E28\\u0E29\\u0E2A\\u0E2B\\u0E2C\\u0E2D\\u0E2E\\u0E2F\\u0E30\\u0E31\\u0E32\\u0E33" +
                            "\\u0E34\\u0E35\\u0E36\\u0E37\\u0E38\\u0E39\\u0E3A\\u0E3F\\u0E40\\u0E41\\u0E42\\u0E43\\u0E44\\u0E45" +
                            "\\u0E46\\u0E47\\u0E48\\u0E49\\u0E4A\\u0E4B\\u0E4C\\u0E4D\\u0E4E\\u0E4F\\u0E50\\u0E51\\u0E52\\u0E53" +
                            "\\u0E54\\u0E55\\u0E56\\u0E57\\u0E58\\u0E59\\u0E5A\\u0E5B']+")
    NUM_REGEX = re.compile(r"[^\[+-]*[0-9]+.*[0-9]]*")
    PUN_REREX = re.compile(r"[^\\u0E01\\u0E02\\u0E03\\u0E04\\u0E05\\u0E06\\u0E07\\u0E08\\u0E09" +
                           "\\u0E0A\\u0E0B\\u0E0C\\u0E0D\\u0E0E\\u0E0F\\u0E10\\u0E11\\u0E12\\u0E13\\u0E14\\u0E15\\u0E16\\u0E17" +
                           "\\u0E18\\u0E19\\u0E1A\\u0E1B\\u0E1C\\u0E1D\\u0E1E\\u0E1F\\u0E20\\u0E21\\u0E22\\u0E23\\u0E24\\u0E25" +
                           "\\u0E26\\u0E27\\u0E28\\u0E29\\u0E2A\\u0E2B\\u0E2C\\u0E2D\\u0E2E\\u0E2F\\u0E30\\u0E31\\u0E32\\u0E33" +
                           "\\u0E34\\u0E35\\u0E36\\u0E37\\u0E38\\u0E39\\u0E3A\\u0E3F\\u0E40\\u0E41\\u0E42\\u0E43\\u0E44\\u0E45" +
                           "\\u0E46\\u0E47\\u0E48\\u0E49\\u0E4A\\u0E4B\\u0E4C\\u0E4D\\u0E4E\\u0E4F\\u0E50\\u0E51\\u0E52\\u0E53" +
                           "\\u0E54\\u0E55\\u0E56\\u0E57\\u0E58\\u0E59\\u0E5A\\u0E5B0-9']")
elif language == 'ar':
    WORD_REGEX = re.compile(r"['ضصثقفغعهخحجشسيبلاتنمكطذءؤرىةوزظدئإأآڨڭپڢڤچ]+")
    NUM_REGEX = re.compile(r"[^\[+-]*[0-9]+.*[0-9]]*")
    PUN_REREX = re.compile(r"[^'ضصثقفغعهخحجشسيبلاتنمكطذءؤرىةوزظدئإأآڨڭپڢڤچ٠0١1٢2٣3٤4٥5٦6٧7٨8٩9]")
elif language == 'fi':
    WORD_REGEX = re.compile(r"[abcdefghijklmnopqrstuvwxyzåäöABCDEFGHIJKLMNOPQRSTUVWXYZAÅÄOÖ']+")
    NUM_REGEX = re.compile(r"[^\[+-]*[0-9]+.*[0-9]]*")
    PUN_REREX = re.compile(r"[^abcdefghijklmnopqrstuvwxyzåäöABCDEFGHIJKLMNOPQRSTUVWXYZAÅÄOÖ0-9']")
elif language == 'it':
    WORD_REGEX = re.compile(r"[qwertyuiìíopèéùúasdfghjklòóàzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM']+")
    NUM_REGEX = re.compile(r"[^\[+-]*[0-9]+.*[0-9]]*")
    PUN_REREX = re.compile(r"[^qwertyuiìíopèéùúasdfghjklòóàzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0-9']")
elif language == 'ru':
    WORD_REGEX = re.compile(r"[йцукенгшщзхфывапролджэячсмитьбюЙЦУКЕНГШЩЗХФЫВАПРОЛДЖЭЯЧСМИТЬБЮ']+")
    NUM_REGEX = re.compile(r"[^\[+-]*[0-9]+.*[0-9]]*")
    PUN_REREX = re.compile(r"[^йцукенгшщзхфывапролджэячсмитьбюЙЦУКЕНГШЩЗХФЫВАПРОЛДЖЭЯЧСМИТЬБЮ0-9']")

elif language == 'tr':
    WORD_REGEX = re.compile(r"[ertyuıopğüasdfghjklşizcvbnmöçERTYUIOPĞÜASDFGHJKLŞİZCVBNMÖÇ']+")
    NUM_REGEX = re.compile(r"[^\[+-]*[0-9]+.*[0-9]]*")
    PUN_REREX = re.compile(r"[^ertyuıopğüasdfghjklşizcvbnmöçERTYUIOPĞÜASDFGHJKLŞİZCVBNMÖÇ0-9']")
elif language == 'pl':
    WORD_REGEX = re.compile(r"[aąbcćdeęfghijklłmnńoóprsśtuwyzźżAĄBCĆDEĘFGHIJKLŁMNŃOÓPRSŚTUWYZŹŻ']+")
    NUM_REGEX = re.compile(r"[^\[+-]*[0-9]+.*[0-9]]*")
    PUN_REREX = re.compile(r"[^aąbcćdeęfghijklłmnńoóprsśtuwyzźżAĄBCĆDEĘFGHIJKLŁMNŃOÓPRSŚTUWYZŹŻ0-9']")
SPLIT_FLAG = "##"
PAD_FLAG = "_PAD"
IN_EOS_FLAG = "<eos>"
OUT_EOS_FLAG = "<eos>"
NUM_FLAG = "<num>"
PUNCTUATION_FLAG = "<pun>"
EMOJI_FLAG = "<emoji>"
UNKNOWN_FLAG = "<unk>"
UNKNOWN_INDICT_FLAG = "<und>"
KEY_START_FLAG = "<start>"
NOT_PHRASE_FLAG = "<unp>"
PAD_ID = 0
IN_EOS_ID = 1
UNKNOWN_WORD_ID = 2
NUM_ID = 3
PUNCTUATION_ID = 4
EMOJI_ID = 5
UNKNOWN_LETTER_ID = 0
KEY_START_ID = 1
OUT_EOS_ID = 0
UNKNOWN_OUT_ID = 1
UNKNOWN_OUT_INDICT_ID = 2

linenum = 5185936
wordsNum = 20000
phraseNum = 20000
rateThreshold = 0.8
trainDataNum = 5155936
devDataNum = 10000
testDataNum = 10000
emojisSet = set()
regex = re.compile('\s+')
wordsCountMapFromVocab = {}
smallWordsDictMap = {}
dictLettersSet = []
bigWordsSet = []
dataLettersSet = set()
dataWordsSet = set()
dataOutWordSet = set()

wordIdMap = {}
letterIdMap = {}
outWordIdMap = {}


def loadEmojisSet(emojisFile):
    for emoji in open(emojisFile):
        emojis = regex.split(emoji.strip())
        if emojis[0] not in emojisSet:
            emojisSet.add(emojis[0])
    print("emoji size", len(emojisSet))


def combineWordsDict(wordsDictFile, wordvocabfile, lettervocabfile):
    # 读取一元词表
    for wordsFromVocab in open(wordsDictFile):
        wordsvocabs = regex.split(wordsFromVocab.strip())
        if wordsvocabs[0] in wordsCountMapFromVocab.keys():
            wordsCountMapFromVocab[wordsvocabs[0].strip()] = wordsCountMapFromVocab[wordsvocabs[0].strip()] + 1
        else:
            wordsCountMapFromVocab[wordsvocabs[0].strip()] = 1
    print("wordsCountMapFromVocab size", len(wordsCountMapFromVocab))
    # print(wordsCountMapFromVocab)
    # 读取在词表中的词频
    for smallDictMap in open(wordvocabfile):
        if smallDictMap in smallWordsDictMap.keys():
            smallWordsDictMap[smallDictMap.strip()] = 0
        else:
            smallWordsDictMap[smallDictMap.strip()] = 0
    print("smallWordsDictMap size", len(smallWordsDictMap))
    # print(smallWordsDictMap)
    # 读取字母表
    for lettersSet in open(lettervocabfile):
        dictLettersSet.append(lettersSet.strip())
    print("dictLettersSet size", len(dictLettersSet))
    # print(dictLettersSet)
    # 读取不在small中在大词表中
    for bigSet in wordsCountMapFromVocab.keys():
        if bigSet not in smallWordsDictMap.keys():
            bigWordsSet.append(str(bigSet).strip())
    print("bigWordsSet size", len(bigWordsSet))
    # print(bigWordsSet)


def convertData(dataPathIn, dataPathOut):

    traindata = open(dataPathOut + '/train_data', 'w')
    devdata = open(dataPathOut + '/dev_data', 'w')
    testdata = open(dataPathOut + '/test_data', 'w')

    rateTrain = float(trainDataNum / linenum)
    rateDev = float(devDataNum / linenum)
    rateTest = float(testDataNum / linenum)
    # print(rateTrain,rateDev,rateTest)
    for datapro in open(dataPathIn, 'r'):
        rand = random.random()
        # print(rand)
        letters = []
        words = []
        # train_data
        if rand < rateTrain:
            # print(datapro)
            lineSplit = datapro.split('|#|')
            # print(len(lineSplit))
            letterIn = lineSplit[0].split('\t')
            wordsIn = lineSplit[1].split('\t')
            wordNum = 0
            unknownWordNum = 0
            convertedWordsin = []
            convertedWordsout = []
            for word in wordsIn:
                if word in smallWordsDictMap.keys():
                    wordConverted = word
                    wordNum += 1
                elif word in emojisSet:
                    wordConverted = EMOJI_FLAG
                    wordNum += 1
                elif re.search(NUM_REGEX, word) is not None:
                    wordConverted = NUM_FLAG
                    unknownWordNum += 1
                elif re.search(PUN_REREX, word) is not None:
                    wordConverted = PUNCTUATION_FLAG
                    unknownWordNum += 1
                else:
                    wordConverted = UNKNOWN_FLAG
                    unknownWordNum += 1
                convertedWordsin.append(wordConverted)
            # print(wordNum,unknownWordNum)
            wordRate = float(wordNum / (wordNum + unknownWordNum))
            # print(wordRate)
            if wordRate >= rateThreshold:
                # print(datapro)
                wordNum = 0
                unknownWordNum = 0
                for word in wordsIn:
                    if word in smallWordsDictMap.keys():
                        wordConverted = word
                        wordNum += 1
                    elif word in bigWordsSet and word not in emojisSet:
                        wordConverted = UNKNOWN_INDICT_FLAG
                        wordNum += 1
                    else:
                        wordConverted = UNKNOWN_FLAG
                        unknownWordNum += 1
                    convertedWordsout.append(wordConverted)
                wordRate = float(wordNum / (wordNum + unknownWordNum))
                if wordRate >= rateThreshold:
                    for letter in letterIn:
                        singleletter = regex.split(letter)
                        for sl in singleletter:
                            if sl in dictLettersSet:
                                dataLettersSet.add(sl)
                            else:
                                dataLettersSet.add(UNKNOWN_FLAG)
                    for inWord in convertedWordsin:
                        dataWordsSet.add(inWord.strip())
                    for outWord in convertedWordsout:
                        dataOutWordSet.add(outWord)
                    # print(datapro)
                    traindata.write(datapro.strip())
                    traindata.write('\n')
        # dev_data
        elif rand < (rateTrain + rateDev):
            devdata.write(datapro.strip())
            devdata.write('\n')
        # test_data
        elif rand < (rateTrain + rateDev + rateTest):
            testdata.write(datapro.strip())
            testdata.write('\n')
        else:
            continue


def saveVocabFiles(dataPathOut):
    vocab_in_words = open(dataPathOut + '/vocab_in_words', 'w')
    vocab_out = open(dataPathOut + '/vocab_out', 'w')
    vocab_in_letters = open(dataPathOut + '/vocab_in_letters', 'w')

    wordIdMap[PAD_FLAG] = PAD_ID
    wordIdMap[IN_EOS_FLAG] = IN_EOS_ID
    wordIdMap[UNKNOWN_FLAG] = UNKNOWN_WORD_ID
    wordIdMap[NUM_FLAG] = NUM_ID
    wordIdMap[PUNCTUATION_FLAG] = PUNCTUATION_ID
    wordIdMap[EMOJI_FLAG] = EMOJI_ID

    letterIdMap[UNKNOWN_FLAG] = UNKNOWN_LETTER_ID
    letterIdMap[KEY_START_FLAG] = KEY_START_ID

    outWordIdMap[OUT_EOS_FLAG] = OUT_EOS_ID
    outWordIdMap[UNKNOWN_FLAG] = UNKNOWN_OUT_ID
    outWordIdMap[UNKNOWN_INDICT_FLAG] = UNKNOWN_OUT_INDICT_ID
    id = len(letterIdMap)
    # 字母表
    for letter in sorted(dataLettersSet):
        if letter not in letterIdMap.keys():
            letterIdMap[letter] = id
            id += 1
    # print(letterIdMap.keys())
    print("letterIdMap size", len(letterIdMap))

    # words && out
    idin = len(wordIdMap)
    idout = len(outWordIdMap)
    for word in smallWordsDictMap.keys():
        if word in dataWordsSet and len(wordIdMap) < wordsNum + 3 and (word not in wordIdMap.keys()):
            wordIdMap[word] = idin
            idin += 1
        if word in dataOutWordSet and len(outWordIdMap) < wordsNum + 6:
            outWordIdMap[word] = idout
            idout += 1
    print("wordIdMap size", len(wordIdMap))
    print("outWordIdMap size", len(outWordIdMap))

    for wordin in wordIdMap:
        vocab_in_words.write(wordin + '##' + str(wordIdMap[wordin]))
        vocab_in_words.write('\n')
    for wordout in outWordIdMap:
        vocab_out.write(wordout + '##' + str(outWordIdMap[wordout]))
        vocab_out.write('\n')
    for letters in letterIdMap:
        vocab_in_letters.write(letters + '##' + str(letterIdMap[letters]))
        vocab_in_letters.write('\n')


def convertToIdsFile(datapathIn, dataPathOutlm, dataPathOutletter):
    datapathIn = open(datapathIn, 'r')
    dataPathOutlm = open(dataPathOutlm, 'w')
    dataPathOutletter = open(dataPathOutletter, 'w')
    lineNums=0
    for line in datapathIn:
        inIdsArray = []
        outIdsArray = []
        lettersIdsArray = []
        letterswords = line.split('|#|')
        letters = letterswords[0].split('\t')
        words = letterswords[1].split('\t')
        if len(letters) != len(words):
            print("error line", line)
            continue
        if len(words) >= 2:
            inIdsArray.append(str(wordIdMap[IN_EOS_FLAG]))
            outIdsArray.append(str(outWordIdMap[OUT_EOS_FLAG]))
            lettersIdsArray.append(str(letterIdMap[KEY_START_FLAG]))
            for word in words:
                if word in wordIdMap.keys():
                    inIdsArray.append(str(wordIdMap[word]))
                elif word in emojisSet:
                    inIdsArray.append(str(wordIdMap[EMOJI_FLAG]))
                elif re.search(NUM_REGEX, word) is not None:
                    inIdsArray.append(str(wordIdMap[NUM_FLAG]))
                elif re.search(PUN_REREX, word) is not None:
                    inIdsArray.append(str(wordIdMap[PUNCTUATION_FLAG]))
                else:
                    inIdsArray.append(str(wordIdMap[UNKNOWN_FLAG]))

                if word in outWordIdMap.keys():
                    outIdsArray.append(str(outWordIdMap[word]))
                elif word in bigWordsSet and word not in emojisSet:
                    outIdsArray.append(str(outWordIdMap[UNKNOWN_INDICT_FLAG]))
                else:
                    outIdsArray.append(str(outWordIdMap[UNKNOWN_FLAG]))
            # 整合字母表转id
            # print(line)
            for letter in letters:
                letterId = str(letterIdMap[KEY_START_FLAG])
                if len(letter.strip()) != 0:
                    alpha = regex.split(letter.strip())
                    for al in alpha:
                        if al in letterIdMap.keys():
                            letterId = letterId + " " + str(letterIdMap[al])
                        else:
                            letterId = letterId + " " + str(letterIdMap[UNKNOWN_FLAG])
                lettersIdsArray.append(letterId)
            if len(lettersIdsArray) != 0 and len(inIdsArray) != 0 and len(outIdsArray) != 0:
                lineNums+=1
                dataPathOutlm.write(" ".join(inIdsArray) + "#" + " ".join(outIdsArray) + "\n")
                dataPathOutletter.write("#".join(lettersIdsArray) + "\n")
    print(datapathIn,lineNums)


def convertToIds(dataPathIn, dataPathOut):
    convertToIdsFile(dataPathIn + '/train_data', dataPathOut + '/train_in_ids_lm',
                     dataPathOut + '/train_in_ids_letters')
    convertToIdsFile(dataPathIn + '/dev_data', dataPathOut + '/dev_in_ids_lm', dataPathOut + '/dev_in_ids_letters')


if __name__ == '__main__':
    # s = sys.argv[2]
    # wordsDictFile = s + sys.argv[3]
    # emojisFile = s + sys.argv[4]
    # dataPathIn = s + sys.argv[5]
    # wordvocabfile = s + sys.argv[6]
    # lettervocabfile = s + sys.argv[7]
    # dataPathOut = s + sys.argv[8]
    s = "/Users/ff/Desktop/train_data/nb/nb_user_web_train/"
    wordsDictFile = s + "nb_unigram_null"
    emojisFile = s + "emojis_null"
    dataPathIn = s + "nb_user_web_pro.txt"
    wordvocabfile = s + "vocab_words_true"
    lettervocabfile = s + "vocab_letters"
    dataPathOut = s + "user_web_no_emoji_60"

    if os.path.exists(dataPathOut):
        print("remove", dataPathOut)
        shutil.rmtree(dataPathOut)
    os.mkdir(dataPathOut)


    loadEmojisSet(emojisFile)  # 读取表情
    combineWordsDict(wordsDictFile, wordvocabfile, lettervocabfile)  # 读取大词表，字母表
    convertData(dataPathIn, dataPathOut)
    saveVocabFiles(dataPathOut)
    convertToIds(dataPathOut, dataPathOut)
print("Finish Line")
# 参数1 语言编码
# 参数2 文件夹 带/
# 参数3 一元词表
# 参数4  emoji
# 参数5 process文件
# 参数6 对比为true文件
# 参数7 字母表
# 参数8 生成文件的文件夹名称 不带/