"""
处理方言问题  将方言词表和其余词表合并 作为生成ngram的原始词表
"""

file_old = "/Users/ff/Desktop/es_US_unigram"
file_new = "/Users/ff/Desktop/es_unigram"
merge_file = "/Users/ff/Desktop/es_US_unigram_merge"
old = []
new = []
f_new = open(file_new, 'r', encoding='utf-8')
# with open(file_new, 'r', encoding='utf-8') as f_new:
for l_n in f_new:
    word_n = l_n.split('\t')[0]
    if word_n not in new:
        new.append(word_n)
f_new.close()
with open(file_old, 'r', encoding='utf-8') as f_old:
    for l_o in f_old:
        word_o = l_o.split('\t')[0]
        if word_o not in new:
            new.append(word_o)

with open(merge_file, 'w', encoding='utf-8') as f_out:
    for n in new:
        f_out.write(n.strip())
        f_out.write('\n')
