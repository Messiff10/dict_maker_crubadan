from cutkum.tokenizer import Cutkum
import os
"""
泰语分词
"""
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
file_path = "/Users/ff/Documents/th_20200420.txt"
out_path = "/Users/ff/Documents/th_20200420_2.txt"
ck = Cutkum()
if os.path.exists(out_path):
    print("remove:" + str(out_path))
    os.remove(out_path)
# กองกลาง วัย 29 ปีก ล่า ว ปิดท้าย
with open(file_path, 'r', encoding='utf-8') as f_in:
    with open(out_path, 'w', encoding='utf-8') as f_out:
        for line in f_in:
            words = ck.tokenize(line)
            # print(" ".join(words))
            f_out.write(" ".join(words))
            f_out.write('\n')
