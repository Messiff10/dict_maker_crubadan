# dividing_test.py
# coding:utf-8

import codecs
import glob
import codecs
import os
import re
"""
将词表进行拆分 
韩语
"""
regex = re.compile('')
first_parts = ("ㄱ", "ㄲ", "ㄴ", "ㄷ", "ㄸ", "ㄹ", "ㅁ", "ㅂ", "ㅃ", "ㅅ", "ㅆ", "ㅇ", "ㅈ", "ㅉ", "ㅊ", "ㅋ", "ㅌ", "ㅍ", "ㅎ")
second_parts = (
    "ㅏ", "ㅐ", "ㅑ", "ㅒ", "ㅓ", "ㅔ", "ㅕ", "ㅖ", "ㅗ", "ㅗㅏ", "ㅗㅐ", "ㅗㅣ", "ㅛ", "ㅜ", "ㅜㅓ", "ㅜㅔ", "ㅜㅣ", "ㅠ", "ㅡ", "ㅡㅣ", "ㅣ")
third_parts = (
    "", "ㄱ", "ㄲ", "ㄳ", "ㄴ", "ㄵ", "ㄶ", "ㄷ", "ㄹ", "ㄺ", "ㄻ", "ㄼ", "ㄽ", "ㄾ", "ㄿ", "ㅀ", "ㅁ", "ㅂ", "ㅄ", "ㅅ", "ㅆ", "ㅇ", "ㅈ",
    "ㅊ", "ㅋ", "ㅌ", "ㅍ", "ㅎ")


def divide_korean(temp_string):
    temp_string_value = ord(temp_string)
    part_1 = (temp_string_value - 44032) // 588
    part_2 = (temp_string_value - 44032 - part_1 * 588) // 28
    part_3 = (temp_string_value - 44032) % 28
    return first_parts[part_1] + second_parts[part_2] + third_parts[part_3]


old_korean_dictionary = {}
read_file = codecs.open("old_korean_dictionary.txt", 'r', encoding="utf-8")
for each_line in read_file:
    old_korean, dividing_parts = each_line.split()
    old_korean_dictionary[old_korean] = dividing_parts


def write_string_to_file(temp_str, file_name):
    # the encoding must be same with the str
    file_object = open(file_name, 'w', encoding="utf-16")
    file_object.write(temp_str)
    file_object.close()


data_files = "/Users/ff/Desktop/train_data/ko/ko_web_split.txt"
words = set()
letters = set()
with open(data_files, 'r', encoding="utf-8") as read_file:
    with open("/Users/ff/Desktop/train_data/ko/ko_wordcount.txt", 'w', encoding='utf-8') as f_out:
        temp_file_string = ""
        for each_line in read_file:
            if each_line.strip() == "":
                continue
            temp_line = ""
            original_line = each_line
            each_line = regex.split(each_line)
            for i in range(0, len(each_line)):
                if each_line[i] >= u'\uAC00' and each_line[i] <= u'\uD7AF':
                    if each_line[i].strip() not in words:
                        words.add(each_line[i].strip())
                        divid_line = divide_korean(each_line[i])
                        divid_line = str(divid_line).replace("ㄳ", "ᆨᆺ").replace("ㄼ", "ᆯᆸ").replace("ㅄ", "ᆸᆺ") \
                            .replace("ㄵ", "ᆫᆽ").replace("ㄽ", "ᆯᆺ").replace("ㄶ", "ᆫᇂ").replace("ㄾ", "ᆯᇀ") \
                            .replace("ㄺ", "ᆯᆨ").replace("ㄿ", "ᆯᇁ").replace("ㄻ", "ᆯᆷ").replace("ㅀ", "ᆯᇂ")
                        f_out.write(each_line[i] + '\t' + divid_line)
                        f_out.write('\n')
                elif each_line[i] == "\n":
                    continue
                else:
                    temp_line = temp_line + each_line[i]
print("Finish line")