# text = "กฎหมายแรงงานฉบับปรับปรุงใหม่ประกาศใช้แล้ว"
import os
import re

from pythainlp import sent_tokenize, word_tokenize
from pythainlp.tokenize.attacut import segment
"""
泰语分词器2
"""
data_folder = "/Users/ff/Desktop/maps/th/"
# out_path_newmm = "/Users/ff/Documents/th_20200420_.txt"
# out_path_longest = "/Users/ff/Desktop/train_data/th/th_100_pythainlp_longest.txt"
# out_path_segment = "/Users/ff/Desktop/train_data/th/th_100_pythainlp_segment.txt"
names=[]
for dir_path, subpaths, files in os.walk(data_folder):
    for name in files:  # 文件夹下的所有文件
        if not name.endswith('.DS_Store'):
            file_path = os.path.join(dir_path, name)
            names.append(name)
for name in names:
    file_path = os.path.join(data_folder, name)
    print(file_path)
    with open(file_path, 'r', encoding='utf-8') as f_in:
        with open(file_path.replace('.txt','split'), 'w', encoding='utf-8') as f_out_new:
            # with open(out_path_longest, 'w', encoding='utf-8') as f_out_long:
            #     with open(out_path_segment, 'w', encoding='utf-8') as f_out_seg:
            for line in f_in:
                # line = "คืบ่อนอนอ่ะ"
                # sents = sent_tokenize(line)
                # sents_ = " ".join(sents)
                # print("line:", line)  # default engine is "newmm"
                # print("sent_tokenize:", sents_)  # default engine is "newmm"
                # newmms = word_tokenize(line)
                # newmms_ = " ".join(newmms)
                # print("word_tokenize:", newmms_)
                # nospaces = word_tokenize(line, keep_whitespace=False)
                # nospaces_ = " ".join(nospaces)
                # print("word_tokenize, without whitespace:", nospaces_)  ## 去空格
                longests = word_tokenize(line, engine="longest")
                longests_ = " ".join(longests)
                # segments = segment(line)
                # segments_ = " ".join(segments)
                longests_ = re.sub('\s+', ' ', longests_)
                #
                # print("longest:", longests)
                # print("segment:", segments_)
                f_out_new.write(longests_.strip())
                f_out_new.write('\n')
                # f_out_long.write(longests_)
                # f_out_seg.write(segments_)
print("Finish line")
