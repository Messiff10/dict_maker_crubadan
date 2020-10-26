import re
import sys


def replacePun(file_ori, file_out, WORD_REGEX):
    with open(file_ori, 'r', encoding='utf-8') as f_in:
        with open(file_out, 'w', encoding='utf-8') as f_out:
            for l_in in f_in:
                l_in = l_in.replace("‘", "'").replace("’", "'")
                l_in = re.sub('\s*-\s*', '-', l_in)
                l_in = re.sub(WORD_REGEX, ' ', l_in)
                l_in = re.sub('\s+', ' ', l_in)
                f_out.write(l_in.strip())
                f_out.write('\n')


def getWordPun(language):
    if language == "en_US":
        WORD_REGEX = re.compile(r"[^a-zA-Z0-9-']")
    elif language == "it":
        WORD_REGEX = re.compile(r"[^qwertyuiìíopèéùúasdfghjklòóàzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0-9-']")
    elif language == "fi":
        WORD_REGEX = re.compile(r"[^abcdefghijklmnopqrstuvwxyzåäöABCDEFGHIJKLMNOPQRSTUVWXYZAÅÄOÖ0-9-']")
    elif language == "tr":
        WORD_REGEX = re.compile(r"[^qwertyüuıiöopâaşsdfğghjklzxçcvbnmQWERTYÜUIİÖOPAŞSDFĞGHJKLZXÇCVBNM0-9-']")
    elif language == "ru":
        WORD_REGEX = re.compile(r"[^йцукенгшщзхфывапролджэячсмитьбюЙЦУКЕНГШЩЗХФЫВАПРОЛДЖЭЯЧСМИТЬБЮ0-9-']")
    elif language == "es":
        WORD_REGEX = re.compile(
            r"[^qwėêęēèéëertyūùûüúuīîįìïíiºōœøõôöòóopåąæāªáàäâãasdfghjklñzxčçćcvbñńnmQWĖÊĘĒÈ3ËERTYŪÙÛÜÚUĪÎĮÌÏÍIºŌŒØÕÔÖÒÓOPÅĄÆĀĀÁÀÄÃASDFGHJKLÑZXČÇĆCVBÑŃNM0-9-']")
    elif language == "es_US":
        WORD_REGEX = re.compile(
            r"[^qwėêęēèéëertyūùûüúuīîįìïíiºōœøõôöòóopåąæāªáàäâãasdfghjklñzxčçćcvbñńnmQWĖÊĘĒÈ3ËERTYŪÙÛÜÚUĪÎĮÌÏÍIºŌŒØÕÔÖÒÓOPÅĄÆĀĀÁÀÄÃASDFGHJKLÑZXČÇĆCVBÑŃNM0-9-']")
    elif language == "ms_MY":
        WORD_REGEX = re.compile(r"[^qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0-9-']")
    elif language == "pl":
        WORD_REGEX = re.compile(r"[^aąbcćdeęfghijklłmnńoóprsśtuwyzźżAĄBCĆDEĘFGHIJKLŁMNŃOÓPRSŚTUWYZŹŻ0-9-']")
    elif language == "sv":
        WORD_REGEX = re.compile(r"[^abcdefghijklmnopqrstuvwxyzåäöABCDEFGHIJKLMNOPQRSTUVWXYZAÅÄOÖ0-9-']")
    elif language == "th":
        WORD_REGEX = re.compile(
            r"[^\u0E01\u0E02\u0E03\u0E04\u0E05\u0E06\u0E07\u0E08\u0E09\u0E0A\u0E0B\u0E0C\u0E0D"
            r"\u0E0E\u0E0F\u0E10\u0E11\u0E12\u0E13\u0E14\u0E15\u0E16\u0E17\u0E18\u0E19\u0E1A"
            r"\u0E1B\u0E1C\u0E1D\u0E1E\u0E1F\u0E20\u0E21\u0E22\u0E23\u0E24\u0E25\u0E26\u0E27\u0E28"
            r"\u0E29\u0E2A\u0E2B\u0E2C\u0E2D\u0E2E\u0E2F\u0E30\u0E31\u0E32\u0E33\u0E34\u0E35\u0E36"
            r"\u0E37\u0E38\u0E39\u0E3A\u0E3F\u0E40\u0E41\u0E42\u0E43\u0E44\u0E45\u0E46\u0E47\u0E48"
            r"\u0E49\u0E4A\u0E4B\u0E4C\u0E4D\u0E4E\u0E4F\u0E50\u0E51\u0E52\u0E53\u0E54\u0E55\u0E56"
            r"\u0E57\u0E58\u0E59\u0E5A\u0E5B0-9-']")
    elif language == "ar":
        WORD_REGEX = re.compile(r"[^\s'ضصثقفغعهخحجشسيبلاتنمكطذءؤرىةوزظدئإأآڨڭپڢڤچ]+")
    elif language == "de":
        WORD_REGEX = re.compile(r"[^qwertzuiopüasdfghjklöäyxcvbnmßQWERTZUIOPÜASDFGHJKLÖÄYXCVBNMẞ0-9-']")
    elif language == "da":
        WORD_REGEX = re.compile(r"[^qwertyuiopåasdfghjkløæzxcvbnmQWERTYUIOPÅASDFGHJKLØÆZXCVBNM0-9-']")
    elif language == "nb":
        WORD_REGEX = re.compile(r"[^qwertyuiopåasdfghjkløæzxcvbnmQWERTYUIOPÅASDFGHJKLØÆZXCVBNM0-9-']")
    elif language == "cs":
        WORD_REGEX = re.compile(
            r"[^aábcčdďeéěfghchiíjklmnňoópqrřsštťuúůvwxyýzžAÁBCČDĎEÉĚFGHChIÍJKLMNŇOÓPQRŘSŠTŤUÚŮVWXYÝZŽ0-9-']")
    elif language == "ur":
        WORD_REGEX = re.compile(r"[^ےیءھہونملگکقفغعظطضصشسژڑرذڈدخحچجثٹتپباآ0-9-']")
    elif language == "ko":
        WORD_REGEX = re.compile(r"[^ㅂㄷㅈㄱㅃㄸㅉㄲㅍㅌㅊㅋㅅㅎㅆㅁㄴㅇㄹㅣㅔㅚㅐㅏㅗㅜㅓㅡㅢㅖㅒㅑㅛㅠㅕㅟㅞㅙㅘㅝ0-9-']")
    elif language == "fr":
        WORD_REGEX = re.compile(
            r"[^éèêëcçàâæazertyÿuiîïoôœpqsdfghjklmùûüwxcvbnAÀÆZEÉÈÊËCÇRTYŸUÛÜIÎÏOÔŒPQSDFGHJKLMWXCVBN0-9-']")
    elif language == "fa":
        WORD_REGEX = re.compile(r"[^ضصثقفغعهةه‍هٔخحجشسیىئيبلٱءآأإاةتنمكکگظطژزرذدپؤوچ0-9-']")
    elif language == "in":
        WORD_REGEX = re.compile(r"[^AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0-9-']")
    elif language == "jv":
        WORD_REGEX = re.compile(r"[^AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0-9-']")
    elif language == "fil":
        WORD_REGEX = re.compile(r"[^AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0-9-']")
    elif language == "yi":
        WORD_REGEX = re.compile(r"[^אאַאָבבּבֿגדדזשהווּוֹװויזזשחטטשייִייײַכּכךלמםנןסעפּפֿפףצץקרששׂתּת0-9-']")
    elif language == "pt_BR":
        WORD_REGEX = re.compile(
            r"[^aáàãâbcçdeéêfghiíjklmnoóõôpqrstuúüvwxyzAÁÀÃBCÇDEÉÊFGHIÍJKLMNOÓÕÔPQRSTUÚÜVWXYZ0-9-']")
    elif language == "su":
        WORD_REGEX = re.compile(r"[^AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0-9-']")
    elif language == "vi":
        WORD_REGEX = re.compile(r"[^AaĂăâBbCcDdĐđEeÊêGgHhIiKkLlMmNnOoÔôƠơPpQqRrSsTtUuƯưVvXxYy0-9-']")
    elif language == "hi":
        WORD_REGEX = re.compile(r"[^\u0900-\u097f0-9-']")
    elif language == "ro":
        WORD_REGEX = re.compile(
            r"[^qwertțyuīíįìïîopâãăàáäæåāaśșßšsdfghjklzxcvbnmQWERTȚYUIĪÍĮÌÏÎOPÄÆÅĀÃĂÀÁASŚȘSSŠDFGHJKLZXCVBNM0-9-']")
    elif language == "hu":
        WORD_REGEX = re.compile(
            r"[^qwėëęęèéêertzuûùūüúűiīìįïîíiōøœõòôőöóopæãåāáàâäasdfghjklyxcvbnmQWĖËĘĒÈÉÊERTZÛÙŪÜÚŰUĪÌĮÏÎÍIØØŒÕÒÔŐÖÓOPÆÃÅĀÁÀÄASDFGHJKLYXCVBNM0-9-']")
    elif language == "uk":
        WORD_REGEX = re.compile(r"[^йцукенґгшщзхфїівапролджєячсмитъьбюЙЦУКЕНГШЩЗХФЇІВАПРОЛДЖЄЯЧСМИТЪЬБЮ0-9-']")
    elif language == "pt_PT":
        WORD_REGEX = re.compile(
            r"[^aáàãâbcçdeéêfghiíjklmnoóõôpqrstuúüvwxyzAÁÀÃBCÇDEÉÊFGHIÍJKLMNOÓÕÔPQRSTUÚÜVWXYZ0-9-']")
    elif language == "kk":
        WORD_REGEX = re.compile(
            r"[^йцұүукқеёнңгғшщзхһфыівәапрөолджэячсмитъьбюЙЦҰҮУҚКЁЕҢНҒГШЩЗҺХФІЫВӘАПРӨОЛДЖЭЯЧСМИТЪЬБЮ0-9-']")
    elif language == "hi_HINGLISH":
        WORD_REGEX = re.compile(r"[^a-zA-Z0-9-']")
    elif language == "ur":
        WORD_REGEX = re.compile(r"[^قوعرتےءیهپلکجحگفدسازشچطبنمؤٰڑہٹَأئةۀُخضھغًڈصہآذژثظِںّ0-9-']")
    return WORD_REGEX


if __name__ == '__main__':
    language = sys.argv[1]
    file_ori = sys.argv[2]
    file_out = sys.argv[3]
    WORD_REGEX = getWordPun(language)
    replacePun(file_ori, file_out, WORD_REGEX)
    print("FINISH LINE")
