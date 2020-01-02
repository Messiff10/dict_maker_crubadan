import re
import sys
## 统计短语数，短语在词表中
regex = re.compile('\s+')
count_dict = {}
phrasesdicte = {}
true_words=set()
# word_true = "/Users/ff/Desktop/测评数据/转process/en_US_words_true"
# with open(word_true, 'r', encoding='utf-8') as f_true:
#     for line in f_true:
#         if line.strip() not in true_words:
#             true_words.add(line.strip())
# s="wey miraiå si va a estar culo que no este chuy I don't know pero no vas a estar sola mmm vas a estar con jannia no we ? y con en max we de que vas a estar con alguien lo vas a estar we"
# words=regex.split(s)
# for w in range(0,len(words)):
#     if w+1<len(words):
#         if words[w] in true_words and words[w+1] in true_words:
#             phrase2=words[w]+" "+words[w+1]
#             # print(phrase2)
#             if phrase2 in phrasesdicte.keys():
#                 phrasesdicte[phrase2]=phrasesdicte[phrase2]+1.0
#             else:
#                 phrasesdicte[phrase2]=1.0
#     if w+2<len(words):
#         if words[w] in true_words and words[w+1] in true_words and words[w+2] in true_words:
#             phrase3=words[w]+" "+words[w+1]+" "+words[w+2]
#             # print(phrase3)
#             if phrase3 in phrasesdicte.keys():
#                 phrasesdicte[phrase3]=phrasesdicte[phrase3]+1.0
#             else:
#                 phrasesdicte[phrase3]=1.0
# for di in phrasesdicte.keys():
#     print(di,phrasesdicte[di])
# print(len(phrasesdicte))

file_path = "/Users/ff/Desktop/测评数据/转process/en_US_user_web_case.txt"
word_true = "/Users/ff/Desktop/测评数据/转process/en_US_words_true"
true_words=set()
with open(word_true, 'r', encoding='utf-8') as f_true:
    for line in f_true:
        if line.strip() not in true_words:
            true_words.add(line.strip())
with open(file_path, 'r', encoding='utf-8') as f_in:
    for line in f_in:
        words = regex.split(line.strip())
        for w in range(0, len(words)):
            if w + 1 < len(words):
                if words[w] in true_words and words[w+1] in true_words :
                    phrase2 = words[w] + " " + words[w + 1]
                    # print(phrase2)
                    if phrase2 in phrasesdicte.keys():
                        phrasesdicte[phrase2] = phrasesdicte[phrase2] + 1
                    else:
                        # print(phrase2)
                        phrasesdicte[phrase2] = 1
            if w + 2 < len(words):
                if words[w] in true_words and words[w+1] in true_words and words[w+2] in true_words:
                    phrase3 = words[w] + " " + words[w + 1] + " " + words[w + 2]
                    # print(phrase3)
                    if phrase3 in phrasesdicte.keys():
                        phrasesdicte[phrase3] = phrasesdicte[phrase3] + 1
                    else:
                        # print(phrase3)
                        phrasesdicte[phrase3] = 1
        # 按照词频从高到低排列
    for phrase_3 in phrasesdicte.keys():
        phrases = regex.split(phrase_3)
        if len(phrases) == 3:
            phrases_2 = phrases[0] + " " + phrases[1]
            phrasesdicte[phrases_2] = phrasesdicte[phrases_2] - phrasesdicte[phrase_3]
    count_list = sorted(phrasesdicte.items(), key=lambda x: int(x[1]), reverse=True)
    with open(file_path.replace('.txt', '.phrase_true'), 'w', encoding='utf-8') as f_phrase:
        for l in count_list:
            s1 = str(l[0])
            f_phrase.write(s1.strip())
            f_phrase.write('\n')
    f_phrase.close()
    f_in.close()
print("Finish line")
