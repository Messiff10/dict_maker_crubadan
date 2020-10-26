import os
import re
"""
网上词典处理
crubadan

"""
MAX_UNI_FREQ = 250
MIN_UNI_FREQ = 1
MAX_BI_FREQ = 15
MIN_BI_FREQ = 1

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
    elif language == "bs-Cyrl":
        INVALID_LETTERS = r"[^љњертзуиопшасдфгхјклчћџцвбнмђж£ЉЊЕРТЗУИОПШАСДФГХЈКЛЧЋЏЦВБНМЂЖ\-']"
    elif language == "fa-Latn":
        INVALID_LETTERS = r"[^AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZzâČčŽžŠš\-']"
    elif language == "kk-Latn":
        INVALID_LETTERS = r"[^AaÄäBbVvGgĞğDdEeJjZzIıIıKkQqLlMmNnŊŋOoÖöPpRrSsTtWwUuÜüFfHhÇçŞşYyİiIiÁáǴǵŃńÓóÝýÚúIýıý\-']"
    elif language == "fy":
        INVALID_LETTERS = r"[^AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZzéÉêÊÛûúÚôÔâ\-']"
    elif language == "sah":
        INVALID_LETTERS = r"[^АаБбВвГгҔҕДдДьдьЕеЁёЖжЗзИиЙйКкЛлМмНнҤҥНьньОоӨөПпРрСсҺһТтУуҮүФфХхЦцЧчШшЩщЪъЫыЬьЭэЮюЯя\-']"
    elif language == "sdc":
        INVALID_LETTERS = r"[^AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZzéèÉÈÀàÓóÌìòÒùÙ\-']"
    elif language == "ast":
        INVALID_LETTERS = r"[^AaBbCcDdEeFfGgHhIiLlMmNnÑñOoPpQqRrSsTtUuVvXxYyZz\-']"
    elif language == "bm":
        INVALID_LETTERS = r"[^AaBbCcDdEeƐɛFfGgHhIiJjKkLlMmNnƝɲŊŋOoƆɔPpRrSsTtUuWwYyZz\-']"
    elif language == "ms-Arab":
        INVALID_LETTERS = r"[^ضصث‎قغ‎فعهخحجدشسيبلاتنمکطئءؤرلاىةوزظڤڠچذإأآڽݢلإلألآۏژ\-']"
    elif language == "cy":
        INVALID_LETTERS = r"[^AaBbCcDdEeFfGgngHhIiLlMmNnOoPpRrSsTtUuWwYyâÊêÎîÔôÛûŴŵŶŷ\-']"
    elif language == "eo":
        INVALID_LETTERS = r"[^AaBbCcĈĉDdEeFfGgĜĝHhĤĥIiJjĴĵKkLlMmNnOoPpRrSsŜŝTtUuŬŭVvZz\-']"
    elif language == "fo":
        INVALID_LETTERS = r"[^AaÁáBbDdÐðEeFfGgHhIiÍíJjKkLlMmNnOoÓóPpRrSsTtUuÚúVvYyÝýÆæØø\-']"
    elif language == "gd":
        INVALID_LETTERS = r"[^AaÀàBbCcDdEeÈèFfGgHhIiÌìLlMmNnOoÒòPpRrSsTtUuÙù\-']"
    elif language == "ig":
        INVALID_LETTERS = r"[^ABCHDEFGGBGHGWHIỊJKKPKWLMNṄN̄NWNYOỌPRSSHTUỤVWYZabchdefggbghgwhiịjkkpkwlmnṅn̄nwnyoọprsshtuụvwyzN̄n̄\-']"
    elif language == "ku":
        INVALID_LETTERS = r"[^ABCÇDEÊFGHIÎJKLŁMNŇOPQRŘSŞTUÛÜVWXYZabcçdeêfghiîjklłmnňopqrřsştuûüvwxyzǦǧḤḥḦḧ\-']"
    elif language == "ku-Arab":
        INVALID_LETTERS = r"[^عش‎س‎ژ‎ز‎ڕ‎ر‎د‎خ‎حچ‎ج‎ت‎پ‎ب‎ا‎ئـ‎ێ‎ی‎وو‎ۆ‎و‎ە‎ھ‎ن‎م‎ڵ‎ل‎گ‎ک‎ق‎ڤ‎ف‎غ‎ۊڥڕؽۊعشغحهكڵڵڥں\-']"
    elif language == "nn":
        INVALID_LETTERS = r"[^AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZzÆæØøÅåÄäÀàÁáâÊêÈèéÉôÔÓóÖöÒòÜü\-']"
    elif language == "nds":
        INVALID_LETTERS = r"[^AaÄäBbCcCHchCKckDdDTdtEeFfGgHhIiJjKkLlMmNnNGngOoÖöPpQUquRrSsSCHschẞßTtTSCHtschUuÜüVvWwXxYyZz\-']"
    elif language == "ky":
        INVALID_LETTERS = r"[^АаБбВвГгДдЕеЁёЖжЗзИиЙйКкЛлМмНнҢңОоӨөПпРрСсТтУуҮүФфХхЦцЧчШшЩщЪъЫыЬьЭэЮюЯя\-']"
    elif language == "ce":
        INVALID_LETTERS = r"[^АаАьаьБбВвГгГIгIДдЕеЁёЖжЗзИиЙйКкКхкхКъкъКIкIЛлМмНнОоОьоьПпПIпIРрСсТтТIтIУуУьуьФфХхХьхьХIхIЦцЦIцIЧчЧIчIШшЩщЪъЬьЭэЮюЮьюьЯяЯьяьIĪ\-']"
    return INVALID_LETTERS


