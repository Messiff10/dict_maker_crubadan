import os
## 测试ar_unigram
ar_unigram="/Users/ff/Desktop/data/unigram/ar_unigram"
def getUnigram(unigram_name):
# def getUnigram(language):
#     unigram_dir = "/Users/grace/data/dict/online_0_0/"
#     unigram_name = os.path.join(unigram_dir, language + ".txt")

    unigram = {}

    if not os.path.exists(unigram_name):
        print(unigram_name, "does not exists!")
        return unigram

    with open(unigram_name, 'r', encoding="utf-8") as unigram_file:
        for line in unigram_file:
            print("line:"+str(line))
            items = line.strip().split("\t")
            word = items[0].strip()
            freq = items[1].strip()
            unigram[word] = freq

    # return unigram

if __name__ == '__main__':
    getUnigram(ar_unigram)