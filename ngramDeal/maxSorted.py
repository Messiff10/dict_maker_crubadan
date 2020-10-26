import math
import re
"""
将真实词频缩放为250
"""
language = "en_US"
file_rnn = "/data/zzf/cellLexicon/en_US/en_US_video.wordcount"  ##统计词频
file_unigram = "/data/zzf/cellLexicon/en_US/en_US_unigram"  ## 基础词表
file_out = "/data/zzf/cellLexicon/en_US/out.txt"
unigram_set = set()
regex = re.compile(r'[^0-9]+')
unigram_dict = {}
# with open(file_unigram, 'r', encoding='utf-8') as f_in:
#     for line in f_in:
#         words = line.strip().split('\t')
#         if words[0].lower().strip() not in unigram_set and int(words[1].strip()) >= 100:
#             unigram_set.add(words[0].lower().strip())
count=0
with open(file_rnn, 'r', encoding='utf-8') as f_in:
    with open(file_out, 'w', encoding='utf-8') as f_out:
        for line in f_in:
            count += 1
            words=line.strip().split('\t')
            if words[0]=="karan":
                break
            print(count)
            words = line.strip().split('\t')
            # print(line)
            if len(words[0].strip()) > 1:
                if len(re.findall(regex, words[0].strip())) > 0 and words[0].lower().strip() not in unigram_set and \
                        words[0] not in unigram_dict.keys():
                    # print(line)
                    unigram_dict[words[0]] = words[1]
                    # f_out.write(line.strip())
                    # f_out.write('\n')
        count = 1 ##降序第一个词频
        for f in sorted(unigram_dict.items(), key=lambda x: -int(x[1])):  ## 降序读取统计出的真实词频
            # result = f[0] + "\t" + str(f[1])
            # f_out.write(result.strip())
            # f_out.write('\n')
            if count == 1: #获取最大词频
                max = int(f[1])
                logmax = math.pow(math.log(max), 2)
            log = math.pow(math.log(int(f[1])), 2)
            result = round((log / logmax * 249) + 1)
            count += 1
            resultline = f[0] + "\t" + str(result)
            f_out.write(resultline.strip())
            f_out.write('\n')
