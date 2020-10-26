import re
import sys
"""
生成gpt2训练语料
字母id|#|单词id
"""
file_original = "/data/zzf/language/en_US/train_data/train_data_en_US_user_web_shuf_case_mapletters_space_gpt2/"
file_vocab = file_original+"vocab_out"
file_letter = file_original+"vocab_in_letters"
file_und = "/data/zzf/language/en_US/train_data/en_US_user_web_nospace_shuf_case.true"
file_out = "/data/zzf/language/en_US/train_data/train_data_en_US_user_web_shuf_case_mapletters_space_gpt2_2/"
file_vocab_out = file_out+"vocab_out"
file_vocab_letter = file_out+"vocab_in_letters"
wordsDict = {}
lettersDict = {}
undSet = set()
regex = re.compile('\s+')
split_PUN = "<b>"
space_PUN = " "
PUN_REREX_SPACE = re.compile("([a-zA-Z']+)([^a-zA-Z']+$)")

## 结果 格式说明 g e t a l l t h e  l a t e s t|#|get all the latest 转换成对应的id

def getword(language):
    if language == "en_US":
        WORD_REGEX = re.compile(r"[a-zA-Z']+")
        NUM_REGEX = re.compile(r"[+-]*[0-9]+.*[0-9]*")
        PUN_REREX = re.compile(r"[^a-zA-Z0-9']")
    if language == "es_US":
        WORD_REGEX = re.compile(r"[qwertyuiopasdfghjklñzxcvbnmQWERTYUIOPASDFGHJKLÑZXCVBNM']+")
        NUM_REGEX = re.compile(r"[+-]*[0-9]+.*[0-9]*")
        PUN_REREX = re.compile(r"[^qwertyuiopasdfghjklñzxcvbnmQWERTYUIOPASDFGHJKLÑZXCVBNM0-9']")
    if language == "sv":
        WORD_REGEX = re.compile(r"[abcdefghijklmnopqrstuvwxyzåäöABCDEFGHIJKLMNOPQRSTUVWXYZAÅÄOÖ']+")
        NUM_REGEX = re.compile(r"[+-]*[0-9]+.*[0-9]*")
        PUN_REREX = re.compile(r"[^abcdefghijklmnopqrstuvwxyzåäöABCDEFGHIJKLMNOPQRSTUVWXYZAÅÄOÖ0-9']")
    if language == "de":
        WORD_REGEX = re.compile(r"[qwertzuiopüasdfghjklöäyxcvbnmßQWERTZUIOPÜASDFGHJKLÖÄYXCVBNMẞ']+")
        NUM_REGEX = re.compile(r"[+-]*[0-9]+.*[0-9]*")
        PUN_REREX = re.compile(r"[^qwertzuiopüasdfghjklöäyxcvbnmßQWERTZUIOPÜASDFGHJKLÖÄYXCVBNMẞ0-9']")
    if language == "ms_MY":
        WORD_REGEX = re.compile(r"[qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM']+")
        NUM_REGEX = re.compile(r"[+-]*[0-9]+.*[0-9]*")
        PUN_REREX = re.compile(r"[^qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0-9']")
    if language == "nb":
        WORD_REGEX = re.compile(r"[qwertyuiopåasdfghjkløæzxcvbnmQWERTYUIOPÅASDFGHJKLØÆZXCVBNM']+")
        NUM_REGEX = re.compile(r"[+-]*[0-9]+.*[0-9]*")
        PUN_REREX = re.compile(r"[^qwertyuiopåasdfghjkløæzxcvbnmQWERTYUIOPÅASDFGHJKLØÆZXCVBNM0-9']")
    if language == "th":
        WORD_REGEX = re.compile(
            r"[\\u0E01\\u0E02\\u0E03\\u0E04\\u0E05\\u0E06\\u0E07\\u0E08\\u0E09\\u0E0A\\u0E0B\\u0E0C\\u0E0D\\u0E0E\\u0E0F\\u0E10\\u0E11\\u0E12\\u0E13\\u0E14\\u0E15\\u0E16\\u0E17\\u0E18\\u0E19\\u0E1A\\u0E1B\\u0E1C\\u0E1D\\u0E1E\\u0E1F\\u0E20\\u0E21\\u0E22\\u0E23\\u0E24\\u0E25\\u0E26\\u0E27\\u0E28\\u0E29\\u0E2A\\u0E2B\\u0E2C\\u0E2D\\u0E2E\\u0E2F\\u0E30\\u0E31\\u0E32\\u0E33\\u0E34\\u0E35\\u0E36\\u0E37\\u0E38\\u0E39\\u0E3A\\u0E3F\\u0E40\\u0E41\\u0E42\\u0E43\\u0E44\\u0E45\\u0E46\\u0E47\\u0E48\\u0E49\\u0E4A\\u0E4B\\u0E4C\\u0E4D\\u0E4E\\u0E4F\\u0E50\\u0E51\\u0E52\\u0E53\\u0E54\\u0E55\\u0E56\\u0E57\\u0E58\\u0E59\\u0E5A\\u0E5B']+")
        NUM_REGEX = re.compile(r"[+-]*[0-9]+.*[0-9]*")
        PUN_REREX = re.compile(
            r"[^\\u0E01\\u0E02\\u0E03\\u0E04\\u0E05\\u0E06\\u0E07\\u0E08\\u0E09\\u0E0A\\u0E0B\\u0E0C\\u0E0D\\u0E0E\\u0E0F\\u0E10\\u0E11\\u0E12\\u0E13\\u0E14\\u0E15\\u0E16\\u0E17\\u0E18\\u0E19\\u0E1A\\u0E1B\\u0E1C\\u0E1D\\u0E1E\\u0E1F\\u0E20\\u0E21\\u0E22\\u0E23\\u0E24\\u0E25\\u0E26\\u0E27\\u0E28\\u0E29\\u0E2A\\u0E2B\\u0E2C\\u0E2D\\u0E2E\\u0E2F\\u0E30\\u0E31\\u0E32\\u0E33\\u0E34\\u0E35\\u0E36\\u0E37\\u0E38\\u0E39\\u0E3A\\u0E3F\\u0E40\\u0E41\\u0E42\\u0E43\\u0E44\\u0E45\\u0E46\\u0E47\\u0E48\\u0E49\\u0E4A\\u0E4B\\u0E4C\\u0E4D\\u0E4E\\u0E4F\\u0E50\\u0E51\\u0E52\\u0E53\\u0E54\\u0E55\\u0E56\\u0E57\\u0E58\\u0E59\\u0E5A\\u0E5B0-9']")
    if language == "ar":
        WORD_REGEX = re.compile(r"['ضصثقفغعهخحجشسيبلاتنمكطذءؤرىةوزظدئإأآڨڭپڢڤچ]+")
        NUM_REGEX = re.compile(r"[٠0١1٢2٣3٤4٥5٦6٧7٨8٩9]+")
        PUN_REREX = re.compile(r"[^'ضصثقفغعهخحجشسيبلاتنمكطذءؤرىةوزظدئإأآڨڭپڢڤچ٠0١1٢2٣3٤4٥5٦6٧7٨8٩9]")
    if language == "fi":
        WORD_REGEX = re.compile(r"[abcdefghijklmnopqrstuvwxyzåäöABCDEFGHIJKLMNOPQRSTUVWXYZAÅÄOÖ']+")
        NUM_REGEX = re.compile(r"[+-]*[0-9]+.*[0-9]*")
        PUN_REREX = re.compile(r"[^abcdefghijklmnopqrstuvwxyzåäöABCDEFGHIJKLMNOPQRSTUVWXYZAÅÄOÖ0-9']")
    if language == "it":
        WORD_REGEX = re.compile(r"[qwertyuiìíopèéùúasdfghjklòóàzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM']+")
        NUM_REGEX = re.compile(r"[+-]*[0-9]+.*[0-9]*")
        PUN_REREX = re.compile(r"[^qwertyuiìíopèéùúasdfghjklòóàzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0-9']")
    if language == "ru":
        WORD_REGEX = re.compile(r"[йцукенгшщзхфывапролджэячсмитьбюЙЦУКЕНГШЩЗХФЫВАПРОЛДЖЭЯЧСМИТЬБЮ']+")
        NUM_REGEX = re.compile(r"[+-]*[0-9]+.*[0-9]*")
        PUN_REREX = re.compile(r"[^йцукенгшщзхфывапролджэячсмитьбюЙЦУКЕНГШЩЗХФЫВАПРОЛДЖЭЯЧСМИТЬБЮ0-9']")
    if language == "tr":
        WORD_REGEX = re.compile(r"[ertyuıopğüasdfghjklşizcvbnmöçERTYUIOPĞÜASDFGHJKLŞİZCVBNMÖÇ']+")
        NUM_REGEX = re.compile(r"[+-]*[0-9]+.*[0-9]*")
        PUN_REREX = re.compile(r"[^ertyuıopğüasdfghjklşizcvbnmöçERTYUIOPĞÜASDFGHJKLŞİZCVBNMÖÇ0-9']")
    if language == "pl":
        WORD_REGEX = re.compile(r"[aąbcćdeęfghijklłmnńoóprsśtuwyzźżAĄBCĆDEĘFGHIJKLŁMNŃOÓPRSŚTUWYZŹŻ']+")
        NUM_REGEX = re.compile(r"[+-]*[0-9]+.*[0-9]*")
        PUN_REREX = re.compile(r"[^aąbcćdeęfghijklłmnńoóprsśtuwyzźżAĄBCĆDEĘFGHIJKLŁMNŃOÓPRSŚTUWYZŹŻ0-9']")
    if language == "tr":
        WORD_REGEX = re.compile(r"[ertyuıopğüasdfghjklşizcvbnmöçERTYUIOPĞÜASDFGHJKLŞİZCVBNMÖÇ']+")
        NUM_REGEX = re.compile(r"[+-]*[0-9]+.*[0-9]*")
        PUN_REREX = re.compile(r"[^ertyuıopğüasdfghjklşizcvbnmöçERTYUIOPĞÜASDFGHJKLŞİZCVBNMÖÇ0-9']")
    if language == "ru":
        WORD_REGEX = re.compile(r"[йцукенгшщзхфывапролджэячсмитьбюЙЦУКЕНГШЩЗХФЫВАПРОЛДЖЭЯЧСМИТЬБЮ']+")
        NUM_REGEX = re.compile(r"[+-]*[0-9]+.*[0-9]*")
        PUN_REREX = re.compile(r"[^йцукенгшщзхфывапролджэячсмитьбюЙЦУКЕНГШЩЗХФЫВАПРОЛДЖЭЯЧСМИТЬБЮ0-9']")
    if language == "ur":
        WORD_REGEX = re.compile(r"[ےیءھہونملگکقفغعظطضصشسژڑرذڈدخحچجثٹتپباآ']+")
        NUM_REGEX = re.compile(r"[+-]*[0-9]+.*[0-9]*")
        PUN_REREX = re.compile(r"[^ےیءھہونملگکقفغعظطضصشسژڑرذڈدخحچجثٹتپباآ0-9']")
    if language == "cs":
        WORD_REGEX = re.compile(
            r"[aábcčdďeéěfghchiíjklmnňoópqrřsštťuúůvwxyýzžAÁBCČDĎEÉĚFGHChIÍJKLMNŇOÓPQRŘSŠTŤUÚŮVWXYÝZŽ']+")
        NUM_REGEX = re.compile(r"[+-]*[0-9]+.*[0-9]*")
        PUN_REREX = re.compile(
            r"[^aábcčdďeéěfghchiíjklmnňoópqrřsštťuúůvwxyýzžAÁBCČDĎEÉĚFGHChIÍJKLMNŇOÓPQRŘSŠTŤUÚŮVWXYÝZŽ0-9']")
    if language == "ko":
        WORD_REGEX = re.compile(r"[ㅂㄷㅈㄱㅃㄸㅉㄲㅍㅌㅊㅋㅅㅎㅆㅁㄴㅇㄹㅣㅔㅚㅐㅏㅗㅜㅓㅡㅢㅖㅒㅑㅛㅠㅕㅟㅞㅙㅘㅝ']+")
        NUM_REGEX = re.compile(r"[+-]*[0-9]+.*[0-9]*")
        PUN_REREX = re.compile(r"[^ㅂㄷㅈㄱㅃㄸㅉㄲㅍㅌㅊㅋㅅㅎㅆㅁㄴㅇㄹㅣㅔㅚㅐㅏㅗㅜㅓㅡㅢㅖㅒㅑㅛㅠㅕㅟㅞㅙㅘㅝ0-9']")
    if language == "fr":
        WORD_REGEX = re.compile(
            r"[éèêëcçàâæazertyÿuiîïoôœpqsdfghjklmùûüwxcvbnAÀÆZEÉÈÊËCÇRTYŸUÛÜIÎÏOÔŒPQSDFGHJKLMWXCVBN']+")
        NUM_REGEX = re.compile(r"[+-]*[0-9]+.*[0-9]*")
        PUN_REREX = re.compile(
            r"[^éèêëcçàâæazertyÿuiîïoôœpqsdfghjklmùûüwxcvbnAÀÆZEÉÈÊËCÇRTYŸUÛÜIÎÏOÔŒPQSDFGHJKLMWXCVBN0-9']")
    if language == "fa":
        WORD_REGEX = re.compile(r"[ضصثقفغعهةه\u200Dهٔخحجشسیىئيبلٱءآأإاةتنمكکگظطژزرذدپؤوچ']+")
        NUM_REGEX = re.compile(r"[+-]*[0-9]+.*[0-9]*۱۲۳۴۵۶۷۸۹۰")
        PUN_REREX = re.compile(r"[^0-9ضصثقفغعهةه\u200Dهٔخحجشسیىئيبلٱءآأإاةتنمكکگظطژزرذدپؤوچ۱۲۳۴۵۶۷۸۹۰']")
    if language == "印尼":
        WORD_REGEX = re.compile(r"[AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz']+")
        NUM_REGEX = re.compile(r"[+-]*[0-9]+.*[0-9]*")
        PUN_REREX = re.compile(r"[^AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0-9']")
    if language == "fil":
        WORD_REGEX = re.compile(r"[AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz']+")
        NUM_REGEX = re.compile(r"[+-]*[0-9]+.*[0-9]*")
        PUN_REREX = re.compile(r"[^AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0-9']")
    if language == "jv":
        WORD_REGEX = re.compile(r"[AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz']+")
        NUM_REGEX = re.compile(r"[+-]*[0-9]+.*[0-9]*")
        PUN_REREX = re.compile(r"[^AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0-9']")
    if language == "pt_BR":
        WORD_REGEX = re.compile(r"[aáàãâbcçdeéêfghiíjklmnoóõôpqrstuúüvwxyzAÁÀÃBCÇDEÉÊFGHIÍJKLMNOÓÕÔPQRSTUÚÜVWXYZ']+")
        NUM_REGEX = re.compile(r"[+-]*[0-9]+.*[0-9]*")
        PUN_REREX = re.compile(r"[^aáàãâbcçdeéêfghiíjklmnoóõôpqrstuúüvwxyzAÁÀÃBCÇDEÉÊFGHIÍJKLMNOÓÕÔPQRSTUÚÜVWXYZ0-9']")
    if language == "su":
        WORD_REGEX = re.compile(r"[AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz']+")
        NUM_REGEX = re.compile(r"[+-]*[0-9]+.*[0-9]*")
        PUN_REREX = re.compile(r"[^AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0-9']")
    if language == "vi":
        WORD_REGEX = re.compile(
            r"[qweễếểệêẽẹềéèẻrtyỵỷỹýỳuữứửựưũụừúùủiịỉĩíìoợỡởớờơộỗổốồôọõỏóòpaẫậặâầấẩăằắẳẵàáảãạsdđfghjklzxcvbnm']+")
        NUM_REGEX = re.compile(r"[+-]*[0-9]+.*[0-9]*")
        PUN_REREX = re.compile(
            r"[^qweễếểệêẽẹềéèẻrtyỵỷỹýỳuữứửựưũụừúùủiịỉĩíìoợỡởớờơộỗổốồôọõỏóòpaẫậặâầấẩăằắẳẵàáảãạsdđfghjklzxcvbnm0-9']")
    if language == "hi":
        WORD_REGEX = re.compile(r"[\\u0900-\\u097f']+")
        NUM_REGEX = re.compile(r"[+-]*[0-9]+.*[0-9]*")
        PUN_REREX = re.compile(r"[^\\u0900-\\u097f0-9']")
    if language == "ro":
        WORD_REGEX = re.compile(
            r"[qwertțyuīíįìïîopâãăàáäæåāaśșßšsdfghjklzxcvbnmQWERTȚYUIĪÍĮÌÏÎOPÄÆÅĀÃĂÀÁASŚȘSSŠDFGHJKLZXCVBNM']+")
        NUM_REGEX = re.compile(r"[+-]*[0-9]+.*[0-9]*")
        PUN_REREX = re.compile(
            r"[^qwertțyuīíįìïîopâãăàáäæåāaśșßšsdfghjklzxcvbnmQWERTȚYUIĪÍĮÌÏÎOPÄÆÅĀÃĂÀÁASŚȘSSŠDFGHJKLZXCVBNM0-9']")
    if language == "hu":
        WORD_REGEX = re.compile(r"[AaÁáBbCcDdEeÉéFfGgHhIiÍíJjKkLlMmNnOoÓóÖöŐPpQqRrSsTtUuÚúÜüŰűVvWwXxYyZz']+")
        NUM_REGEX = re.compile(r"[+-]*[0-9]+.*[0-9]*")
        PUN_REREX = re.compile(r"[^AaÁáBbCcDdEeÉéFfGgHhIiÍíJjKkLlMmNnOoÓóÖöŐPpQqRrSsTtUuÚúÜüŰűVvWwXxYyZz0-9']")
    if language == "uk":
        WORD_REGEX = re.compile(r"[аБбВвГгҐґДдЕеЄєЖжЗзИиІіЇїЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЬьЮюЯя']+")
        NUM_REGEX = re.compile(r"[+-]*[0-9]+.*[0-9]*")
        PUN_REREX = re.compile(r"[^аБбВвГгҐґДдЕеЄєЖжЗзИиІіЇїЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЬьЮюЯя0-9']")
    if language == "kk":
        WORD_REGEX = re.compile(r"[йцуұүкқеёнңгғшщзхфыіваәпроөлджэһячсмитьъбю']+")
        NUM_REGEX = re.compile(r"[+-]*[0-9]+.*[0-9]*")
        PUN_REREX = re.compile(r"[^йцуұүкқеёнңгғшщзхфыіваәпроөлджэһячсмитьъбю0-9']")
    if language == "nl":
        WORD_REGEX = re.compile(r"[qweéërtyuüiïoóöpasdfghjklzxcvbnmQWEÉËRTYUÜIÏOÓÖPASDFGHJKLZXCVBNM']+")
        NUM_REGEX = re.compile(r"[+-]*[0-9]+.*[0-9]*")
        PUN_REREX = re.compile(r"[^qweéërtyuüiïoóöpasdfghjklzxcvbnmQWEÉËRTYUÜIÏOÓÖPASDFGHJKLZXCVBNM0-9']")
    return WORD_REGEX, NUM_REGEX, PUN_REREX


