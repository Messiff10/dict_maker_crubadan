from config.conf import languages, maxLenInVoca

src_path = "/Users/grace/data/dict/pack_from/"


def removelongword(src_path, languages):
    for language in languages:
        suffixs = ["_unigram.txt", "_bigram.txt"]
        for suffix in suffixs:
            file_path = src_path + language + "/" + language + suffix
            print("processing" + file_path + "...")
            res = []
            with open(file_path, 'r', encoding='utf-8') as f:
                for line in f:
                    items = line.split("\t")
                    for item in items:
                        isTooLong = False
                        if len(item.strip()) > maxLenInVoca:
                            print(len(item.strip()), ",", item, ",", line)
                            isTooLong = True
                            break
                    if not isTooLong:
                        res.append(line)

            with open(file_path, 'w', encoding='utf-8') as f:
                f.writelines(res)


removelongword(src_path, languages)
print("Finished!")
