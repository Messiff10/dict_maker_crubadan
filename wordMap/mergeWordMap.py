
"""
合并不同时期的word_map
"""

old_word_map = "/Users/ff/Desktop/测评数据/文件合并/word_map.txt"
new_word_map = "/Users/ff/Desktop/测评数据/文件合并/ur_map_sort.txt"
merge_word_map = "/Users/ff/Desktop/测评数据/文件合并/word_map_sort_merge"
old_dict = {}
merge_dict = {}
with open(old_word_map, 'r', encoding='utf-8') as f_old:
    for line in f_old:
        words = line.strip().split('\t')
        word_wrong = words[0] + "\t" + words[1]
        if word_wrong not in old_dict.keys():
            old_dict[word_wrong] = words[2]
    # print(old_dict)
with open(new_word_map, 'r', encoding='utf-8') as f_new:
    with open(merge_word_map, 'w', encoding='utf-8') as f_out:
        for lines in f_new:
            words_new = lines.strip().split('\t')
            word_wrong_new = words_new[0] + "\t" + words_new[1]
            if word_wrong_new not in old_dict.keys():
                merge_dict[word_wrong_new] = words_new[2]
            else:
                # print(word_wrong_new)
                merge_dict[word_wrong_new] = old_dict[word_wrong_new]
        for sor in sorted(merge_dict.items(), key=lambda x: x[0]):
            f_out.write((sor[0] + "\t" + sor[1]).strip())
            f_out.write('\n')

print("finish line")
