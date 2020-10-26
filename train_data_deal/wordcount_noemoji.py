import re
import sys
"""
统计词频
"""

import emoji

##
## 参数列表
## 参数一：语言locale 参数二：
regex = re.compile("\s+")
# WORD_REGEX = re.compile(r"[^qwėêęēèéëertyūùûüúuīîįìïíiºōœøõôöòóopåąæāªáàäâãasdfghjklñzxčçćcvbñńnmQWĖÊĘĒÈ3ËERTYŪÙÛÜÚUĪÎĮÌÏÍIºŌŒØÕÔÖÒÓOPÅĄÆĀĀÁÀÄÃASDFGHJKLÑZXČÇĆCVBÑŃNM']")
# language = sys.argv[1]
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
    WORD_REGEX = re.compile(r"[^qwėêęēèéëertyūùûüúuīîįìïíiºōœøõôöòóopåąæāªáàäâãasdfghjklñzxčçćcvbñńnmQWĖÊĘĒÈ3ËERTYŪÙÛÜÚUĪÎĮÌÏÍIºŌŒØÕÔÖÒÓOPÅĄÆĀĀÁÀÄÃASDFGHJKLÑZXČÇĆCVBÑŃNM']")
elif language == "es_US":
    WORD_REGEX = re.compile(r"[^qwėêęēèéëertyūùûüúuīîįìïíiºōœøõôöòóopåąæāªáàäâãasdfghjklñzxčçćcvbñńnmQWĖÊĘĒÈ3ËERTYŪÙÛÜÚUĪÎĮÌÏÍIºŌŒØÕÔÖÒÓOPÅĄÆĀĀÁÀÄÃASDFGHJKLÑZXČÇĆCVBÑŃNM']")
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
elif language == "fa":
    WORD_REGEX = re.compile(r"[^ضصثقفغعهةه‍هٔخحجشسیىئيبلٱءآأإاةتنمكکگظطژزرذدپؤوچ']")
elif language == "in":
    WORD_REGEX = re.compile(r"[^AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz']")
elif language == "jv":
    WORD_REGEX = re.compile(r"[^AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz']")
elif language == "fil":
    WORD_REGEX = re.compile(r"[^AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz']")
elif language == "yi":
    WORD_REGEX = re.compile(r"[^אאַאָבבּבֿגדדזשהווּוֹװויזזשחטטשייִייײַכּכךלמםנןסעפּפֿפףצץקרששׂתּת']")
elif language == "pt_BR":
    WORD_REGEX = re.compile(r"[^aáàãâbcçdeéêfghiíjklmnoóõôpqrstuúüvwxyzAÁÀÃBCÇDEÉÊFGHIÍJKLMNOÓÕÔPQRSTUÚÜVWXYZ']")
elif language == "su":
    WORD_REGEX = re.compile(r"[^AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz']")
elif language == "vi":
    WORD_REGEX = re.compile(r"[^AaĂăâBbCcDdĐđEeÊêGgHhIiKkLlMmNnOoÔôƠơPpQqRrSsTtUuƯưVvXxYy']")
elif language == "hi":
    WORD_REGEX = re.compile(r"[^\u0900-\u097f']")
elif language == "ro":
    WORD_REGEX = re.compile(r"[^qwertțyuīíįìïîopâãăàáäæåāaśșßšsdfghjklzxcvbnmQWERTȚYUIĪÍĮÌÏÎOPÄÆÅĀÃĂÀÁASŚȘSSŠDFGHJKLZXCVBNM']")
elif language == "hu":
    WORD_REGEX = re.compile(r"[^qwėëęęèéêertzuûùūüúűiīìįïîíiōøœõòôőöóopæãåāáàâäasdfghjklyxcvbnmQWĖËĘĒÈÉÊERTZÛÙŪÜÚŰUĪÌĮÏÎÍIØØŒÕÒÔŐÖÓOPÆÃÅĀÁÀÄASDFGHJKLYXCVBNM']")
elif language == "uk":
    WORD_REGEX = re.compile(r"[^йцукенґгшщзхфїівапролджєячсмитъьбюЙЦУКЕНГШЩЗХФЇІВАПРОЛДЖЄЯЧСМИТЪЬБЮ']")
elif language == "pt_PT":
    WORD_REGEX = re.compile(r"[^aáàãâbcçdeéêfghiíjklmnoóõôpqrstuúüvwxyzAÁÀÃBCÇDEÉÊFGHIÍJKLMNOÓÕÔPQRSTUÚÜVWXYZ']")
elif language == "kk":
    WORD_REGEX = re.compile(r"[^йцұүукқеёнңгғшщзхһфыівәапрөолджэячсмитъьбюЙЦҰҮУҚКЁЕҢНҒГШЩЗҺХФІЫВӘАПРӨОЛДЖЭЯЧСМИТЪЬБЮ']")
