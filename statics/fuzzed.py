import re
"""
统计纠错语料错误率
"""
regex2 = re.compile("WR#CO")
regex = re.compile('\s+')
file_path = "/Users/ff/Desktop/测评数据/纠错/hi_HINGLISH_twitter.tsv.fuzzed"
count = 0
falsecount = 0
with open(file_path, 'r', encoding='utf-8') as f_in:
    for line in f_in:
        # print(line)
        fileds = regex2.split(line.strip())
        fileds0 = regex.split(fileds[0].strip())
        fileds1 = regex.split(fileds[1].strip())
        if len(fileds1) == len(fileds0):
            for i in range(0, len(fileds0)):
                count += 1
                if fileds0[i] != fileds1[i]:
                    # print(fileds1[i])
                    falsecount += 1
        else:
            print(line, len(fileds1), len(fileds0))
print("纠错率", str(count) + "\t" + str(falsecount) + "\t" + str(float(falsecount / count)))
