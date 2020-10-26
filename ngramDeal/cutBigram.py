"""
二元词表处理
每组词保留5个
"""

file = open("/Users/ff/Desktop/data/dict/input/da/da_bigram.txt", 'r', encoding='utf-8')
file_out = open("/Users/ff/Desktop/data/dict/input/da/da_bigram_cut.txt", 'w', encoding='utf-8')
# count = 0
result = {}
with open("/Users/ff/Desktop/data/dict/input/da/da_bigram.txt", 'r', encoding='utf-8') as f_in:
    for l in f_in:
        uni, big, freq = l.strip().split('\t')

        if uni in result.keys() and result[uni] < 5:
            # print(result[uni])
            # print(l)
            result[uni] = result[uni] + 1
            file_out.write(l.strip())
            file_out.write('\n')
        elif uni not in result.keys():
            file_out.write(l.strip())
            file_out.write('\n')
            result[uni] = 1
# file.close()
