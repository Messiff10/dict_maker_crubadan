#!/usr/bin/python3
import re
import emoji


def is_emoji(content):
    if re.match(emoji.get_emoji_regexp(), content):
        return True
    return False

if __name__ == "__main__":
    content = "👰"
    content = "dddf"
    print(content, "is emoji?\t\t👰", is_emoji(content))
