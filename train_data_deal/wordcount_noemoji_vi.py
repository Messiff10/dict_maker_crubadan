import re
import sys
"""
特殊语言处理 统计词频
越南语
"""
## 统计词频和单词
## 匹配键码生成训练数据
import emoji


def is_emoji(content):
    if re.match(emoji.get_emoji_regexp(), content):
        return True
    return False


##
## 参数列表
## 参数一：语言locale 参数二：
regex_pun = re.compile(
    '[\])>}{\[<(±+_\-—–·&‰%¢$£¥₱€#@†*‡★؟„\”“«»‚‹›\:;¡!¿?/,….~`|♪•♣♠♥♦√πΠ÷×§¶∆≠=≈∞′°″↑^←«»‚‹›\:;¡!¿?/,….~`|♪•♣♠♥♦√πΠ÷×§¶←↓→\\©®™℅,ـًٌٍَُِّْٰٖٕٓٔ¹½⅓¼⅛²⅔³¾⅜⅝⁴⅞@#¢₱€£¥%٪‰&_\-—–·+±\)}>﴿\({<﴾*★٭"„“”»«\‚‘’›‹:;؛¡!?؟∆≠=≈∞′°″،↑↓→\\\[\]\)>}{\[<\(±+_\-—–·&‰٪%¢£¥₱€#@†*‡★؟„\”“©®™℅]')  # ar

regex = re.compile('\|\|\|')
language = sys.argv[1]
if language == "en_US":
    WORD_REGEX = re.compile(r"[^a-zA-Z']")
elif language == "it":
    WORD_REGEX = re.compile(r"[^qwertyuiìíopèéùúasdfghjklòóàzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM']")
elif language == "fi":
    WORD_REGEX = re.compile(r"[^abcdefghijklmnopqrstuvwxyzåäöABCDEFGHIJKLMNOPQRSTUVWXYZAÅÄOÖ']")
elif language == "tr":
    WORD_REGEX = re.compile(r"[^qwertyüuıiöopâaşsdfğghjklzxçcvbnmQWERTYÜUIİÖOPAŞSDFĞGHJKLZXÇCVBNM']")
elif language == "ru":
    WORD_REGEX = re.compile(r"[^йцукенгшщзхфывапролджэячсмитьбюЙЦУКЕНГШЩЗХФЫВАПРОЛДЖЭЯЧСМИТЬБЮ']")
elif language == "es":
    WORD_REGEX = re.compile(r"[^qwėêęēèéëertyūùûüúuīîįìïíiºōœøõôöòóopåąæāªáàäâãasdfghjklñzxčçćcvbñńnmQWĖÊĘĒÈ3ËERTYŪÙÛÜÚUĪÎĮÌÏÍIºŌŒØÕÔÖÒÓOPÅĄÆĀĀÁÀÄ ÃASDFGHJKLÑZXČÇĆCVBÑŃNM']")
elif language == "es_US":
    WORD_REGEX = re.compile(r"[^qwėêęēèéëertyūùûüúuīîįìïíiºōœøõôöòóopåąæāªáàäâãasdfghjklñzxčçćcvbñńnmQWĖÊĘĒÈ3ËERTYŪÙÛÜÚUĪÎĮÌÏÍIºŌŒØÕÔÖÒÓOPÅĄÆĀĀÁÀÄ ÃASDFGHJKLÑZXČÇĆCVBÑŃNM']")
elif language == "ms_MY":
    WORD_REGEX = re.compile(r"[^qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM']")
elif language == "pl":
    WORD_REGEX = re.compile(r"[^aąbcćdeęfghijklłmnńoóprsśtuwyzźżAĄBCĆDEĘFGHIJKLŁMNŃOÓPRSŚTUWYZŹŻ']")
elif language == "sv":
    WORD_REGEX = re.compile(r"[^abcdefghijklmnopqrstuvwxyzåäöABCDEFGHIJKLMNOPQRSTUVWXYZAÅÄOÖ']")
elif language == "th":
    WORD_REGEX = re.compile(
        r"[^\u0E01\u0E02\u0E03\u0E04\u0E05\u0E06\u0E07\u0E08\u0E09\u0E0A\u0E0B\u0E0C\u0E0D"
        r"\u0E0E\u0E0F\u0E10\u0E11\u0E12\u0E13\u0E14\u0E15\u0E16\u0E17\u0E18\u0E19\u0E1A"
        r"\u0E1B\u0E1C\u0E1D\u0E1E\u0E1F\u0E20\u0E21\u0E22\u0E23\u0E24\u0E25\u0E26\u0E27\u0E28"
        r"\u0E29\u0E2A\u0E2B\u0E2C\u0E2D\u0E2E\u0E2F\u0E30\u0E31\u0E32\u0E33\u0E34\u0E35\u0E36"
        r"\u0E37\u0E38\u0E39\u0E3A\u0E3F\u0E40\u0E41\u0E42\u0E43\u0E44\u0E45\u0E46\u0E47\u0E48"
        r"\u0E49\u0E4A\u0E4B\u0E4C\u0E4D\u0E4E\u0E4F\u0E50\u0E51\u0E52\u0E53\u0E54\u0E55\u0E56"
        r"\u0E57\u0E58\u0E59\u0E5A\u0E5B']")
