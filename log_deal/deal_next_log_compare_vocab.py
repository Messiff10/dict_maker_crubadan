import re

"""
先对log进行sublime初步处理 根据正则
分析输入效率 
查找下一次log中未匹配到的词
和词表进行对照
"""

regex = re.compile("ACCU_WORD(.*)\tTASK:input:(.*)\tSUGGESTION:(.*)")
file_in = "/Users/ff/Desktop/合入20200916"
file_out = "/Users/ff/Desktop/合入20200916_out"
vocab_true = "/Users/ff/Desktop/vocab_out"

vocaba = {}
false_vocab = {}
next = [()]


def getlog(file_out, count_false):
    f_out = open(file_out, 'w', encoding='utf-8')
    for current in range(2, len(next)):
        if next[current][1] == "false" and next[current][0] in vocaba.keys():
            result = next[current - 1][0] + " " + next[current][0]
            false_vocab[result] = vocaba[next[current][0]]
            count_false += 1
    for result in sorted(false_vocab.items(), key=lambda x: int(x[1])):
        result_line = result[0] + "\t" + str(result[1])
        # print(result_line)
        f_out.write(result[0].strip())
        f_out.write('\n')
    count = len(next) - 1
    print("all count", count, "false count", count_false, "false rate", str(float(count_false / count)))


def getnext(file_in, file_out):
    f_out = open(file_out, 'w', encoding='utf-8')
    with open(file_in, 'r', encoding='utf-8') as f_in:
        for l in f_in:
            if len(re.findall(regex, l)) != 0:
                a = re.findall(regex, l)[0]
                next.append(a)
                # f_out.write(l.strip())
                # f_out.write('\n')
        print(next)


def getvocab(vocab_true, num):
    with open(vocab_true, 'r', encoding='utf-8') as vocab:
        for l in vocab:
            words, freq = l.split('##')
            if len(vocaba) < num:
                vocaba[words] = str(freq).strip()
    print(vocaba)


if __name__ == '__main__':
    num = 20006
    getvocab(vocab_true, num)
    # count = 0
    count_false = 0
    getnext(file_in, file_out)
    getlog(file_out, count_false)
