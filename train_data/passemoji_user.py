from utils.is_emoji import is_emoji
import re
import os
import time
regex = re.compile('')

# 去掉表情
# line ="لا تفتح اذنك لمن يقول مستحي😍ل 💔 😍 حينما تتمني"
add_path="/Users/ff/Desktop/train_data/pl/pl_web.txt" # ar_user_400.txt
count=0
# 去表情
with open(add_path, 'r', encoding='utf-8') as add_file:
    with open(add_path.replace('web.txt', 'web_noemoji.txt'), 'w', encoding='utf-8') as out_file:
        for line in add_file:
            centence = line
            words = regex.split(line)
            for word in words:
                if is_emoji(word):
                    centence=""
                    print(line)
                    break
            if centence is not "":
                count = count + 1
                out_file.writelines(line)
    print(count)
    print(add_path,"FInish line")