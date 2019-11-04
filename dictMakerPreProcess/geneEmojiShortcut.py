from config.conf import languages


# 此时unigram中有部分emoji频率，其中没有的emoji频率设为1
# 生成shortcut文件，格式为：airplane \t true \t 13(emoji频率) \t ✈ \t 14
def geneEmojiShortcut():
    all_emoji_file_path = "/Users/grace/data/languages_from_intern/ar/Emoji.tsv"
    emoji_description = {}
    with open(all_emoji_file_path, "r", encoding="utf-8") as all_emoji_file:
        print("reading", all_emoji_file_path)
        count = 0
        for line in all_emoji_file:
            count += 1
            if count == 1:  # 忽略第一行
                continue
            items = line.split("\t")
            emoji = items[1].strip()
            descriptions = [item.strip() for item in items[3].strip().split(",")]  # 每行中emoji可能有多种描述，用","分隔
            if emoji in emoji_description:  # 有些emoji有多行描述
                # print(emoji)
                emoji_description[emoji] = emoji_description[emoji] + descriptions
            else:
                emoji_description[emoji] = descriptions

    print("emoji_description size:", len(emoji_description))

    emoji_freq_file_path_dir = "/Users/grace/data/dict/pack_from/"
    for language in languages:
        print("\nstart processing", language)
        emoji_freq_file_path = emoji_freq_file_path_dir + language + "/" + language + "_unigram_only_emoji.txt"
        out_file_path = emoji_freq_file_path_dir + language + "/" + language + "_emoji_shortcut.txt"

        emoji_freq = {}
        with open(emoji_freq_file_path, "r", encoding="utf-8") as emoji_freq_file:
            for line in emoji_freq_file:
                items = line.split("\t")
                emoji = items[0].strip()
                freq = items[1].strip()
                emoji_freq[emoji] = freq
        print("emoji_freq size:", str(len(emoji_freq)))

        all_descriptions = {}
        freq_of_unk_emoji = "1"
        isNotAWord = "true"
        shortcutTargetfreq = "14"
        for emoji in emoji_description:
            for description in emoji_description[emoji]:
                if emoji in emoji_freq:
                    cur_freq = emoji_freq[emoji]
                else:
                    cur_freq = freq_of_unk_emoji

                if description in all_descriptions:
                    freq = all_descriptions[description].split("\t")[2]

                    # 让频率高的emoji更容易出现。有可能这个单词对应了两个不同的emoji，一个频率高一个频率低，都用高的那个来算
                    if freq > cur_freq:
                        continue

                res_item = description + "\t" \
                           + isNotAWord + "\t" \
                           + cur_freq + "\t"\
                           + emoji + "\t" \
                           + shortcutTargetfreq + "\n"
                all_descriptions[description] = res_item

        with open(out_file_path, "w", encoding="utf-8") as out_file:
            print("writing", out_file_path, "\tsize:", len(all_descriptions))
            out_file.writelines(all_descriptions.values())


if __name__ == "__main__":
    geneEmojiShortcut()

    print("Finished!")
