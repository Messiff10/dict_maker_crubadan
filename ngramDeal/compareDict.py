bigram = "/Users/ff/Desktop/data/dict/input/en_US/en_US_bigram.txt"
trigram = "/Users/ff/Desktop/data/dict/input/en_US/en_US_trigram.txt"
trigram_out =  "/Users/ff/Desktop/data/dict/input/en_US/en_US_trigram_2.txt"


"""
比较二元词表和三元词表
"""

old_dict = {}
merge_dict = {}
with open(bigram, 'r', encoding='utf-8') as f_old:
    for line in f_old:
        words = line.strip().split('\t')
        word_wrong = words[0] + "\t" + words[1]
        if word_wrong not in old_dict.keys():
            old_dict[word_wrong] = words[2]
    # print(old_dict)
with open(trigram, 'r', encoding='utf-8') as f_new:
    with open(trigram_out, 'w', encoding='utf-8') as f_out:
        for lines in f_new:
            words_new = lines.strip().split('\t')
            word_wrong_new = words_new[0] + "\t" + words_new[1]
            if word_wrong_new in old_dict.keys():
                # merge_dict[word_wrong_new] = words_new[2]
                f_out.write(lines.strip())
                f_out.write('\n')
        #     else:
        #         # print(word_wrong_new)
        #         merge_dict[word_wrong_new] = old_dict[word_wrong_new]
        # for sor in sorted(merge_dict.items(), key=lambda x: x[0]):
        #     f_out.write((sor[0] + "\t" + sor[1]).strip())
        #     f_out.write('\n')

print("finish line")
