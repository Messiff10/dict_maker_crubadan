import re
"""
将爬取词典（去掉单个字母）和比较为true的部分合并
"""
language = "ro"
inputpath = "/Users/ff/Desktop/第一优先级语言词表/desc/wy筛选词表/" + language + "_dict_uniq.txt"
unigrampath = "/Users/ff/Desktop/第一优先级语言词表/desc/wy筛选词表/" + language + "_true_unigram.txt"
outpath = "/Users/ff/Desktop/第一优先级语言词表/desc/wy筛选词表/" + language + "_unigram"

unigram = set()
unigramfreq = set()

# language = sys.argv[1]
if language == "en_US":
    WORD_REGEX = re.compile(r"[^a-zA-Z']")
elif language == "it":
    WORD_REGEX = re.compile(r"[^qwertyuiìíopèéùúasdfghjklòóàzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM']")
elif language == "fi":
    WORD_REGEX = re.compile(r"[^abcdefghijklmnopqrstuvwxyzåäöABCDEFGHIJKLMNOPQRSTUVWXYZAÅÄOÖ']")
elif language == "tr":
    WORD_REGEX = re.compile(r"[^ertyuıopğüasdfghjklşizcvbnmöçERTYUIOPĞÜASDFGHJKLŞİZCVBNMÖÇ']")
elif language == "ru":
    WORD_REGEX = re.compile(r"[^йцукенгшщзхфывапролджэячсмитьбюЙЦУКЕНГШЩЗХФЫВАПРОЛДЖЭЯЧСМИТЬБЮ']")
elif language == "es":
    WORD_REGEX = re.compile(r"[^qwertyuiopasdfghjklñzxcvbnmQWERTYUIOPASDFGHJKLÑZXCVBNM']")
elif language == "es_US":
    WORD_REGEX = re.compile(r"[^qwertyuiopasdfghjklñzxcvbnmQWERTYUIOPASDFGHJKLÑZXCVBNM']")
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
    WORD_REGEX = re.compile(r"[^aábcčdďeéěfghchiíjklmnňoópqrřsštťuúůvwxyýzžAÁBCČDĎEÉĚFGHChIÍJKLMNŇOÓPQRŘSŠTŤUÚŮVWXYÝZŽ']")
elif language == "ur":
    WORD_REGEX = re.compile(r"[^ےیءھہونملگکقفغعظطضصشسژڑرذڈدخحچجثٹتپباآ']")
elif language == "ko":
    WORD_REGEX = re.compile(r"[^ㅂㄷㅈㄱㅃㄸㅉㄲㅍㅌㅊㅋㅅㅎㅆㅁㄴㅇㄹㅣㅔㅚㅐㅏㅗㅜㅓㅡㅢㅖㅒㅑㅛㅠㅕㅟㅞㅙㅘㅝ']")
elif language == "fr":
    WORD_REGEX = re.compile(r"[^éèêëcçàâæazertyÿuiîïoôœpqsdfghjklmùûüwxcvbnAÀÆZEÉÈÊËCÇRTYŸUÛÜIÎÏOÔŒPQSDFGHJKLMWXCVBN']")
elif language == "nl":
    WORD_REGEX = re.compile(r"[^qweéërtyuüiïoóöpasdfghjklzxcvbnmQWEÉËRTYUÜIÏOÓÖPASDFGHJKLZXCVBNM']")
elif language == "kk":
    WORD_REGEX = re.compile(r"[^йцуұүкқеёнңгғшщзхфыіваәпроөлджэһячсмитьъбю']")
elif language == "pt_BR":
    WORD_REGEX = re.compile(r"[^aáàãâbcçdeéêfghiíjklmnoóõôpqrstuúüvwxyzAÁÀÃBCÇDEÉÊFGHIÍJKLMNOÓÕÔPQRSTUÚÜVWXYZ']")
elif language == "pt_PT":
    WORD_REGEX = re.compile(r"[^aáàãâbcçdeéêfghiíjklmnoóõôpqrstuúüvwxyzAÁÀÃBCÇDEÉÊFGHIÍJKLMNOÓÕÔPQRSTUÚÜVWXYZ']")
elif language == "ro":
    WORD_REGEX = re.compile(r"[^qwertțyuīíįìïîopâãăàáäæåāaśșßšsdfghjklzxcvbnmQWERTȚYUIĪÍĮÌÏÎOPÄÆÅĀÃĂÀÁASŚȘSSŠDFGHJKLZXCVBNM']")
elif language == "uk":
    WORD_REGEX = re.compile(r"[^АаБбВвГгҐґДдЕеЄєЖжЗзИиІіЇїЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЬьЮюЯя']")
elif language == "hu":
    WORD_REGEX = re.compile(r"[^AaÁáBbCcDdEeÉéFfGgHhIiÍíJjKkLlMmNnOoÓóÖöŐPpQqRrSsTtUuÚúÜüŰűVvWwXxYyZz']")


def getunigram(input):
    with open(input, 'r', encoding='utf-8') as f_unigram:
        for line in f_unigram:
            words = line.strip().split('\t')
            if words[0].strip() not in unigram:
                # words[0] = "".join(filter(str.isalpha, words[0]))
                unigram.add(words[0].strip())
    print("getunigram finish")
    # unigramfreq.add((words[0].strip(), words[1].strip()))


def ifcontains(input):
    with open(input, 'r', encoding='utf-8') as f_input:
        for lin in f_input:
            lin = lin.strip()
            if len(lin) >= 2:
                if lin.strip() not in unigram and len(re.findall(WORD_REGEX, lin.strip())) == 0:
                    lin = re.sub('\s+', ' ', lin.strip())
                    # lin = re.sub('[^\w+]', '', lin)
                    unigram.add(lin.strip())

    print("ifcontains finish")


def getout(out):
    with open(out, 'w', encoding='utf-8') as f_out:
        for ll in unigram:
            f_out.write(ll.strip())
            f_out.write('\n')
    print("getout finish")


if __name__ == '__main__':
    getunigram(unigrampath)
    ifcontains(inputpath)
    getout(outpath)
    print("Finish line")
