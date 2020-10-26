"""
处理线上的语料 取所需部分
"""

data_flode = "rus-ru_web-public_2019_1M"
file_line = "/Users/ff/Downloads/" + data_flode + "/" + data_flode + "-sentences.txt"
file_out = "/Users/ff/Downloads/" + data_flode + "/centence_out.txt"
people = set()
lineset = set()
# with open(file_people, 'r', encoding='utf-8') as f_in:
#     for line in f_in:
#         wrds = line.strip().split('\t')
#         if wrds[0].strip() not in people:
#             people.add(wrds[0].strip())
#
with open(file_line, 'r', encoding='utf-8') as f_in:
    with open(file_out, 'w', encoding='utf-8') as f_out:
        for line in f_in:
            words = line.strip().split('\t')
            f_out.write(words[1].strip())
            f_out.write('\n')
print("Finish line")
