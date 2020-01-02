isPrint = False  # 是否打印细节

priority = '1'  # 语言优先级
max_out_num = 30000  # 需要3w个词

# 第一优先级
languages = ["es_MX", "es_US", "ar", "it", "nl", "cs", "ru", "fr", "en_US", "de", "es", "en_GB", "pl", "tr", "ur"]
# 第二优先级
# languages = ["ro", "fa", "uk", "pt_PT", "ms_MY", "tl", "hu"]
# 第三优先级
# languages = ["th", "fi", "vi", "sv", "kk", "da", "nb"]
# 第四优先级
# languages = ["hi", "sw", "my_MM", "bn", "iw", "ja", "el", "zh_HK", "sr", "sk", "be", "bg", "zh_TW", "hr", "lt", "si",
#              "sl", "mk", "ko", "km_KH", "am", "mn_MN", "ka_GE", "uz", "et_EE", "lv", "lo_LA", "ne", "in", "az", "pt_BR"]

# languages = ["ar", "it", "nl", "cs", "fr", "de", "es", "en_GB", "tr", "ur"]
# languages = ["hi", "bn", "in", "ne", "my_MM", "km_KH", "lo_LA"]

# languages = ["th"]
languages = ["hi","sw","my_MM","bn","iw","el","sr","sk","be",
             "bg","hr","lt","si","sl","mk","km_KH","am","ka_GE",
             "uz","et_EE","lv","lo_LA","ne","in","az","pt_BR","ta","kn","gu","te"]
languages = ["az","et_EE","gu","hr","in","ka_GE","lt","lv","pt_BR","sk","sl"]
languages = ["az","et_EE","gu","hr","ka_GE","lt","lv","pt_BR","sk","sl"]
# languages = ["es","en_US"]
#
languages = ["tr","ru","ms_MY","pl"]
# languages=["es_US"]
# languages = ["pl","it","ms_MY","de","es_US"]
# languages=["de","it","ms_MY","pl"]
languages=["ar","sv","fi","ru"]
languages=["da","nb"]


# scenes_names可以为"", "communication", "social", "browser", "facebook", "twitter"
scenes_names = ["im", "facebook", "twitter", "twitter_huawei", "twitter_kaggle"]
scenes_ratios = [0.4, 0.1, 0.1, 0.4, 0.4]
# scenes_names = ["im", "facebook"]
# scenes_ratios = [0.4, 0.2]
scenes_names = ["web", "twitter", "facebook", "im"]
scenes_ratios = [0.2, 0.2, 0.2, 0.4]
# filterWordThreshold = [0.75,0.75,0.7,0.7]
scenes_names = ["im","facebook"]  # 0.70
scenes_ratios = [0.4,0.1]
# scenes_names = ["twitter","web"]   # 0.75
# scenes_ratios = [0.2,0.2]
# scenes_names = ["im"]
# scenes_ratios = [0.4]
# scenes_names = ["facebook"] # 0.7
# scenes_ratios = [0.2]
# scenes_names = ["web"] # 0.75
# scenes_ratios = [0.2]
# scenes_ratios = [0.5, 0.5]
# scenes_ratios = [1, 1, 1, 1, 1]
# scenes_names = [""]
# scenes_ratios = [1]


# 按照word_map中的概率在语料中加入噪声
addNoise = False  # True  #

# 清洗语料比例

filterWordThreshold = 0.7
# 是否去除不在字符集中的句子
ifRemoveNoCharacter = True  # False  #

# 词表相关配置
maxLenInVoca = 10  # 大于128的词可以直接删除
# 词典位置
dict_dir = "/Users/ff/Desktop/data/unigram/"
dict_dir_2w = "/Users/ff/Desktop/data/vocab_words/"