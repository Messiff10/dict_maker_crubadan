# import random
#
# file = open("/Users/ff/Desktop/video/en_US_video_unigram_deal", 'r', encoding='utf-8')
# file_2 = open("/Users/ff/Desktop/video/video_rate.txt", 'r', encoding='utf-8')
# file_3 = open("/Users/ff/Desktop/video/all_video_rate_random.txt", 'w', encoding='utf-8')
# rates = {}
# # random.randint(1, 250)
# for l in file_2:
#     name, rate = l.strip().split('\t')
#     if name not in rates.keys():
#         rates[name] = rate
#         # file_3.write(l.strip())
#         # file_3.write('\n')
# for l2 in file:
#     name = l2.strip().split('\t')[0]
#     if name not in rates.keys():
#         rates[name] = str(random.randint(1, 200))
#         # result = name + '\t' +str(random.randint(1, 250))
#         # file_3.write(result.strip())
#         # file_3.write('\n')
# for temp in sorted(rates.items(), key=lambda x: -int(x[1])):
#     result = temp[0] + '\t' + temp[1]
#     file_3.write(result.strip())
#     file_3.write('\n')
# import re
#
# regex = re.compile('[0-9]')
#
#
# def is_Chinese(word):
#     for ch in word:
#         # print(ch)
#         if len(re.findall(regex,ch))>0:
#             break
#
#         if '\u4e00' <= ch <= '\u9fff':
#             return True
#     return False
#
#
# s = "中	新	经纬	客户	端	1月	1日	电	(	魏薇	薛宇飞	)	在	市场	期待	多日	后	，	2020年	第一	天	，	“	央妈	”	送	来	降准	大礼包	。	1日	下午	，中国	人民	银行	宣布	，	为	支持	实体	经济	发展	，	降低	社会	融资	实际	成本	，	决定	于	2020年	1月	6日	下调	金融	机构	存款	准备金率	0	.	5	个	百分点	(	不含	财务	公司	、	金融	租赁	公司	和	汽车	金融	公司	)	。	业内人士	认为	，	此次	降准	落地	后	，	对	股市	、	债	市	、	楼市	都	将	产生	一定	的	利好	。"
# words = s.split('\t')
# for w in words:
#     if is_Chinese(w):
#         print(w)

# ch = "1日"
# print(re.findall(regex, ch), len(re.findall(regex, ch)))
import math

file = open("/Users/ff/Desktop/train_data/en_US/unigram.txt", 'r', encoding='utf-8')
count = 1
max = 0
for l in file:
    word,freq = l.split('\t')
    if count == 1:  # 获取最大词频
        max = int(freq)
        logmax = math.pow(math.log(max), 2)
    log = math.pow(math.log(int(freq)), 2)
    result = round((log / logmax * 249) + 1)
    count += 1
    print(word + '\t' + str(result))
