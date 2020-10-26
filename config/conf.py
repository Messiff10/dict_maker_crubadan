isPrint = False  # 是否打印细节
"""
主要是测评语料配置
"""
priority = '1'  # 语言优先级
max_out_num = 30000  # 需要3w个词

# 第一优先级
languages = ["es_SA"]


# scenes_names可以为"", "communication", "social", "browser", "facebook", "twitter"
scenes_names = ["im", "facebook", "twitter", "twitter_huawei", "twitter_kaggle"]
scenes_ratios = [0.4, 0.1, 0.1, 0.4, 0.4]
# scenes_names = ["im", "facebook"]
# scenes_ratios = [0.4, 0.2]
scenes_names = ["web", "facebook", "im","twitter"]
scenes_ratios = [0.2, 0.2, 0.4,0.2]
# scenes_names = ["im", "facebook"]  # s0.70
# scenes_ratios = [0.4, 0.1]
# scenes_names = ["twitter","web"]   # 0.75
# scenes_ratios = [0.2,0.2]
# scenes_names = ["im"]
# scenes_ratios = [0.4]
# scenes_names = ["facebook"] # 0.7
# scenes_ratios = [0.2]
# scenes_names = ["web"] # 0.75
# scenes_ratios = [0.2]



# 按照word_map中的概率在语料中加入噪声
addNoise = False  # True  #

# 清洗语料比例

filterWordThreshold = 0.70
# 是否去除不在字符集中的句子
ifRemoveNoCharacter = True  # False  #

# 词表相关配置
maxLenInVoca = 10  # 大于128的词可以直接删除
# 词典位置
dict_dir = "/Users/ff/Desktop/data/unigram/"
dict_dir_2w = "/Users/ff/Desktop/data/vocab_words/"
