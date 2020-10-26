bigram = "/Users/ff/Desktop/speech_en.txt"
trigram = "/Users/ff/Desktop/vocab_out"
trigram_out = "/Users/ff/Desktop/speech_en_out.txt"

"""
词性标注 词表
"""

# aset=set()
old_dict = {}

merge_dict = {}
with open(bigram, 'r', encoding='utf-8') as f_old:
    for line in f_old:
        words = line.strip().split('----')
        ww = words[0]
        # word_wrong = words[0] + "\t" + words[1]
        if len(words) > 1:
            for w in range(1, len(words)):
                # print(ww, words[w])
                if ww in old_dict.keys() and words[w] not in old_dict[ww] and words[w].strip() is not "":
                    # print(old_dict, words[w])
                    old_dict[ww].append(words[w])
                    # old_dict[ww] = old_dict[ww].append(words[w])
                elif words[w].strip() is not "":
                    # print(old_dict)
                    # old_dict[ww] =set()
                    # aset.add(words[w])
                    old_dict[ww] = [words[w]]
    # print(old_dict)
count = 0
with open(trigram, 'r', encoding='utf-8') as f_new:
    with open(trigram_out, 'w', encoding='utf-8') as f_out:
        for lines in f_new:
            words_new = lines.strip().split('##')
            # print(len(words_new))
            if int(words_new[1]) > 2:
                # word_wrong_new = words_new[0] + "\t" + words_new[1]
                if words_new[0] in old_dict.keys():
                    result = lines.strip() + "\t" + "|".join(old_dict[words_new[0]])
                    f_out.write(result.strip())
                    f_out.write('\n')
                else:
                    if words_new[0].istitle() or words_new[0].replace("'s", "").istitle() or words_new[0].isupper() or \
                            words_new[0].replace("'s", "").isupper():
                        result = lines.strip() + "\t" + "n."
                        f_out.write(result.strip())
                        f_out.write('\n')
                    elif words_new[0].lower() in old_dict.keys():
                        result = lines.strip() + "\t" + "|".join(old_dict[words_new[0].lower()])
                        f_out.write(result.strip())
                        f_out.write('\n')
                    else:
                        count += 1
                        result = lines.strip() + "\t" + "unk"
                        f_out.write(result.strip())
                        f_out.write('\n')
            else:
                f_out.write(lines.strip())
                f_out.write('\n')

print("finish line", count)
