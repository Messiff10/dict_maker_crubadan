import re
import sys
"""
越南语 按照词组分割语句
"""
file = sys.argv[1]
dictfile = sys.argv[2]
resultfile = sys.argv[3]

dictsets = set()
dictsets_sort = []


def chooseword(file, resultfile):
    with open(file, 'r', encoding='utf-8') as f_in:
        with open(resultfile, 'w', encoding='utf-8') as f_out:
            for line in f_in:
                line = " " + line.strip() + " "
                for dts in dictsets_sort:
                    if str(dts).lower() in line.lower():
                        print("dict-----" + str(dts).lower())
                        start = line.lower().index(str(dts).lower())
                        line = line.replace(line[start:start + len(str(dts).lower())].strip(),
                                            re.sub('\s+', '^^', line[start:start + len(str(dts).lower())].strip()))
                        print("result---" + line)
                line = re.sub("\s+", '|||', line.strip())
                line = line.strip().replace('^^', ' ')
                f_out.write(line.strip())
                f_out.write('\n')


def getdict(dictfile):
    with open(dictfile, 'r', encoding='utf-8') as f_dict:
        for line in f_dict:
            if line.strip() not in dictsets:
                dictsets.add(" " + line.strip() + " ")
        for dictset in sorted(dictsets, key=lambda x: -int(len(x))):
            dictsets_sort.append(dictset)


if __name__ == '__main__':
    getdict(dictfile)
    chooseword(file, resultfile)
    print("finish line")
