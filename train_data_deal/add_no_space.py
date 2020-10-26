import codecs
import os
import re
import sys
"""
爬取新闻前后加空格
"""

# def is_emoji(content):
#     if re.match(emoji.get_emoji_regexp(), content):
#         return True
#     return False

language = sys.argv[3]
if language == "ur":
    regex = re.compile(
        r"([¹½⅓¼⅛²⅔³⅜¾⁴⅝⅞ⁿ∅\])}>({\[<+±\-_—–·：‰%¢$£¥€₱#@†*‡★\"„“”«»’‚‘\‹›؛¡！¿؟/،.…~`|♪•♣♠♥♦√πΠ÷§×¶∆≠=≈∞′°″↑^←↓→\\©®™℅≤≥ْْ])")
elif language == "en_US":
    regex = re.compile(
        r"([)(+\-&%$#@*\":\";!¹½⅓¼⅛²⅔³⅜¾⁴⅝⅞∅\]}>{<\[±—–·‰¢€₱£¥†‡★“”„«»’‘‚‹›¡¿?/.~`|♪•♣♠♥♦√÷×§¶∆\"≠=≈∞′°″↑^←↓→\\©®™℅≤≥,…])")
elif language == "ms_MY":
    regex = re.compile(
        r"([,-:@#!,?.¹½⅓¼⅛²⅔⅜³¾⁴⅝⅞ⁿ∅@#€¢£¥₱$‰%&—_–·\-±+<{[()\]}>/★†‡*„“”«»\"‚‘’‹›:;¡!¿?_, ….~`|♣♠♪♥♦•√πΠ÷×§¶∆£€¥¢←↑↓→^′″°∞≠≈={},\©®™℅\[\]‹≤«<>»≥› ….])")
elif language == "sv":
    regex = re.compile(
        r"([.\-:@#!?¹½⅓¼⅛²⅔⅜³¾⁴⅝⅞∅ⁿ€₱$¢£¥%‰&—_–·+±\(<{\[\)>}\]*†‡★\"„“”»«‚‘’›‹;¡¿/…~`|•♣♠♪♥♦√Ππ÷×¶§∆^←↑↓→°′″=∞≠≈\\©®™℅≤≥])")
elif language == "fi":
    regex = re.compile(
        r"([,.\-:@#!?¹½⅓¼⅛²⅔⅜³¾⁴⅝⅞∅ⁿ€₱$¢£¥%‰&—_–·+±(<{[)>}\]*†‡★\"„“”«»‚‘’‹›;¡¿/…~`|•♣♠♪♥♦√Ππ÷×¶§∆^←↑↓→°′″=∞≠≈\\©®™℅≤≥])")
elif language == "es_CO":
    regex = re.compile(
        r"([,:¡@¿;!,?¹½⅓¼⅛²⅔⅜³¾⁴⅝⅞ⁿ∅@#$¢£¥₱€‰%&——–·\-±+<{[()\]}>/★†‡*„“”«»\"‚‘’‹›:;¡!¿?_!¡, ?¿.~`|♣♠♪♥♦•√πΠ÷×§¶∆£¥$¢←↑↓→^′″°∞≠≈={}!¡,\©®™℅[\]‹≤«<>»≥› ?¿.])")

regex2 = re.compile('\s+')
regex3 = re.compile('')
# data_folder = '/Users/ff/Desktop/测评数据/加空格'
# names = []
emojiset = set()
centence = set()
file_path = sys.argv[1]


def getemoji(emoji_path):
    with open(emoji_path, 'r', encoding='utf-8') as f_emoji:
        for line in f_emoji:
            emojis = line.strip().split('\t')
            if emojis[0].strip() not in emojiset:
                emojiset.add(emojis[0])


def addspace():
    with open(file_path, 'r', encoding='utf-8') as f_in:
        with open(file_path.replace('.txt', '.space_pass_distinct'), 'w', encoding='utf-8') as f_out:
            for line in f_in:
                # print(line)

                # line.replace()
                # words=re.find(regex,line)
                allwords = [ch for ch in line.strip()]
                for allw in allwords:
                    if allw.strip() in emojiset:
                        line = ""
                        # print(line)
                        break
                        # line = line.replace(allw, ' ' + allw + ' ')
                        # line = re.sub('\s+', ' ', line)
                if line.strip() is not "":
                    if line.strip() not in centence:
                        # centence.add(line)
                        centence.add(line.strip())
                        # words = re.findall(regex, line)

                        line = re.sub(regex, lambda x: " " + x.group(1) + " ", line.strip())
                        line = re.sub("\s+", " ", line)
                        # words = re.findall(regex, line)
                        # for w in words:
                        #     # line=line.replace(' ','')
                        #     # 先去空格
                        #     # line = line.replace(' '+w , w)
                        #     line = re.sub('\s+', ' ', line)
                        #     line = line.replace(' ' + w + ' ', w)
                        #     line = line.replace(' ' + w, w)
                        #     line = line.replace(w + ' ', w)
                        #     # line = line.replace('  ', '')
                        #     # 加空格
                        #     # line.replace(emojiset, ' ' + emojiset + ' ', line)
                        #     line = line.replace(w, ' ' + w + ' ')  # 加空格
                        #     line = re.sub(r"(\w+) ?\' (\w+)?", r"\1'\2", line)
                        #     # line = line.replace('\'', '\'')
                        # line = re.sub('\s+', ' ', line)
                        # print(line)
                        f_out.write(line.strip())
                        f_out.write('\n')


if __name__ == '__main__':
    emoji_path = sys.argv[2]
    print(language)
    getemoji(emoji_path)
    addspace()
    print("Finsh line")
# print(line)
