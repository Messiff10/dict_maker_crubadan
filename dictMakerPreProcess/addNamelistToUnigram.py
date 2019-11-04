from config.conf import languages

def getNameList(namelist_file_name, namelist_out_file_name):
    # 从namelist_file_name读取namelist写入namelist_out_file_name
    # namelist_out_file_name中的词符合词表格式：name \t freq

    freq_of_name = 1

    # count + count_candidate为总共添加的name行数
    count = 0
    count_candidate = 0
    res_name = []
    with open(namelist_file_name, 'r', encoding="utf-8") as namelist_file:
        for line in namelist_file:
            count += 1
            items = line.strip().split("\t")
            if len(items) == 1:
                word = items[0]
            elif len(items) == 2:
                # print(items[0])
                word = items[1]

            # 处理这样的情况，两个词都可以用来指Scotland：Scotland	أسكتلندا\أسكتلاندا
            candidates = word.split("\\")
            if len(candidates) != 1:
                # print(line)
                count_candidate += (len(candidates) - 1)
                for candidate in candidates:
                    candidate = candidate
            else:
                candidate = candidates[0]

            res_line = candidate + "\t" + str(freq_of_name) + "\n"
            res_name.append(res_line)

    with open(namelist_out_file_name, 'w', encoding="utf-8") as namelist_out_file:
        namelist_out_file.writelines(res_name)

    print("namelist size:" + str(count), "candidates size:", str(count_candidate))
    return res_name


# 以frequency为1给unigram添加namelist，此时unigram中没有任何name和emoji
if __name__ == "__main__":
    namelist_file_name = "/Users/grace/data/languages_from_intern/ar/WordlistofNameDictionary.tsv"
    namelist_out_file_name = "/Users/grace/data/dict/pack_from/namelist/ar.txt"

    namelist = getNameList(namelist_file_name, namelist_out_file_name)

    for language in languages:
        unigram_file_name = "/Users/grace/data/dict/pack_from/" + language + "/" + language + "_unigram.txt"

        # 给unigram文件之后append namelist
        # with open(unigram_file_name, 'a', encoding="utf-8") as unigram_file:
        #     unigram_file.writelines(namelist)

    print("Finished!")
