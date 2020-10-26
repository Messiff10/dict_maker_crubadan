from utils.is_emoji import is_emoji
from utils.reExpression import pattern_delete, getCharacterPattern
from utils.getUnigram import getUnigram
from config.conf import languages, scenes_names, scenes_ratios, priority, addNoise, max_out_num, isPrint, dict_dir
import re
import os
import time
import numpy as np
from scipy.stats import entropy
"""
分析华为数据和字典的命中率
"""

def analyze_kl():
    # 不同语料间的KL距离
    print("languages", languages)
    print("scenes_names", scenes_names)

    word_im_twitter_fb_huawei_kaggle = {}

    input_file_dir = '/Users/grace/data/word/csv_from_spark/'

    for language in languages:
        characterPattern = getCharacterPattern(language)

        if addNoise:
            output_file_dir = '/Users/grace/data/word/runword/addNoise/'
        else:
            output_file_dir = '/Users/grace/data/word/runword/notAddNoise/'
        output_file_name = output_file_dir + priority + '/' + language + '.txt'

        if os.path.exists(output_file_name):
            print("remove", output_file_name)
            os.remove(output_file_name)

        count_line = 0
        count_outs = []
        for scene, scenes_ratio in zip(scenes_names, scenes_ratios):
            if scene == "im":
                word_kika_huawei_kaggle_index = 0
            elif scene == "twitter":
                word_kika_huawei_kaggle_index = 1
            elif scene == "facebook":
                word_kika_huawei_kaggle_index = 2
            elif scene == "twitter_huawei":
                word_kika_huawei_kaggle_index = 3
            elif scene == "twitter_kaggle":
                word_kika_huawei_kaggle_index = 4

            if isPrint:
                print("start processing", language, scene, "in", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

            if scene == "":
                input_file_name = input_file_dir + priority + '/' + language + '_.txt'
            else:
                input_file_name = input_file_dir + priority + '/' + language + '_' + scene + '_.txt'

            max_out_num_scene = max_out_num * scenes_ratio

            if not os.path.exists(input_file_name):
                print(input_file_name, "doesn't exists!")
                continue

            with open(input_file_name, 'r', encoding='utf-8') as input_file:
                count_out = 0
                for line in input_file:
                    line = re.sub(pattern_delete, "", line).lower()  # 删除某些符号
                    words = line.strip().strip('"').split(' ')
                    has_emoji = False
                    for word in words:
                        if is_emoji(word):
                            has_emoji = True
                            break
                    if has_emoji:
                        continue
                    isNoCharacter = re.search(characterPattern, line)
                    if isNoCharacter:
                        continue
                    count_line += 1
                    for word in words:
                        if word in word_im_twitter_fb_huawei_kaggle:
                            word_im_twitter_fb_huawei_kaggle[word][word_kika_huawei_kaggle_index] += 1
                        else:
                            word_im_twitter_fb_huawei_kaggle[word] = [0, 0, 0, 0, 0]
                            word_im_twitter_fb_huawei_kaggle[word][word_kika_huawei_kaggle_index] = 1

                        count_out += 1

                    if count_out >= max_out_num_scene:
                        break
                count_outs.append(count_out)
                print(scene, count_out)

        epsilon = 1e-2
        values = np.array(list(word_im_twitter_fb_huawei_kaggle.values())) + epsilon
        im = values[:, 0]
        twitter = values[:, 1]
        fb = values[:, 2]
        huawei = values[:, 3]
        kaggle = values[:, 4]

        kl_im_twitter = (entropy(im, twitter) + entropy(twitter, im)) / 2
        kl_im_fb = (entropy(im, fb) + entropy(fb, im)) / 2
        kl_fb_twitter = (entropy(fb, twitter) + entropy(twitter, fb)) / 2

        kl_kika_huawei = (entropy(twitter, huawei) + entropy(huawei, twitter)) / 2
        kl_kika_kaggle = (entropy(twitter, kaggle) + entropy(kaggle, twitter)) / 2
        kl_huawei_kaggle = (entropy(huawei, kaggle) + entropy(kaggle, huawei)) / 2

        print("word_kika_huawei_kaggle:\t", word_im_twitter_fb_huawei_kaggle)
        print("im:\t", im)
        print("twitter:\t", twitter)
        print("fb:\t", fb)
        print("kaggle:\t", kaggle)
        print("huawei:\t", huawei)

        print("kl_im_twitter", kl_im_twitter,
              "\nkl_im_fb:", kl_im_fb,
              "\nkl_fb_twitter:", kl_fb_twitter,
              "\nkl_kika_huawei", kl_kika_huawei,
              "\nkl_kika_kaggle:", kl_kika_kaggle,
              "\nkl_huawei_kaggle:", kl_huawei_kaggle)
        print("language:", language, "\tcount_line:", count_line,
              "\tcount_out:", count_outs, "\tlen of words:", str(len(word_im_twitter_fb_huawei_kaggle)),
              "\tin", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))


        # uniform = [1] * 30000
        #
        # range_ = np.arange(30000) + epsilon
        # print((entropy(range_, uniform) + entropy(uniform, range_)) / 2)
        #
        # range_ = np.r_[np.arange(25000), np.zeros(5000)] + epsilon
        # print((entropy(range_, uniform) + entropy(uniform, range_)) / 2)
        #
        # range_ = np.r_[np.arange(20000), np.zeros(10000)] + epsilon
        # print((entropy(range_, uniform) + entropy(uniform, range_)) / 2)
        #
        # range_ = np.r_[np.ones(5000), np.zeros(25000)] + epsilon
        # print((entropy(range_, uniform) + entropy(uniform, range_)) / 2)
        #
        # range_ = np.r_[np.ones(10000), np.zeros(20000)] + epsilon
        # print((entropy(range_, uniform) + entropy(uniform, range_)) / 2)


