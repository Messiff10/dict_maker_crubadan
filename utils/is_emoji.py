#!/usr/bin/python3
import re
import emoji

"""
判断是否是表情
"""
def is_emoji(content):
    if re.match(emoji.get_emoji_regexp(), content):
        return True
    return False

if __name__ == "__main__":
    content = "あともう少しだった 😓  . . /"
    # content = "dddf"
    print(re.sub(emoji.get_emoji_regexp()," ",content))
