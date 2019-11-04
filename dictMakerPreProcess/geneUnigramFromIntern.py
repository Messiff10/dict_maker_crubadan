import re
import os

# 将阿拉伯语实习生筛选结果改为可以作为输入生成词典的格式
# 阿拉伯语实习生筛选结果格式：بيذيد	361	Wrong (Egyptian)	بيزيد
# unigram 格式 :  word \t freq

input_dir = "/Users/grace/data/languages_from_intern/"
input_file_name = input_dir + "ar/WordlistofArabic.tsv"

output_dir = "/Users/grace/data/dict/from_intern/ar/"
output_file_standard_name = output_dir + 'ar_standard_unigram'
output_file_egyptian_name = output_dir + 'ar_egyptian_unigram'

if not os.path.exists(input_file_name):
    print(input_file_name, "doesn't exists!")

res_standard = []
res_egyptian = []
res_standard_set = []
with open(input_file_name, 'r', encoding='utf-8') as input_file:
    for line in input_file:
        items = line.split('\t')
        if len(items) != 4:  # 该行没有4部分
            print(line)

        word = items[0].strip()
        freq = items[1].strip()
        category = items[2].strip()
        candidate = items[3].strip()

        # 检查原始文件是否符合规范
        if word == "":
            print("type 1：" + line)
            continue
        if candidate == "" and (category == "Wrong (Standard)" or category == "Wrong (Egyptian)"):
            print("type 2：" + line)
            continue
        if freq == "added":
            freq = "0"

        if category == "Standard":
            res_standard.append(word + "\t" + freq + "\n")
            res_egyptian.append(word + "\t" + freq + "\n")
            res_standard_set.append(word + "\n")
        elif category == "Egyptian":
            res_egyptian.append(word + "\t" + freq + "\n")
        elif category == "Wrong (Standard)":
            res_standard.append(candidate + "\t" + freq + "\n")
            res_egyptian.append(candidate + "\t" + freq + "\n")
            res_standard_set.append(word + "\n")
        elif category == "Wrong (Egyptian)":
            res_egyptian.append(candidate + "\t" + freq + "\n")


res_standard_set = list(set(res_standard_set))
print("res_standard_set size:", str(len(res_standard_set)))

pattern = re.compile("^.+\t\d+$")
print("checking res_standard...")
for item in res_standard:
    if not re.match(pattern, item):
        print(item)

print("checking res_egyptian...")
for item in res_egyptian:
    if not re.match(pattern, item):
        print(item)

with open(output_file_egyptian_name, 'w', encoding='utf-8') as output_file:
    print("writing" + output_file_egyptian_name + ", size:" + str(len(res_egyptian)))
    output_file.writelines(res_egyptian)

with open(output_file_standard_name, 'w', encoding='utf-8') as output_file:
    print("writing" + output_file_standard_name + ", size:" + str(len(res_standard)))
    output_file.writelines(res_standard)


def countByCategories():
    with open(input_file_name, 'r', encoding='utf-8') as input_file:
        count_standard = 0
        count_egyptian = 0
        count_Wrong_Standard = 0
        count_Wrong_Egyptian = 0
        for line in input_file:
            items = line.split('\t')
            if len(items) != 4:  # 该行没有4部分
                print(line)

            category = items[2].strip()

            if category == "Standard":
                count_standard += 1
            elif category == "Egyptian":
                count_egyptian += 1
            elif category == "Wrong (Standard)":
                count_Wrong_Standard += 1
            elif category == "Wrong (Egyptian)":
                count_Wrong_Egyptian += 1

        print("count_standard: " + str(count_standard) + "\n"
              + "count_egyptian: " + str(count_egyptian) + "\n"
              + "count_Wrong_Standard:" + str(count_Wrong_Standard) + "\n"
              + "count_Wrong_Egyptian:" + str(count_Wrong_Egyptian))


countByCategories()

print("Finished!")
