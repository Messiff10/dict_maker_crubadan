from utils.is_emoji import is_emoji
import time


def selectEmojiFromRawCount():
    print("start at", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

    input_path = "/Users/grace/data/dict/raw/ar_unigram.txt"
    output_path = "/Users/grace/data/dict/raw/ar_unigram_emoji.txt"

    with open(input_path, 'r', encoding="utf-8") as inputfile:
        res = []
        for line in inputfile:
            items = line.split("\t")
            if is_emoji(items[0]):
                # print(line)
                res.append(line)

    with open(output_path, 'w', encoding="utf-8") as outputfile:
        outputfile.writelines(res)
    print("end at", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))


def selectEmojiFromUnigram():
    print("start at", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    languages = ["ar_standard", "ar_egyptian"]

    for language in languages:
        input_path = "/Users/grace/data/dict/pack_from/" + language + "/" + language + "_emoji_unigram.txt"
        output_path = "/Users/grace/data/dict/pack_from/" + language + "/" + language + "_emoji.txt"

        with open(input_path, 'r', encoding="utf-8") as inputfile:
            res = []
            for line in inputfile:
                items = line.split("\t")
                if is_emoji(items[0]):
                    print(line)
                    res.append(line)

        with open(output_path, 'w', encoding="utf-8") as outputfile:
            outputfile.writelines(res)

    print("start at", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))


if __name__ == "__main__":
    # selectEmojiFromRawCount()
    selectEmojiFromUnigram()
    print("Finished!")