elif language == "ar":
    WORD_REGEX = re.compile(r"[^\s'ضصثقفغعهخحجشسيبلاتنمكطذءؤرىةوزظدئإأآڨڭپڢڤچ]+")
elif language == "de":
    WORD_REGEX = re.compile(r"[^qwertzuiopüasdfghjklöäyxcvbnmßQWERTZUIOPÜASDFGHJKLÖÄYXCVBNMẞ']")
elif language == "da":
    WORD_REGEX = re.compile(r"[^qwertyuiopåasdfghjkløæzxcvbnmQWERTYUIOPÅASDFGHJKLØÆZXCVBNM']")
elif language == "nb":
    WORD_REGEX = re.compile(r"[^qwertyuiopåasdfghjkløæzxcvbnmQWERTYUIOPÅASDFGHJKLØÆZXCVBNM']")
elif language == "cs":
    WORD_REGEX = re.compile(
        r"[^aábcčdďeéěfghchiíjklmnňoópqrřsštťuúůvwxyýzžAÁBCČDĎEÉĚFGHChIÍJKLMNŇOÓPQRŘSŠTŤUÚŮVWXYÝZŽ']")
elif language == "ur":
    WORD_REGEX = re.compile(r"[^ےیءھہونملگکقفغعظطضصشسژڑرذڈدخحچجثٹتپباآ']")
elif language == "ko":
    WORD_REGEX = re.compile(r"[^ㅂㄷㅈㄱㅃㄸㅉㄲㅍㅌㅊㅋㅅㅎㅆㅁㄴㅇㄹㅣㅔㅚㅐㅏㅗㅜㅓㅡㅢㅖㅒㅑㅛㅠㅕㅟㅞㅙㅘㅝ']")
elif language == "fr":
    WORD_REGEX = re.compile(r"[^éèêëcçàâæazertyÿuiîïoôœpqsdfghjklmùûüwxcvbnAÀÆZEÉÈÊËCÇRTYŸUÛÜIÎÏOÔŒPQSDFGHJKLMWXCVBN']")
elif language == "nl":
    WORD_REGEX = re.compile(r"[^qweéërtyuüiïoóöpasdfghjklzxcvbnmQWEÉËRTYUÜIÏOÓÖPASDFGHJKLZXCVBNM']")
elif language == "kk":
    WORD_REGEX = re.compile(r"[^йцұүукқеёнңгғшщзхһфыівәапрөолджэячсмитъьбюЙЦҰҮУҚКЁЕҢНҒГШЩЗҺХФІЫВӘАПРӨОЛДЖЭЯЧСМИТЪЬБЮ']")
elif language == "vi":
    WORD_REGEX = re.compile(r"[^AaĂăâBbCcDdĐđEeÊêGgHhIiKkLlMmNnOoÔôƠơPpQqRrSsTtUuƯưVvXxYy ']")
count_dict = {}
letterset = set()
emojiset = set()
file_path = sys.argv[2]
emoji_path = sys.argv[3]
with open(emoji_path, 'r', encoding='utf-8') as f_emoji:
    for line in f_emoji:
        emojis = line.strip().split('\t')
        if emojis[0] not in emojiset:
            emojiset.add(emojis[0])
with open(file_path, 'r', encoding='utf-8') as f_in:
    for line in f_in:
        line = re.sub(regex_pun, ' ', line.strip())
        line = re.sub('\s+', ' ', line.strip())
        words = regex.split(line.strip())
        # 如果字典里有该单词则加1，否则添加入字典
        for w in words:
            if re.search(WORD_REGEX, w.strip()) is None:
                # print(w)
                if w.strip() in count_dict.keys():
                    count_dict[w] = count_dict[w] + 1
                else:
                    count_dict[w] = 1
        # 按照词频从高到低排列
    count_list = sorted(count_dict.items(), key=lambda x: int(x[1]), reverse=True)
    with open(file_path.replace('.txt', '.wordcount'), 'w', encoding='utf-8') as f_word:
        for l in count_list:
            s1 = str(l[0]) + "\t" + str(l[1])
            alist = [ch for ch in str(l[0]).lower()]
            for letter in alist:
                if re.search(WORD_REGEX, letter) is None:
                    if letter not in letterset:
                        print(letter)
                        letterset.add(letter)
            f_word.write(s1)
            f_word.write('\n')
    with open(file_path.replace('.txt', '.letter'), 'w', encoding='utf-8') as f_letter:
        for lt in sorted(letterset):
            f_letter.write(lt.strip())
            f_letter.write('\n')
    f_letter.close()
    f_word.close()
    f_in.close()
print("Finish line")
