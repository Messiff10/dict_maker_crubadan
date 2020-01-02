import re
## 筛选韩语
import emoji

regex2=re.compile('\s+')
regex = re.compile(
    '[\])>}{\[<(±+_\-—–·&‰%¢$£¥₱€#@†*‡★؟„\”“«»‚‹›\:;¡!¿?/,….~`|♪•♣♠♥♦√πΠ÷×§¶∆≠=≈∞′°″↑^←«»‚‹›\:;¡!¿?/,….~`|♪•♣♠♥♦√πΠ÷×§¶←↓→\\©®™℅,ـًٌٍَُِّْٰٖٕٓٔ¹½⅓¼⅛²⅔³¾⅜⅝⁴⅞@#¢₱€£¥%٪‰&_\-—–·+±\)}>﴿\({<﴾*★٭"„“”»«\‚‘’›‹:;؛¡!?؟∆≠=≈∞′°″،↑↓→\\\[\]\)>}{\[<\(±+_\-—–·&‰٪%¢£¥₱€#@†*‡★؟„\”“©®™℅\']')  # ar
# s = "ㅂㄷㅈㄱㅃㄸㅉㄲㅍㅌㅊㅋㅅㅎㅆㅁㄴㅇㄹㅣㅔㅚㅐㅏㅗㅜㅓㅡㅢㅖㅒㅑㅛㅠㅕㅟㅞㅙㅘㅝ"
# alist = [ch for ch in s]

#
# for w in alist:
#     chInt = ord(w)
#     if chInt >= 12592 and chInt <= 12735 or chInt >= 44032 and chInt <= 55203:
#         print(w)
korean_path = "/Users/ff/Desktop/train_data/ko/ko_user.txt"
with open(korean_path, 'r', encoding='utf-8') as f_ko:
    with open(korean_path.replace('.txt', '_search.txt'), 'w', encoding='utf-8') as f_out:
        for line in f_ko:
            words=regex2.split(line.strip())
            if len(words)>=2:
                a = line
                centence = line
                line = re.sub(emoji.get_emoji_regexp(), '', line)
                line = re.sub(regex, '', line)
                line = re.sub('\s+', '', line)
                line = re.sub('\d+', '', line)
                # line = re.sub(r'[a-zA-Z]+', '', line)
                alist = [ch for ch in line.strip()]
                for w in alist:
                    chInt = 0
                    chInt = ord(w)
                    if not (chInt >= 12592 and chInt <= 12735 or chInt >= 44032 and chInt <= 55203):
                        centence = ""
                        break;
                if centence is not "":
                    # print(a)
                    f_out.write(centence.strip())
                    f_out.write('\n')
            else:
                continue

print("Finish Line")