elif language == "hi_HINGLISH":
    WORD_REGEX = re.compile(r"[^a-zA-Z']")
elif language == "ur":
    WORD_REGEX = re.compile(r"[^قوعرتےءیهپلکجحگفدسازشچطبنمؤٰڑہٹَأئةۀُخضھغًڈصہآذژثظِںّ']")

count_dict = {}
letterset = set()
emojiset = set()
file_path = sys.argv[2]
emoji_path = sys.argv[3]
# file_path = "/Users/ff/Desktop/train_data/ur/ur_unigram.txt"
# emoji_path = "/Users/ff/Desktop/train_data/all_emojis"
with open(emoji_path, 'r', encoding='utf-8') as f_emoji:
    for line in f_emoji:
        emojis = line.strip().split('\t')
        if emojis[0] not in emojiset:
            emojiset.add(emojis[0])
with open(file_path, 'r', encoding='utf-8') as f_in:
    for line in f_in:
        if language == "ur":
            line = line.strip().replace('\uFBAE', '\u06D2').replace('\uFBAF', '\u06D2') \
                .replace('\uFBFC', '\u06CC').replace('\uFBFD', '\u06CC').replace('\uFBFE', '\u06CC').replace('\uFBFF',
                                                                                                             '\u06CC') \
                .replace('\uFE80', '\u0621') \
                .replace('\uFE70', '\u064B') \
                .replace('\uFE76', '\u064E').replace('\uFE77', '\u064E') \
                .replace('\uFE78', '\u064F').replace('\uFE79', '\u064F') \
                .replace('\uFE7A', '\u0650').replace('\uFE7B', '\u0650') \
                .replace('\uFE7C', '\u0651').replace('\uFE7D', '\u0651') \
                .replace('\uFBA4', '\u06C0').replace('\uFBA5', '\u06C0') \
                .replace('\uFBAA', '\u06BE').replace('\uFBAB', '\u06BE').replace('\uFBAC', '\u06BE').replace('\uFBAD',
                                                                                                             '\u06BE') \
                .replace('\uFE83', '\u0623').replace('\uFE84', '\u0623') \
                .replace('\uFBA6', '\u06C1').replace('\uFBA7', '\u06C1').replace('\uFBA8', '\u06C1').replace('\uFBA9',
                                                                                                             '\u06C1') \
                .replace('\uFEED', '\u0648').replace('\uFEEE', '\u0648') \
                .replace('\uFB9E', '\u06BA').replace('\uFB9F', '\u06BA') \
                .replace('\uFE85', '\u0624').replace('\uFE86', '\u0624') \
                .replace('\uFE93', '\u0629)').replace('\uFE94', '\u0629') \
                .replace('\uFEE5', '\u0646').replace('\uFEE6', '\u0646').replace('\uFEE7', '\u0646').replace('\uFEE8',
                                                                                                             '\u0646') \
                .replace('\uFE89', '\u0626').replace('\uFE8A', '\u0626').replace('\uFE8B', '\u0626').replace('\uFE8C',
                                                                                                             '\u0626') \
                .replace('\uFEE1', '\u0645').replace('\uFEE2', '\u0645').replace('\uFEE3', '\u0645').replace('\uFEE4',
                                                                                                             '\u0645') \
                .replace('\uFEDD', '\u0644').replace('\uFEDE', '\u0644').replace('\uFEDF', '\u0644').replace('\uFEE0',
                                                                                                             '\u0644') \
                .replace('\uFB92', '\u06AF').replace('\uFB93', '\u06AF').replace('\uFB94', '\u06AF').replace('\uFB95',
                                                                                                             '\u06AF') \
                .replace('\uFB8E', '\u06A9').replace('\uFB8F', '\u06A9').replace('\uFB90', '\u06A9').replace('\uFB91',
                                                                                                             '\u06A9') \
                .replace('\uFED5', '\u0642').replace('\uFED6', '\u0642').replace('\uFED7', '\u0642').replace('\uFED8',
                                                                                                             '\u0642') \
                .replace('\uFED1', '\u0641').replace('\uFED2', '\u0641').replace('\uFED3', '\u0641').replace('\uFED4',
                                                                                                             '\u0641') \
                .replace('\uFECE', '\u063A').replace('\uFECF', '\u063A').replace('\uFED0', '\u063A') \
                .replace('\uFEC9', '\u0639').replace('\uFECA', '\u0639').replace('\uFECB', '\u0639').replace('\uFECC',
                                                                                                             '\u0639') \
                .replace('\uFEC5', '\u0638').replace('\uFEC6', '\u0638').replace('\uFEC7', '\u0638').replace('\uFEC8',
                                                                                                             '\u0638') \
                .replace('\uFEC1', '\u0637').replace('\uFEC2', '\u0637').replace('\uFEC3', '\u0637').replace('\uFEC4',
                                                                                                             '\u0637') \
                .replace('\uFEBD', '\u0636').replace('\uFEBE', '\u0636').replace('\uFEBF', '\u0636').replace('\uFEC0',
                                                                                                             '\u0636') \
                .replace('\uFEB9', '\u0635').replace('\uFEBA', '\u0635').replace('\uFEBB', '\u0635').replace('\uFEBC',
                                                                                                             '\u0635') \
                .replace('\uFEB5', '\u0634').replace('\uFEB6', '\u0634').replace('\uFEB7', '\u0634').replace('\uFEB8',
                                                                                                             '\u0634') \
                .replace('\uFEB1', '\u0633').replace('\uFEB2', '\u0633').replace('\uFEB3', '\u0633').replace('\uFEB4',
                                                                                                             '\u0633') \
                .replace('\uFB8A', '\u0698').replace('\uFB8B', '\u0698') \
                .replace('\uFB8C', '\u0691').replace('\uFB8D', '\u0691') \
                .replace('\uFEAD', '\u0631').replace('\uFEAE', '\u0631') \
                .replace('\uFEAB', '\u0630').replace('\uFEAC', '\u0630') \
                .replace('\uFB88', '\u0688').replace('\uFB89', '\u0688') \
                .replace('\uFEA9', '\u062F').replace('\uFEAA', '\u062F') \
                .replace('\uFEAF', '\u0632').replace('\uFEB0', '\u0632') \
                .replace('\uFEA5', '\u062E').replace('\uFEA6', '\u062E').replace('\uFEA7', '\u062E').replace('\uFEA8',
                                                                                                             '\u062E') \
                .replace('\uFEA1', '\u062D').replace('\uFEA2', '\u062D').replace('\uFEA3', '\u062D').replace('\uFEA4',
                                                                                                             '\u062D') \
                .replace('\uFB7A', '\u0686').replace('\uFB7B', '\u0686').replace('\uFB7C', '\u0686').replace('\uFB7D',
                                                                                                             '\u0686') \
                .replace('\uFE9D', '\u062C').replace('\uFE9E', '\u062C').replace('\uFE9F', '\u062C').replace('\uFEA0',
                                                                                                             '\u062C') \
                .replace('\uFE99', '\u062B').replace('\uFE9A', '\u062B').replace('\uFE9B', '\u062B').replace('\uFE9C',
                                                                                                             '\u062B') \
                .replace('\uFB66', '\u0679').replace('\uFB67', '\u0679').replace('\uFB68', '\u0679').replace('\uFB69',
                                                                                                             '\u0679') \
                .replace('\uFE95', '\u062A').replace('\uFE96', '\u062A').replace('\uFE97', '\u062A').replace('\uFE98',
                                                                                                             '\u062A') \
                .replace('\uFB56', '\u067E').replace('\uFB57', '\u067E').replace('\uFB58', '\u067E').replace('\uFB59',
                                                                                                             '\u067E') \
                .replace('\uFE8F', '\u0628').replace('\uFE90', '\u0628').replace('\uFE91', '\u0628').replace('\uFE92',
                                                                                                             '\u0628') \
                .replace('\uFE8D', '\u0627').replace('\uFE8E', '\u0627') \
                .replace('\uFE81', '\u0622').replace('\uFE82', '\u0622') \
                .replace('\uFEE9', '\u0647').replace('\uFEEA', '\u0647').replace('\uFEEB', '\u0647').replace('\uFEEC',
                                                                                                             '\u0647') \
                .replace('\u200f', '')
        else:
            line = line.strip()
        words = regex.split(line.strip())
        # 如果字典里有该单词则加1，否则添加入字典
        for w in words:
            if re.search(WORD_REGEX, w.strip()) is None:
                # print(w)
                if w.strip() in count_dict.keys():
                    count_dict[w] = count_dict[w] + 1
                else:
                    count_dict[w] = 1
            # else:
            #     print(w,re.search(WORD_REGEX, w.strip()))
        # 按照词频从高到低排列
    count_list = sorted(count_dict.items(), key=lambda x: int(x[1]), reverse=True)
    print(WORD_REGEX)
    with open(file_path.replace('.txt', '.wordcount'), 'w', encoding='utf-8') as f_word:
        for l in count_list:
            s1 = str(l[0]) + "\t" + str(l[1])
            alist = [ch for ch in str(l[0].strip()).lower()]
            for letter in alist:
                if re.search(WORD_REGEX, letter) is None:
                    if letter not in letterset:
                        print(letter)
                        letterset.add(letter)
                # else:
                #     print(letter)
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
