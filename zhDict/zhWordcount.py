import re
import sys

file = sys.argv[1]
# file_out = sys.argv[2]
wordcount = {}
letter = set()
regex = re.compile('[0-9]')
regex_letter = re.compile('[a-z\']')


def is_Chinese(word):
    for ch in word:
        if len(re.findall(regex, ch)) > 0:
            break
        if '\u4e00' <= ch <= '\u9fff':
            return True
    return False


with open(file, 'r', encoding='utf-8') as f_in:
    for l in f_in:
        words = l.strip().split('|#|')[1]
        for w in words.split('\t'):
            if is_Chinese(w):
                if w not in wordcount.keys():
                    wordcount[w] = 1
                else:
                    wordcount[w] += 1

with open(file.replace('.token', '.wordcount'), 'w', encoding='utf-8') as f_word:
    for l in sorted(wordcount.items(), key=lambda x: -int(x[1])):
        tuple = l[0] + '\t' + str(l[1])
        f_word.write(tuple.strip())
        f_word.write('\n')