def get_freq_from_line_index(lines, index):
    print(lines)
    return int(lines[index].strip().split()[-1])


def scale(ori_min, ori_max, new_min, new_max, x):
    return int((new_max - new_min) * (x - ori_min) / (ori_max - ori_min) + new_min)


def build_unigram_dict(in_file_path, out_file_path, INVALID_LETTERS):
    with open(in_file_path, 'r', encoding='utf-8') as in_file:
        in_lines = in_file.readlines()

    in_lines = [l for l in in_lines if not any(re.match(INVALID_LETTERS, w) for w in l.strip().split()[:-1])]

    ori_max_freq = get_freq_from_line_index(in_lines, 5)
    ori_min_freq = get_freq_from_line_index(in_lines, -1)

    with open(out_file_path, 'w+', encoding='utf-8') as out_file:
        for line in in_lines:
            word, freq = line.strip().split()
            freq = int(freq)
            if len(word)<40:
                new_freq = scale(ori_min_freq, ori_max_freq, MIN_UNI_FREQ, MAX_UNI_FREQ, freq)
                new_freq = MAX_UNI_FREQ if new_freq > MAX_UNI_FREQ else new_freq
                out_file.write(f'{word}\t{new_freq}\n')


def build_bigram_dict(in_file_path, out_file_path, INVALID_LETTERS):
    with open(in_file_path, 'r', encoding='utf-8') as in_file:
        in_lines = in_file.readlines()

    in_lines = [l for l in in_lines if not any(re.match(INVALID_LETTERS, w) for w in l.strip().split()[:-1])]

    ori_max_freq = get_freq_from_line_index(in_lines, 5)
    ori_min_freq = get_freq_from_line_index(in_lines, -1)

    with open(out_file_path, 'w+', encoding='utf-8') as out_file:
        for line in in_lines:
            prev_word, next_word, freq = line.strip().split()
            freq = int(freq)
            if len(prev_word) < 40 and len(next_word)<40:
                new_freq = scale(ori_min_freq, ori_max_freq, MIN_BI_FREQ, MAX_BI_FREQ, freq)
                new_freq = MAX_UNI_FREQ if new_freq > MAX_UNI_FREQ else new_freq
                out_file.write(f'{prev_word}\t{next_word}\t{new_freq}\n')


if __name__ == '__main__':
    s = "nds"
    s_ = "nds"
    unigram_dict_file_input = "/Users/ff/Desktop/data/dict/netDict/" + s + "/" + s + "-words.txt"
    bigram_dict_file_input = "/Users/ff/Desktop/data/dict/netDict/" + s + "/" + s + "-wordbigrams.txt"
    if not os.path.exists("/Users/ff/Desktop/data/dict/input/" + s_):
        os.makedirs("/Users/ff/Desktop/data/dict/input/" + s_)
    unigram_dict_file_output = "/Users/ff/Desktop/data/dict/input/" + s_ + "/" + s_ + "_unigram.txt"
    bigram_dict_file_output = "/Users/ff/Desktop/data/dict/input/" + s_ + "/" + s_ + "_bigram.txt"
    INVALID_LETTERS = getlanguage(s)
    build_unigram_dict(unigram_dict_file_input, unigram_dict_file_output, INVALID_LETTERS)
    build_bigram_dict(bigram_dict_file_input, bigram_dict_file_output, INVALID_LETTERS)
    print("Finish line")
