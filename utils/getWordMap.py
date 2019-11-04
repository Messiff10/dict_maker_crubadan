import os


# 从文件中读取所有单词的word_map，结果格式为{ desired_word: { keys: freq } }
def getWordMap(language):
    word_map_dir = "/Users/grace/data/word_map/"
    word_map_name = os.path.join(word_map_dir, language + ".txt")
    wordmap = {}
    with open(word_map_name, 'r', encoding="utf-8") as input_file:
        current_word = ""
        current_map = {}
        for line in input_file:
            items = line.split("\t")
            desired_word = items[0].strip()
            keys = items[1].strip()
            freq = items[2].strip()

            if keys == "":  # 推荐正确，直接空格上屏
                continue

            if current_word == desired_word:
                current_map[keys] = freq
            else:
                if current_word != "":
                    wordmap[current_word] = current_map

                current_word = desired_word
                current_map = {}
                current_map[keys] = freq

        wordmap[current_word] = current_map

    return wordmap
