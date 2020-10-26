import re
import sys
"""
统计短语词频
无词表对照
"""
regex = re.compile('\s+')
language = "en_US"
if language == "en_US":
    WORD_REGEX = re.compile(r"[^a-zA-Z']")
elif language == "it":
    WORD_REGEX = re.compile(r"[^qwertyuiìíopèéùúasdfghjklòóàzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM']")
elif language == "fi":
    WORD_REGEX = re.compile(r"[^abcdefghijklmnopqrstuvwxyzåäöABCDEFGHIJKLMNOPQRSTUVWXYZAÅÄOÖ']")
elif language == "tr":
    WORD_REGEX = re.compile(r"[^ertyuıopğüasdfghjklşizcvbnmöçERTYUIOPĞÜASDFGHJKLŞİZCVBNMÖÇ']")
elif language == "ru":
    WORD_REGEX = re.compile(r"[^йцукенгшщзхфывапролджэячсмитьбюЙЦУКЕНГШЩЗХФЫВАПРОЛДЖЭЯЧСМИТЬБЮ']")
elif language == "es":
    WORD_REGEX = re.compile(r"[^qwertyuiopasdfghjklñzxcvbnmQWERTYUIOPASDFGHJKLÑZXCVBNM']")
elif language == "es_US":
    WORD_REGEX = re.compile(r"[^qwertyuiopasdfghjklñzxcvbnmQWERTYUIOPASDFGHJKLÑZXCVBNM']")
elif language == "ms_MY":
    WORD_REGEX = re.compile(r"[^qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM']")
elif language == "pl":
    WORD_REGEX = re.compile(r"[^aąbcćdeęfghijklłmnńoóprsśtuwyzźżAĄBCĆDEĘFGHIJKLŁMNŃOÓPRSŚTUWYZŹŻ']")
elif language == "sv":
    WORD_REGEX = re.compile(r"[^abcdefghijklmnopqrstuvwxyzåäöABCDEFGHIJKLMNOPQRSTUVWXYZAÅÄOÖ']")
elif language == "th":
    WORD_REGEX = re.compile(
        r"[^\\u0E01\\u0E02\\u0E03\\u0E04\\u0E05\\u0E06\\u0E07\\u0E08\\u0E09\\u0E0A\\u0E0B\\u0E0C\\u0E0D\\u0E0E\\u0E0F\\u0E10\\u0E11\\u0E12\\u0E13\\u0E14\\u0E15\\u0E16\\u0E17\\u0E18\\u0E19\\u0E1A\\u0E1B\\u0E1C\\u0E1D\\u0E1E\\u0E1F\\u0E20\\u0E21\\u0E22\\u0E23\\u0E24\\u0E25\\u0E26\\u0E27\\u0E28\\u0E29\\u0E2A\\u0E2B\\u0E2C\\u0E2D\\u0E2E\\u0E2F\\u0E30\\u0E31\\u0E32\\u0E33\\u0E34\\u0E35\\u0E36\\u0E37\\u0E38\\u0E39\\u0E3A\\u0E3F\\u0E40\\u0E41\\u0E42\\u0E43\\u0E44\\u0E45\\u0E46\\u0E47\\u0E48\\u0E49\\u0E4A\\u0E4B\\u0E4C\\u0E4D\\u0E4E\\u0E4F\\u0E50\\u0E51\\u0E52\\u0E53\\u0E54\\u0E55\\u0E56\\u0E57\\u0E58\\u0E59\\u0E5A\\u0E5B']")
elif language == "ar":
    WORD_REGEX = re.compile(r"[^'ضصثقفغعهخحجشسيبلاتنمكطذءؤرىةوزظدئإأآڨڭپڢڤچ]")
elif language == "de":
    WORD_REGEX = re.compile(r"[^qwertzuiopüasdfghjklöäyxcvbnmßQWERTZUIOPÜASDFGHJKLÖÄYXCVBNMẞ']")
elif language == "da":
    WORD_REGEX = re.compile(r"[^qwertyuiopåasdfghjkløæzxcvbnmQWERTYUIOPÅASDFGHJKLØÆZXCVBNM']")
elif language == "nb":
    WORD_REGEX = re.compile(r"[^qwertyuiopåasdfghjkløæzxcvbnmQWERTYUIOPÅASDFGHJKLØÆZXCVBNM']")
count_dict = {}
phrasesdicte = {}

# s="wey miraiå si va a estar culo que no este chuy pero no vas a estar sola mmm vas a estar con jannia no we ? y con en max we de que vas a estar con alguien lo vas a estar we"
# words=regex.split(s)
# for w in range(0,len(words)):
#     if w+1<len(words):
#         if re.search(WORD_REGEX,words[w]) is None and re.search(WORD_REGEX,words[w+1]) is None:
#             phrase2=words[w]+" "+words[w+1]
#             # print(phrase2)
#             if phrase2 in phrasesdicte.keys():
#                 phrasesdicte[phrase2]=phrasesdicte[phrase2]+1.0
#             else:
#                 phrasesdicte[phrase2]=1.0
#     if w+2<len(words):
#         if re.search(WORD_REGEX,words[w]) is None and re.search(WORD_REGEX,words[w+1]) is None and re.search(WORD_REGEX,words[w+2]) is None:
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
with open(file_path, 'r', encoding='utf-8') as f_in:
    for line in f_in:
        words = regex.split(line.strip())
        for w in range(0, len(words)):
            if w + 1 < len(words):
                if re.search(WORD_REGEX, words[w]) is None and re.search(WORD_REGEX, words[w + 1]) is None:
                    phrase2 = words[w] + " " + words[w + 1]
                    # print(phrase2)
                    if phrase2 in phrasesdicte.keys():
                        phrasesdicte[phrase2] = phrasesdicte[phrase2] + 1
                    else:
                        # print(phrase2)
                        phrasesdicte[phrase2] = 1
            if w + 2 < len(words):
                if re.search(WORD_REGEX, words[w]) is None and re.search(WORD_REGEX,
                                                                         words[w + 1]) is None and re.search(WORD_REGEX,
                                                                                                             words[
                                                                                                                 w + 2]) is None:
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
    with open(file_path.replace('.txt', '.phrasecount_compare'), 'w', encoding='utf-8') as f_phrase:
        for l in count_list:
            s1 = str(l[0]) + "\t" + str(l[1])
            f_phrase.write(s1.strip())
            f_phrase.write('\n')
    f_phrase.close()
    f_in.close()
print("Finish line")
