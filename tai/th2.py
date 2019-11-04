import os
from time import time

import pythainlp
from pythainlp import word_tokenize, Tokenizer
from pythainlp import sent_tokenize, word_tokenize
from pythainlp.corpus.common import thai_words
from pythainlp import word_tokenize, Tokenizer
from pythainlp.tokenize.multi_cut import find_all_segment, mmcut, segment


# text = "กฎหมายแรงงานฉบับปรับปรุงใหม่ประกาศใช้แล้ว"
file_path="/Users/ff/Desktop/train_data/th/th_100.txt"
out_path_newmm="/Users/ff/Desktop/train_data/th/th_100_pythainlp_newmm.txt"
out_path_longest="/Users/ff/Desktop/train_data/th/th_100_pythainlp_longest.txt"
out_path_segment="/Users/ff/Desktop/train_data/th/th_100_pythainlp_segment.txt"

if os.path.exists(out_path_newmm):
    print("remove:",out_path_newmm)
    os.remove(out_path_newmm)
if os.path.exists(out_path_longest):
    print("remove:",out_path_longest)
    os.remove(out_path_longest)
if os.path.exists(out_path_segment):
    print("remove:",out_path_segment)
    os.remove(out_path_segment)
with open(file_path,'r',encoding='utf-8') as f_in:
    with open(out_path_newmm,'w',encoding='utf-8') as f_out_new:
        with open(out_path_longest, 'w', encoding='utf-8') as f_out_long:
            with open(out_path_segment, 'w', encoding='utf-8') as f_out_seg:
                for line in f_in:
                    sents=sent_tokenize(line)
                    sents_=" ".join(sents)
                    newmms=word_tokenize(line)
                    newmms_=" ".join(newmms)
                    nospaces=word_tokenize(line, keep_whitespace=False)
                    nospaces_=" ".join(nospaces)
                    longests=word_tokenize(line,engine="longest")
                    longests_=" ".join(longests)
                    segments=segment(line)
                    segments_=" ".join(segments)
                    print("line:", line)  # default engine is "newmm"
                    print("sent_tokenize:", sents_)# default engine is "newmm"
                    print("word_tokenize:", newmms_)
                    print("word_tokenize, without whitespace:", nospaces_)## 去空格
                    print("longest:", longests_)
                    print("segment:", segments_)
                    f_out_new.write(newmms_)
                    f_out_long.write(longests_)
                    f_out_seg.write(segments_)