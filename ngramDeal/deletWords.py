"""
去除敏感词汇
"""


senstive_path = "/Users/ff/Desktop/测评数据/文件对比/senstive.txt"
unigram_path = "/Users/ff/Desktop/测评数据/文件对比/de_unigram.txt"
senstive = set()
pass_senstive = set()
pass_senstive_true = set()
# 敏感词
with open(senstive_path, 'r', encoding='utf-8') as f_sen:
    for lin in f_sen:
        if lin.strip().lower().strip() not in senstive:
            senstive.add(lin.strip().lower())
print(len(senstive))
# 一元词表
with open(unigram_path, 'r', encoding='utf-8') as f_unigram:
    for line in f_unigram:
        words = line.strip().split('\t')
        if words[0].strip().lower().strip() not in senstive:
            pass_senstive.add((words[0].strip(),words[1]))
        else:
            print(words[0])
            pass_senstive_true.add(words[0])
# 二元词表
# with open(unigram_path, 'r', encoding='utf-8') as f_unigram:
#     for line in f_unigram:
#
#         words = line.strip().split('\t')
#         if words[0].strip().lower().strip() not in senstive and words[1].strip().lower().strip() not in senstive:
#             pass_senstive.add((words[0].strip(), words[1].strip(), words[2]))
#         else:
#             print(words[0])
#             pass_senstive_true.add((words[0].strip(), words[1].strip()))
# 一元词表
with open(unigram_path.replace('.txt', '.passsenstive'), 'w', encoding='utf-8') as f_unigram_pass:
    for li in sorted(pass_senstive, key=lambda x: int(x[1]),reverse=True):
        f_unigram_pass.write((li[0].strip() + "\t" + li[1]).strip())
        f_unigram_pass.write('\n')
# 二元词表
# with open(unigram_path.replace('.txt', '.passsenstive'), 'w', encoding='utf-8') as f_unigram_pass:
#     for li in sorted(pass_senstive, key=lambda x: (x[0], -int(x[2]))):
#         f_unigram_pass.write((li[0].strip() + "\t" + li[1]).strip() + "\t" + li[2])
#         f_unigram_pass.write('\n')
# 所有
with open(unigram_path.replace('.txt', '.senstive'), 'w', encoding='utf-8') as f_unigram_get:
    for lit in pass_senstive_true:
        f_unigram_get.write(lit[0].strip()+"\t"+lit[1].strip())
        f_unigram_get.write('\n')

print("Finish line")