def getvocab(vocab, vocab_out):
    with open(vocab, 'r', encoding='utf-8') as f_in:
        for line in f_in:
            words_ = line.strip().split('##')
            if words_[0].strip() not in wordsDict.keys():
                wordsDict[words_[0]] = int(words_[1])
            else:
                continue
    with open(vocab_out, 'w', encoding='utf-8') as f_out:
        for l in sorted(wordsDict.items(), key=lambda x: int(x[1])):
            result = l[0] + "##" + str(l[1])
            f_out.write(str(result).strip())
            f_out.write('\n')
    print("wordsDict size", len(wordsDict.keys()))


def getletter(letter, letter_out):
    with open(letter, 'r', encoding='utf-8') as f_in:
        for line in f_in:
            letters_ = line.strip().split('##')
            if letters_[0].strip() not in lettersDict.keys():
                lettersDict[letters_[0]] = int(letters_[1])
            else:
                continue
    with open(letter_out, 'w', encoding='utf-8') as f_out:
        for l in sorted(lettersDict.items(), key=lambda x: int(x[1])):
            result = l[0] + "##" + str(l[1])
            f_out.write(str(result).strip())
            f_out.write('\n')
    print("letterDict size", len(lettersDict.keys()))


def getoriginal(file, file_out):
    fils = ["test_data", "train_data", "dev_data"]
    for f in fils:
        with open(file + f, 'r', encoding='utf-8') as f_in:
            with open(file_out + f, 'w', encoding='utf-8') as f_out:
                for line in f_in:
                    resultLetter = []
                    resultWord = []
                    letters_words = line.strip().split('|#|')
                    letters = letters_words[0].split('\t')
                    words = letters_words[1].split('\t')
                    for letter in letters:
                        lineLetter = []
                        if len(letter) == 1:
                            if letter in lettersDict.keys():
                                resultLetter.append(str(lettersDict[letter]))
                                # lineLetter.append()
                            else:
                                resultLetter.append(str(lettersDict["<unk>"]))
                        else:
                            for l in regex.split(letter):
                                if l in lettersDict.keys():
                                    lineLetter.append(str(lettersDict[l]))
                                else:
                                    lineLetter.append(str(lettersDict["<unk>"]))
                            resultLetter.append(" ".join(lineLetter))
                    for w in words:
                        # w_ori = w
                        ## 当数据是标点和单词间不加空格的话，则只去标点前的单词部分进行比较
                        # w = re.sub(PUN_REREX_SPACE, lambda x: x.group(1), w)
                        if w in wordsDict.keys():
                            resultWord.append(str(wordsDict[w]))
                        elif w in undSet:
                            resultWord.append(str(wordsDict["<und>"]))
                        else:
                            resultWord.append(str(wordsDict["<unk>"]))
                    # print("\t".join(resultLetter) + "|#|" + "\t".join(resultWord))
                    f_out.write("\t".join(resultLetter) + "|#|" + "\t".join(resultWord))
                    f_out.write('\n')
                    # newline += 1


def getund(file_und):
    with open(file_und, 'r', encoding='utf-8') as f_in:
        for line in f_in:
            words = line.strip().split('\t')
            if words[0].strip() not in wordsDict.keys() and words[0].strip() not in undSet:
                undSet.add(words[0])
    print("undDict size", len(undSet))


if __name__ == '__main__':
    # language = sys.argv[]
    getund(file_und)
    getletter(file_letter, file_vocab_letter)
    getvocab(file_vocab, file_vocab_out)
    # WORD_REGEX, NUM_REGEX, PUN_REGEX = getword(language)
    getoriginal(file_original, file_out)
