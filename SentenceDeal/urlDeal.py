import re

import emoji

"""
将语句中的网址信息删除
"""
regex = re.compile(
    '[\±+_·&‰%¢$£¥₱€#@†*‡★؟\‚\:;/,….~`|♪•♣♠♥♦√πΠ÷×§¶∆≠=≈∞°↑^←‚\:;?/,….~`|♪•♣♠♥♦√πΠ÷×§¶←↓→\\©®™℅,ـًٌٍَُِّْٰٖٕٓٔ¹½⅓¼⅛²⅔³¾⅜⅝⁴⅞@#¢₱€£¥%٪‰&_·+±\\﴾*★٭\‚‹:;؛∆≠=≈!∞°،↑)}\]’’>›»’↓→\±+_\·&‰٪%¢£¥₱€#@†*‡★\©®™℅]')  # ar

file_path = "/Users/ff/Desktop/jp_ori.txt"
with open(file_path, 'r', encoding='utf-8') as f_in:
    with open(file_path.replace('.txt', '.replace'), 'w', encoding='utf-8') as f_out:
        for line in f_in:
            # line = re.sub(r'(https|http)?:\/\/(\w|-|\.|\/|\?|\=|\&|\%)*\b', '', line)
            # line = re.sub("[a-zA-Z']", " ", line)
            # # line = re.sub("【 (.*)】|\((.*)\)|", " ", line)
            # line = re.sub(emoji.get_emoji_regexp(), " ", line)
            # line = re.sub('[\±+_·&‰%¢$£¥₱€#@†*‡★؟\‚\:;/,….~`|♪•♣♠♥♦√πΠ÷×§¶∆≠=≈∞°↑^←‚\:;?/,….~`|♪•♣♠♥♦√πΠ÷×§¶←↓→\\©®™℅,ـًٌٍَُِّْٰٖٕٓٔ¹½⅓¼⅛²⅔³¾⅜⅝⁴⅞@#¢₱€£¥%٪‰&_·+±\\﴾*★٭\‚‹:;؛∆≠=≈!∞°،↑)}\]’’>›»’↓→\±+_\·&‰٪%¢£¥₱€#@†*‡★\©®™℅]', " ", line)
            line = re.sub("\s+", " ", line)
            f_out.write(line.strip())
            f_out.write('\n')
print("Finish Line")
