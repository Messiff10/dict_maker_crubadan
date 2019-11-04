from utils.is_emoji import is_emoji
import re
import os
import time
regex = re.compile('\s+')

# 去掉表情
# line ="لا تفتح اذنك لمن يقول مستحي😍ل 💔 😍 حينما تتمني"
add_path="/Users/ff/Desktop/train_data/tr/tr_user_web.txt" # ar_user_400.txt
out_path="/Users/ff/Desktop/train_data/tr/tr_user_web_noemoji.txt"
count=0
# with open(add_path, 'r', encoding='utf-8') as adpwdd_file:
#     with open(out_path, 'a', encoding='utf-8') as out_file:
#         for line in add_file:
#             centence = line
#             words = regex.split(line)
#             for word in words:
#                 if(is_emoji(word)):
#                     centence=""
#                     break
#             if (centence is not ""):
#                 count = count + 1
#                 print(line)
#                 out_file.writelines(line)
#                 # out_file.write("\n")
#     print(count)
# 去表情
with open(add_path, 'r', encoding='utf-8') as add_file:
    with open(out_path, 'a', encoding='utf-8') as out_file:
        for line in add_file:
            centence = line
            words = regex.split(line)
            for word in words:
                if(is_emoji(word)):
                    centence=""
                    print(line)
                    break
            if (centence is not ""):
                count = count + 1
                out_file.writelines(line)
                out_file.write("\n")
    print(count)
# centence = line
# count=0
# # words = line.split("\\s+")
# words = regex.split(line)
# for word in words:
#     # print(word+"\n")
#     if( is_emoji( word ) ):
#         centence=""
#         print("true")
#         break
# if(centence is ""):
#     count = count+1
#     print(count)
#     print(line)