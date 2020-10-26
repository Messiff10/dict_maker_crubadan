# import json
# s = '\u0900'
#
# print(json.loads('"%s"' % s))

"""
天城文处理
"""
import re
letterset=set()
WORD_REGEX = re.compile(r"[\u0900-\u097f']")
s="विश्वास की एक डोरी है दोस्ती विश्वास के बिना कोरी है दोस्ती कभी थैंक्स तो कभी सॉरी है दोस्ती ना मानो तो कुछ भी नहीं पर मानो तो रब की भी कमजोरी है दोस्ती"
alist = [ch for ch in str(s).lower()]
print(alist)
for letter in alist:
    if re.search(WORD_REGEX, letter) is not None:
        if letter not in letterset:
            print(letter,re.search(WORD_REGEX, letter))

