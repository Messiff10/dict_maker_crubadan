import re
"""
筛选韩语
"""
import emoji

regex2 = re.compile('\s+')
regex = re.compile(
    '[\])>}{\[<(±+_\-—–·&‰%¢$£¥₱€#@†*‡★؟„\”“«»‚‹›\:;¡!¿?/,….~`|♪•♣♠♥♦√πΠ÷×§¶∆≠=≈∞′°″↑^←«»‚‹›\:;¡!¿?/,….~`|♪•♣♠♥♦√πΠ÷×§¶←↓→\\©®™℅,ـًٌٍَُِّْٰٖٕٓٔ¹½⅓¼⅛²⅔³¾⅜⅝⁴⅞@#¢₱€£¥%٪‰&_\-—–·+±\)}>﴿\({<﴾*★٭"„“”»«\‚‘’›‹:;؛¡!?؟∆≠=≈∞′°″،↑↓→\\\[\]\)>}{\[<\(±+_\-—–·&‰٪%¢£¥₱€#@†*‡★؟„\”“©®™℅\']')  # ar
# s = "ㅂㄷㅈㄱㅃㄸㅉㄲㅍㅌㅊㅋㅅㅎㅆㅁㄴㅇㄹㅣㅔㅚㅐㅏㅗㅜㅓㅡㅢㅖㅒㅑㅛㅠㅕㅟㅞㅙㅘㅝ"
# alist = [ch for ch in s]
regex_ko = re.compile(u"[\uac00-\ud7ff]+")
korean_path = "/Users/ff/Desktop/data/word/spark_language_data/1/ko_im_.txt"
with open(korean_path, 'r', encoding='utf-8') as f_ko:
    with open(korean_path.replace('.txt', '_search.txt'), 'w', encoding='utf-8') as f_out:
        for line in f_ko:
            words = regex2.split(line)
            result = re.findall(regex_ko, line)
            result = " ".join(result)
            if result.strip() is not "":
                # print(result)
                f_out.write(result.strip())
                f_out.write('\n')

print("Finish Line")
