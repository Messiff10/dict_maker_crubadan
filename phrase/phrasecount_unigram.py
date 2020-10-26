import re
import sys

"""
统计短语数，根据词表对照
"""
regex = re.compile('\s+')
count_dict = {}
phrasesdicte = {}

file_path = sys.argv[1]
word_true = sys.argv[2]
true_words = set()


def getTrue(word_true):
    with open(word_true, 'r', encoding='utf-8') as f_true:
        for line in f_true:
            if line.strip() not in true_words:
                true_words.add(line.strip())


def getPhrase(file_path):
    with open(file_path, 'r', encoding='utf-8') as f_in:
        for line in f_in:
            words = regex.split(line.strip())
            for w in range(0, len(words)):
                if w + 1 < len(words):
                    if words[w] in true_words and words[w + 1] in true_words:
                        phrase2 = words[w] + " " + words[w + 1]
                        # print(phrase2)
                        if phrase2 in phrasesdicte.keys():
                            phrasesdicte[phrase2] = phrasesdicte[phrase2] + 1
                        else:
                            # print(phrase2)
                            phrasesdicte[phrase2] = 1
                if w + 2 < len(words):
                    if words[w] in true_words and words[w + 1] in true_words and words[w + 2] in true_words:
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
        i = 0
        count_list = sorted(phrasesdicte.items(), key=lambda x: int(x[1]), reverse=True)
        with open(file_path.replace('.txt', '.phrase'), 'w', encoding='utf-8') as f_phrase:
            for l in count_list:
                if i < 50000:
                    i += 1
                    s1 = str(l[0])+"\t"+str(l[1])
                    f_phrase.write(s1.strip())
                    f_phrase.write('\n')
    print("Finish line")


if __name__ == '__main__':
    getTrue(word_true)
    getPhrase(file_path)
