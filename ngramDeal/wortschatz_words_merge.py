# -*- coding: utf-8 -*-
import re
import string
# from utils.language_filter import is_latin__all
language=""
out_file_path = '/Users/xinmei/Downloads/其他语种/mt马耳他语/unigram/mt_unigram'
"""
网上词典处理
wordschatz
"""
out_file = open(out_file_path, 'w')
def getlanguage(language):
    if language == "en_US":
        INVALID_LETTERS = r"[^a-zA-Z\-']"
    elif language == "it":
        INVALID_LETTERS = r"[^qwertyuiìíopèéùúasdfghjklòóàzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM\-']"
    elif language == "fi":
        INVALID_LETTERS = r"[^abcdefghijklmnopqrstuvwxyzåäöABCDEFGHIJKLMNOPQRSTUVWXYZAÅÄOÖ\-']"
    elif language == "tr":
        INVALID_LETTERS = r"[^ertyuıopğüasdfghjklşizcvbnmöçERTYUIOPĞÜASDFGHJKLŞİZCVBNMÖÇ\-']"
    elif language == "ru":
        INVALID_LETTERS = r"[^йцукенгшщзхфывапролджэячсмитьбюЙЦУКЕНГШЩЗХФЫВАПРОЛДЖЭЯЧСМИТЬБЮ\-']"
    elif language == "es":
        INVALID_LETTERS = r"[^qwertyuiopasdfghjklñzxcvbnmQWERTYUIOPASDFGHJKLÑZXCVBNM\-']"
    elif language == "es_US":
        INVALID_LETTERS = r"[^qwertyuiopasdfghjklñzxcvbnmQWERTYUIOPASDFGHJKLÑZXCVBNM\-']"
    elif language == "ms_MY":
        INVALID_LETTERS = r"[^qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM\-']"
    elif language == "pl":
        INVALID_LETTERS = r"[^aąbcćdeęfghijklłmnńoóprsśtuwyzźżAĄBCĆDEĘFGHIJKLŁMNŃOÓPRSŚTUWYZŹŻ\-']"
    elif language == "sv":
        INVALID_LETTERS = r"[^abcdefghijklmnopqrstuvwxyzåäöABCDEFGHIJKLMNOPQRSTUVWXYZAÅÄOÖ\-']"
    elif language == "ar":
        INVALID_LETTERS = r"[^'ضصثقفغعهخحجشسيبلاتنمكطذءؤرىةوزظدئإأآڨڭپڢڤچ]"
    elif language == "de":
        INVALID_LETTERS = r"[^qwertzuiopüasdfghjklöäyxcvbnmßQWERTZUIOPÜASDFGHJKLÖÄYXCVBNMẞ\-']"
    elif language == "da":
        INVALID_LETTERS = r"[^qwertyuiopåasdfghjkløæzxcvbnmQWERTYUIOPÅASDFGHJKLØÆZXCVBNM\-']"
    elif language == "nb":
        INVALID_LETTERS = r"[^qwertyuiopåasdfghjkløæzxcvbnmQWERTYUIOPÅASDFGHJKLØÆZXCVBNM\-']"
    elif language == "cs":
        INVALID_LETTERS = r"[^aábcčdďeéěfghchiíjklmnňoópqrřsštťuúůvwxyýzžAÁBCČDĎEÉĚFGHChIÍJKLMNŇOÓPQRŘSŠTŤUÚŮVWXYÝZŽ\-']"
    elif language == "ur":
        INVALID_LETTERS = r"[^ےیءھہونملگکقفغعظطضصشسژڑرذڈدخحچجثٹتپباآ\-']"
    elif language == "ko":
        INVALID_LETTERS = r"[^ㅂㄷㅈㄱㅃㄸㅉㄲㅍㅌㅊㅋㅅㅎㅆㅁㄴㅇㄹㅣㅔㅚㅐㅏㅗㅜㅓㅡㅢㅖㅒㅑㅛㅠㅕㅟㅞㅙㅘㅝ\-']"
    elif language == "fr":
        INVALID_LETTERS = r"[^éèêëcçàâæazertyÿuiîïoôœpqsdfghjklmùûüwxcvbnAÀÆZEÉÈÊËCÇRTYŸUÛÜIÎÏOÔŒPQSDFGHJKLMWXCVBN\-']"
    elif language == "be":
        INVALID_LETTERS = r"[^абвгдеёжзійклмнопрстуўфхцчшыьэюяАБВГДЕЁЖЗІЙКЛМНОПРСТУЎФХЦЧШЫЬЭЮЯ\-']"
    elif language == "th":
        INVALID_LETTERS = r"[^\u0E01\u0E02\u0E03\u0E04\u0E05\u0E06\u0E07\u0E08\u0E09\u0E0A\u0E0B\u0E0C\u0E0D" \
                          r"\u0E0E\u0E0F\u0E10\u0E11\u0E12\u0E13\u0E14\u0E15\u0E16\u0E17\u0E18\u0E19\u0E1A" \
                          r"\u0E1B\u0E1C\u0E1D\u0E1E\u0E1F\u0E20\u0E21\u0E22\u0E23\u0E24\u0E25\u0E26\u0E27\u0E28" \
                          r"\u0E29\u0E2A\u0E2B\u0E2C\u0E2D\u0E2E\u0E2F\u0E30\u0E31\u0E32\u0E33\u0E34\u0E35\u0E36" \
                          r"\u0E37\u0E38\u0E39\u0E3A\u0E3F\u0E40\u0E41\u0E42\u0E43\u0E44\u0E45\u0E46\u0E47\u0E48" \
                          r"\u0E49\u0E4A\u0E4B\u0E4C\u0E4D\u0E4E\u0E4F\u0E50\u0E51\u0E52\u0E53\u0E54\u0E55\u0E56" \
                          r"\u0E57\u0E58\u0E59\u0E5A\u0E5B\-']"
    elif language == "prs":
        INVALID_LETTERS = r"[^یہونملگكقفغعظطضصشسژزرذدخحچجثتپباآ\-']"
    elif language == "mn":
        INVALID_LETTERS = r"[^АаБбВвГгДдЕеЁёЖжЗзИиЙйКкЛлМмНнОоӨөПпРрСсТтУуҮүФфХхЦцЧчШшЩщЪъЫыЬьЭэЮюЯя\-']"
    elif language == "wen":
        INVALID_LETTERS = r"[^AaBbCcČčĆćDdEeĚěFfGgHhIiJjKkŁłLlMmNnŃńOoÓóPpRrŘřŔŕSsŠšŚśTtUuWwYyZzŽžŹźChchDźdź\-']"
    elif language == "smi":
        INVALID_LETTERS = r"[^AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZzÁáÅåâÄäÆæČčƷʒǮǯĐđǦǧǤǥÏïǨǩŊŋÕõÖöØøŠšŦŧÜüŽž\-']"
    elif language == "rom":
        INVALID_LETTERS = r"[^AaBbCcĆćČčČhčhĆhćhÇçDdDždžEeËëFfGgHhIiJjKkKhkhLlMmNnOoΘθPpPhphQqRrRrrrSsŚśŠšTtThthUuVvXxZzŽžŹźƷვ\-']"
    elif language == "af":
        INVALID_LETTERS = r"[^AaBbCcDdEeËëÊêFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuÛûVvWwXxYyZz\-']"
    elif language == "nah":
        INVALID_LETTERS = r"[^AaChchEeIiHhKkKwKwLlMmNnOoPpSsTtTltlTstsUuXxYyĀāĒēĪīŌō\-']"
    elif language == "csb":
        INVALID_LETTERS = r"[^AaĄąÃãBbCcDdEeÉéËëFfGgHhIiJjKkLlŁłMmNnŃńOoÒòÓóÔôPpRrSsTtUuÙùWwYyZzŻż\-']"
    elif language == "so":
        INVALID_LETTERS = r"[^'BbTtJjXxKHkhDdRrSsSHshDHdhCcGgFfQqKkLlMmNnWwHhYyAaEeIiOoUu\-']"
    elif language == "kl":
        INVALID_LETTERS = r"[^AaEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvBbCcDdXxYyZzWwÆæØøÅå\-']"
    elif language == "arn":
        INVALID_LETTERS = r"[^AaCHchDdEeFfGgIiKkLlḺḻLLllMmNnṈṉÑñNGngOoPpRrSsTtṮṯTRtrUuÜüWwYyazümchefiktnhtxoyqglhñrsllpuwlnshT't'\-']"
    elif language == "br":
        INVALID_LETTERS = r"[^AaBbCHchC'Hc'hDdEeFfGgHhIiJjJkLlMmNnOoPpRrSsTtUuVvWwYyZzâÊêÎîÔôÛûÙùÜüÑñ\-']"
    elif language == "ceb":
        INVALID_LETTERS = r"[^AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZzÑñNGng\-']"
    elif language == "ku":
        INVALID_LETTERS = r"[^ABCÇDEÊFGHIÎJKLŁMNŇOPQRŘSŞTUÛÜVWXYZabcçdeêfghiîjklłmnňopqrřsştuûüvwxyz\-']"
    elif language == "yi":
        INVALID_LETTERS = r"[^אאַאָבבּבֿגדדזשהווּוֹװויזזשחטטשייִייײַכּכךלמםנןסעפּפֿפףצץקרששׂתּת\-']"
    elif language == "sc":
        INVALID_LETTERS = r"[^AaBbCcÇçDdEeFfGgHhIiJjKkLlMmNnOoPpRrSsTtTztzUuVvXxYyZz\-']"
    elif language == "mr":
        INVALID_LETTERS = r"[^AaĀāBbBhbhCcChchDdDhdhḌḍḌhḍhEeFfGgGhghHhḤḥIiĪīJjJhjhKkKhkhLlMmNnṆṇṄṅOoPpPhphRrṚṛSsṢṣŠšTtThthṬṭṬhṭhUuŪūVvYy\-']"
    elif language == "bho":
        INVALID_LETTERS = r"[^ऀँंःऄअआइईउऊऋऌऍऎएऐऑऒओऔकखगघङचछजझञटठडढणतथदधनऩपफबभमयरऱलळऴवशषसहऺऻ़ऽािीुूृॄॅॆेैॉॊोौ्ॎॏॐ॒॑॓॔ॕॖॗक़ख़ग़ज़ड़ढ़फ़य़ॠॡॢॣ।॥०१२३४५६७८९॰ॱॲॳॴॵॶॷॸॹॺॻॼॽॾॿ\-']"
    elif language == "ro":
        INVALID_LETTERS = r"[^AaĂăâBbCcDdEeFfGgHhIiÎîJjKkLlMmNnOoPpQqRrSsȘșTtȚțUuVvWwXxYyZz\-']"
    elif language == "qu":
        INVALID_LETTERS = r"[^AaChchHhIiKkLlLlllMmNnÑñPpQqSsTtUuWwYyChhchhCh'ch'KhkhK'k'PhphP'p'QhqhQ'q'ShshSh'shThthT't'EeOoTr'tr'TstsZzBbDdØØFfGgKwkwRrRrrrTrtrVvČčĈĉŠšŽžꞫɜÁáÀà\-']"
    elif language == "bar":
        INVALID_LETTERS = r"[^AaÀàâÅåÃãĂăÄäBbCcDdEeÈèÉéÊêẼẽĔĕFfGgHhIiÎîJjKkLlMmNnOoÒòÓóÔôŎŏÖöPpQqRrSsTtUuÛûÜüVvWwXxYyZz\-']"

    elif language == "ak":
        INVALID_LETTERS = r"[^AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZzƐɛↃↄ\-']"
    elif language == "ktu":
        INVALID_LETTERS = r"[^AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz\-']"
    elif language == "mad":
        INVALID_LETTERS = r"[^AaBbCcDdÈèEeÉéFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZzṬṭḌḍÑñ\-']"
    elif language == "lg":
        INVALID_LETTERS = r"[^AaBbCcDdEeFfGgHhIiJjKkLlMmNnŊŋOoPpQqRrSsTtUuVvWwXxYyZz\-']"
    elif language == "hil":
        INVALID_LETTERS = r"[^AaBbKkDdEeGgHhIiLlMmNnNGngOoPpRrSsTtUuWwYy'\-']"
    elif language == "ny":
        INVALID_LETTERS = r"[^AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpRrSsTtUuVvWwŴŵZz’\-']"
    elif language == "ilo":
        INVALID_LETTERS = r"[^AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz\-']"
    elif language == "ht":
        INVALID_LETTERS = r"[^BbChchDdFfGgHhJjKkLlMmNnNgngPpRrSsTtVvZzDjdjWwYyUiuiAaEeÈèIiOoÒòOuouAnanEnenOnon\-']"
    elif language == "sn":
        INVALID_LETTERS = r"[^AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpRrSsTtUuVvWwYyZz\-']"
    elif language == "bar":
        INVALID_LETTERS = r"[^AaÀàâÅåÃãĂăÄäBbCcDdEeÈèÉéÊêẼẽĔĕFfGgHhIiÎîJjKkLlMmNnOoÒòÓóÔôŎŏÖöPpQqRrSsTtUuÛûÜüVvWwXxYyZz\-']"
    elif language == "nap":
        INVALID_LETTERS = r"[^AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvZz âÀàÁáÉéÊêÈèÍíÌìÎîÚúÛûÙùÓóÒòÔô\-']"
    elif language == "gn":
        INVALID_LETTERS = r"[^AaÃãEeẼẽGgG̃g̃HhIiĨĩJjKkLlMmNnÑñOoÕõPpRrSsTtUuŨũVvYyỸỹ\-']"
    elif language == "kg":
        INVALID_LETTERS = r"[^AaBbDdEeFfIiKkLlMmNnOoPpSsTtUuVvWwYyZz\-']"
    elif language == "ki":
        INVALID_LETTERS = r"[^AaBbCcDdEeGgHhIiĨĩJjKkMmNnOoRrTtUuŨũWwYy\-']"
    elif language == "min":
        INVALID_LETTERS = r"[^AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz\-']"

    elif language == "st":
        INVALID_LETTERS = r"[^AaBbDdEeFfHhIiJjKkLlMmNnOoPpQqRrSsTtUuWwYy’\-']"
    elif language == "ee":
        INVALID_LETTERS = r"[^AaBbDdƉɖEeƐɛFfƑƒGgƔɣHhIiKkLlMmNnŊŋOoƆɔPpRrSsTtUuVvƲʋWwXxYyZzÃãẼẽĨĩÕõŨũ\-']"
    elif language == "sg":
        INVALID_LETTERS = r"[^AaBbDdEeFfGgHhIiKkLlMmNnOoPpRrSsTtUuVvWwYyZzÊêËëûÛÜüîÎÏïôÔöÖäÄâ \-']"
    elif language == "scn":
        INVALID_LETTERS = r"[^AaBbCcDdEeFfGgHhIiJjLlMmNnOoPpQqRrSsTtUuVvZzÀàâÈèËëÊêÙùÛûÚúÌìÎîÏïÍíôÔòÒçÇ\-']"
    elif language == "luo":
        INVALID_LETTERS = r"[^AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpRrSsTtUuVvWwYyZz\-']"
    elif language == "nso":
        INVALID_LETTERS = r"[^AaBbDdEeFfHhIiJjKkLlMmNnOoPpQqRrSsTtUuWwYyÊêŠšôÔ\-']"
    elif language == "tn":
        INVALID_LETTERS = r"[^AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtVvWwXxYyZzÊêôÔŠš\-']"
    elif language == "bjn":
        INVALID_LETTERS = r"[^AaBbCcDdGhHhIiJjKkLlMmNnOoPpRrSsTtUuWwYyÉé\-']"
    elif language == "ace":
        INVALID_LETTERS = r"[^AaBbCcDdEeÉéÈèËëFfGgHhIiJjKkLlMmNnOoôÔöÖPpQqRrSsTtVvUuWwXxYyZz\-']"
    elif language == "lmo":
        INVALID_LETTERS = r"[^AaBbCcDdEeFfGgHhIiJjLlMmNnOoPpQqRrSsTtUuVvZzôÔòÒÓó\-']"
    elif language == "uz-Latn":
        INVALID_LETTERS = r"[^qwertyuioopasdfgghjklzxcvbnmQWERTYUIOOPASDFGGHJKLZXCVBNM\-']"
    elif language == "sr-Latn":
        INVALID_LETTERS = r"[^qwertzuiopšđasdfghjklčćyxcvbnmžQWERTZUIOPŠĐASDFGHJKLČĆYXCVBNMŽ\-']"
    return INVALID_LETTERS

words_freq = dict()
for i in ['mlt_newscrawl_2012_100K-words.txt', 'mlt_web_2012_300K-words.txt','mlt_wikipedia_2014_30K-words.txt','mlt_wikipedia_2016_30K-words.txt']:
    in_file_path = '/Users/xinmei/Downloads/其他语种/mt马耳他语/unigram/' + i
    in_file = open(in_file_path, 'r', encoding='utf-8')

    for line in in_file:
        words = line.strip().split('\t')[1]
        freq = int(line.strip().split('\t')[-1])
        for word in words.split(' '):
            if word in words_freq:
                words_freq[word] += freq
            else:
                words_freq[word] = freq

for i in sorted(words_freq.items(), key=lambda x: x[1], reverse=True):
    word = i[0]
    freq = str(i[1])
    all_latin = True
    for j in word:
        if not any(re.match(getlanguage(language), j)) or not str(j).isalpha():
            all_latin = False
            # print(word)
            break
    if all_latin:
        out_file.write(word + '\t' + freq + '\n')

