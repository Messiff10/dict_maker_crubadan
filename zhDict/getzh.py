import re
file="/Users/ff/Desktop/maps/mark/zh_20200420.txt"
file_out="/Users/ff/Desktop/maps/mark/zh_20200420_.txt"
with open(file,'r',encoding='utf-8') as f_in:
    with open(file_out, 'w', encoding='utf-8') as f_out:
        for line in f_in:
            m = re.findall('[\u4e00-\u9fa50-9]+', line)
            if m is not "":
                # print(" ".join(m))
                f_out.write(" ".join(m).strip())
                f_out.write('\n')
        # print(m)


        # def translate(str):
        #     line = str.strip()  # 处理前进行相关的处理，包括转换成Unicode等
        #     pattern = re.compile('[^\u4e00-\u9fa50-9]')  # 中文的编码范围是：\u4e00到\u9fa5
        #     zh = " ".join(pattern.split(line)).strip()
        #     # zh = ",".join(zh.split())
        #     outStr = zh  # 经过相关处理后得到中文的文本
        #     return outStr
        #
        #
        # print(translate(line))