# 分析华为给的语料中的词的分布：出现在所有语料中的词在不同语料（kika, huawei, kaggle）中的频率，计算KL距离
# 1. 词的总个数
# 2. 不在词表中的词的个数
# 3.
def analyze_wordInVocabRatio():
    # 语料库的位置
    # huawei_Facebook 13
    # huawei_Twitter 12
    # huawei_web 8
    # Kika_Facebook 13
    # Kika_IM 7
    data_dir = "/Users/ff/Desktop/data/scenes_language/3/huawei_Facebook/"
    # data_dir = "/Users/xm/data/word/runword/notAddNoise/scenes/1/"
    # data_dir = "/Users/grace/data/word/runword/notAddNoise/scenes/1/"
    # data_dir = "/Users/grace/data/word/runword/notAddNoise/1/"
    # print("--------------")
    for file in os.listdir(data_dir):
        # print(file)
        if os.path.isdir(file) or file.endswith("Store") or file.endswith("tok"):
            continue

        if file.endswith("-facebook.tsv"):
            language = file[:-13]  # kika_im,华为
            scene = "huawei_Facebook"
        elif file.endswith("-twitter.tsv"):
            language = file[:-12]  # kika_facebook
            scene = "huawei_Twitter"
        elif file.endswith("-web.tsv"):
            language = file[:-8]
            scene = "huawei_web"
        elif file.endswith("_facebook.txt"):
            language = file[:-13]
            scene = "Kika_Facebook"
        elif file.endswith("_im.txt"):
            language = file[:-7]
            scene = "Kika_IM"
        # language = file[:-13]  # 华为

        # print(language)
        # language = file[:-4]  # kika
        #print(language)
        languages_huawei = ["es_us","es_la","ar","it","nl","cs","ru","fr","en_us","de","es_es","es","en_uk","en_gb","pl","tr","ur",
                                    "ro","fa","uk","pt","ms","ph","pt_pt","ms_my","tl","hu",
                                    "th","fi","vi","vn","sv","kz","kk","da","no","nb","thl"]
        # languages_huawei = ["en_US"]
        if language.lower() not in languages_huawei:
            continue

        dict_file_path = dict_dir + language.lower() + "_unigram"
        dict_lang = getUnigram(dict_file_path)

        count_all = 0
        count_inVocab = 0
        # with open(os.path.join(data_dir, file), 'r', encoding='utf-8') as data_file:
        #     # data = data_file.read()
        #     # print(data)
        #     # print(data.strip())
        #     # print(data.strip().split(" "))
        #     for word in data_file.read().strip().strip('"').split(" "):
        #         count_all += 1
        #         if word in dict_lang:
        #             count_inVocab += 1
        with open(os.path.join(data_dir, file), 'r', encoding='utf-8') as data_file:
            data = [word for item in data_file.read().strip().strip('"').split(" ") for word in item.split("\n")]
            for word in data:
                if word != "":
                    count_all += 1
                    if word in dict_lang:
                        count_inVocab += 1

        wordInVocaRatio = count_inVocab / count_all
        print("language:", language, "\tcount_all:", str(count_all),
              "\tcount_inVocab:", str(count_inVocab), "\twordInVocaRatio:", str(wordInVocaRatio))



if __name__ == "__main__":
    analyze_wordInVocabRatio()

    # analyze_kl()
    print("Finished!")
