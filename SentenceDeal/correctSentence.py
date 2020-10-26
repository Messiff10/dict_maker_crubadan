import itertools
import random
import re
"""
生成纠错语料
"""
from utils.reExpression import replace_quotes_1, replace_brackets_1, replace_brackets_2 \
    , replace_brackets_3, replace_brackets_4, replace_brackets_5, replace_brackets_6, replace_brackets_7 \
    , replace_brackets_8, replace_brackets_9, replace_clock_time, replace_brackets_1, replace_quotes_2, \
    replace_quotes_3, replace_brackets_10, replace_brackets_11, replace_quotes_4, replace_line_time

regex_pun = re.compile(
    '[\±+_·&‰%¢$£¥₱€#@†*‡★؟\‚\:;/,….~`|♪•♣♠♥♦√πΠ÷×§¶∆≠=≈∞°↑^←‚\:;?/,….~`|♪•♣♠♥♦√πΠ÷×§¶←↓→\\©®™℅,ـًٌٍَُِّْٰٖٕٓٔ¹½⅓¼⅛²⅔³¾⅜⅝⁴⅞@#¢₱€£¥%٪‰&_·+±\\﴾*★٭\‚‹:;؛∆≠=≈!∞°،↑)}\]’’>›»’↓→\±+_\·&‰٪%¢£¥₱€#@†*‡★\©®™℅]')  # ar

data_path = "/Users/ff/Desktop/测评数据/纠错/"
sentence_path = data_path + "hi_HINGLISH_twitter.txt"
word_map_path = data_path + "word_map_sort"
emoji_path = data_path + "all_emojis"
pun = ["/", "(", ")", "@", "#", ">", "<"]
emojiset = set()
regex = re.compile('\s+')
result = set()
result_lower = set()
# WORD_REGEX = re.compile(r'')
sequence_new = {}


def getregex(language, WORD_REGEX):
    if language == "en_US":
        WORD_REGEX = re.compile(
            r"[^1234567890qweēêëèértyuūüùûúiìïīîíoõōøœòöôópaæãåā@as as#ad$f%g&h-j+k(l)z*x\"c'çv:b;n!m?, .-:'@#!"
            r",?QWEĒÊËÈÉRTYUŪÜÙÛÚIÌÏĪÎÍOÕŌØŒÒÖÔÓPAÆÃÅĀ@ÀÁ ÄS#SSD$F%G&H\-J+K(L)Z*X\"C'ÇV:B;N!ÑM?¹½⅓¼⅛²⅔⅜³¾⁴⅝⅞ⁿ∅@#"
            r"€¢£¥₱$%‰&-—_–·+±(<{[\]}>)/★†‡*„“”«»\"'‚‘’‹›:;¡!¿?_, ….~`|♣♠♪♥♦•√πΠ÷×§¶∆£€¥¢←↑↓→^′″°∞≠≈={},\©®™℅[\]‹≤«<>»≥› …']")
    elif language == "it":
        WORD_REGEX = re.compile(r"[^qwertyuiìíopèéùúasdfghjklòóàzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM']" + regex_pun)
    elif language == "fi":
        WORD_REGEX = re.compile(r"[^abcdefghijklmnopqrstuvwxyzåäöABCDEFGHIJKLMNOPQRSTUVWXYZAÅÄOÖ']" + regex_pun)
    elif language == "tr":
        WORD_REGEX = re.compile(r"[^ertyuıopğüasdfghjklşizcvbnmöçERTYUIOPĞÜASDFGHJKLŞİZCVBNMÖÇ']" + regex_pun)
    elif language == "ru":
        WORD_REGEX = re.compile(r"[^йцукенгшщзхфывапролджэячсмитьбюЙЦУКЕНГШЩЗХФЫВАПРОЛДЖЭЯЧСМИТЬБЮ']" + regex_pun)
    elif language == "es":
        WORD_REGEX = re.compile(r"[^qwertyuiopasdfghjklñzxcvbnmQWERTYUIOPASDFGHJKLÑZXCVBNM']" + regex_pun)
    elif language == "es_US":
        WORD_REGEX = re.compile(r"[^qwertyuiopasdfghjklñzxcvbnmQWERTYUIOPASDFGHJKLÑZXCVBNM']" + regex_pun)
    elif language == "ms_MY":
        WORD_REGEX = re.compile(r"[^qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM']" + regex_pun)
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
        WORD_REGEX = re.compile(
            r"[^éèêëcçàâæazertyÿuiîïoôœpqsdfghjklmùûüwxcvbnAÀÆZEÉÈÊËCÇRTYŸUÛÜIÎÏOÔŒPQSDFGHJKLMWXCVBN']")
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
        WORD_REGEX = re.compile(
            r"[^१1⅓¼⅛¹½2²⅔२३¾3³⅜४4⁴५5⅝६67⅞७8८9९0∅ⁿ@#€¢£¥₱$%‰&—_–·\-+±(<{[\]}>)/★†‡*„“”«»\"\'‚‘’‹›:;¡!¿?_, ….~`|♪♣♠♥♦•√πΠ÷×§¶∆£€¥"
            r"¢←↑↓→^′″°∞≠≈={},\©®™℅[\]‹≤«<>›≥» ….\u0948\u0947\u0942\u0941\u094b\u094c\u093f\u0940\u0902\u093c\u0948\u0947\u0942"
            r"\u0941\u094b\u094c\u093f\u0940\u0902\u093c\u0948\u0967\u0973\u0976\u0977\u0967\u0947\u0968\u0974\u0911\u0972\u0968"
            r"\u0942\u0969\u0969\u0941\u096a\u0941\u096a\u094b\u096b\u096b\u094c\u096c\u096c\u093f\u096d\u090d\u096d\u0940\u096e"
            r"\u090e\u096e\u0902\u096f\u0904\u0912\u096f\u093c\u0966\u0975\u0966\u0905\u0967\u0948\u0973\u0976\u0977\u0967\u0906"
            r"\u0968\u0947\u0974\u0911\u0972\u0968\u0907\u0969\u0942\u0969\u0908\u096a\u0941\u096a\u0909\u096b\u094c\u096b\u090a"
            r"\u096c\u094b\u096c\u090f\u096d\u093f\u090d\u096d\u0910\u096e\u0940\u090e\u096e\u0913\u096f\u0902\u0904\u0912\u096f\u0914"
            r"\u0966\u093c\u0975\u0966\u090b\u0919\u093e\u0a3e\u094e\u0962\u0963\u0915\u094d\u0937\u0949\u0943\u0933\u0934\u0955\u0945"
            r"\u094d\u093b\u090b\u0919\u093e\u0a3e\u094e\u0962\u0963\u0915\u094d\u0937\u0949\u0943\u0933\u0934\u0955\u0945\u094d\u093b"
            r"\u0915\u0915\u094d\u0930\u0915\u094d\u092f\u0915\u094d\u0938\u0915\u094d\u0932\u0958\u0930\u094d\u0915\u0916\u0916\u093c"
            r"\u0916\u094d\u092f\u0916\u094d\u092e\u0930\u094d\u0916\u0917\u0917\u094d\u0930\u0917\u094d\u092f\u0917\u094d\u092e\u0917"
            r"\u094d\u0924\u0930\u094d\u0917\u0917\u0952\u095a\u0918\u0918\u094d\u0930\u0918\u094d\u092f\u0930\u094d\u0918\u091a\u091a"
            r"\u094d\u0930\u091a\u094d\u091a\u091a\u094d\u092f\u091a\u094d\u091b\u0930\u094d\u091a\u091b\u091b\u094d\u0930\u0930\u094d"
            r"\u091b\u091b\u0903\u091c\u091c\u094d\u0930\u0930\u094d\u091c\u091c\u093c\u091c\u0902\u091c\u094d\u092f\u091c\u0952\u0979"
            r"\u091c\u094d\u0930\u095b\u091d\u091d\u094d\u092e\u091d\u094d\u0930\u0936\u0936\u094d\u0935\u0936\u094d\u0930\u0936\u094d"
            r"\u091a\u0930\u094d\u0936\u0939\u0939\u094d\u0923\u0939\u094d\u0932\u0939\u094d\u0935\u0939\u094d\u092e\u0930\u094d\u0939"
            r"\u0939\u094d\u092f\u0938\u0938\u094d\u0928\u0938\u094d\u0925\u0938\u094d\u091f\u0938\u094d\u091c\u0938\u094d\u0915\u0938"
            r"\u094d\u0924\u0938\u094d\u0935\u0938\u094d\u0930\u0930\u094d\u0938\u0943\u0944\u0900\u094a\u097d\u094f\u0971\u093d\u25cc"
            r"\u093a\u0954\u0970\u0953\u0957\u0952\u0956\u0903\u0946\u0943\u0944\u0900\u094a\u097d\u094f\u0971\u093d\u25cc\u093a\u0954"
            r"\u0970\u0953\u0957\u0952\u0956\u0903\u0946\u091f\u091f\u094d\u091f\u0930\u094d\u091f\u091f\u094d\u0920\u091f\u094d\u0930"
            r"\u091f\u0902\u0920\u0930\u094d\u0920\u0920\u094d\u0930\u0920\u0902\u0921\u0921\u0902\u0921\u093c\u0930\u094d\u0921\u095c"
            r"\u0921\u0952\u0922\u0922\u0902\u0922\u093c\u0930\u094d\u0922\u095d\u0923\u0923\u094d\u0930\u0923\u094d\u0921\u0923\u094d"
            r"\u091f\u0930\u094d\u0923\u0924\u0924\u094d\u0924\u0924\u094d\u0930\u0930\u094d\u0924\u0924\u094d\u092e\u0924\u094d\u0928"
            r"\u0924\u094d\u0925\u0925\u0924\u094d\u0925\u0925\u094d\u0930\u0930\u094d\u0925\u0926\u0926\u094d\u0930\u0926\u094d\u0935"
            r"\u0926\u094d\u0927\u0926\u094d\u0926\u0927\u0927\u094d\u0930\u0930\u094d\u0927\u0927\u094d\u0925\u0928\u0928\u094d\u0928"
            r"\u0930\u094d\u0928\u0928\u094d\u092e\u0928\u094d\u0924\u0928\u094d\u092f\u0928\u093c\u0937\u0937\u0937\u094d\u091f\u0937"
            r"\u094d\u0920\u0937\u094d\u005f\u0936\u094d\u0930\u0960\u0901\u0924\u094d\u0930\u091e\u0950\u091c\u094d\u091e\u093a\u050f"
            r"\u0936\u094d\u0930\u0960\u0901\u0924\u094d\u0930\u091e\u0950\u091c\u094d\u091e\u093a\u092a\u092a\u094d\u092a\u0928\u094d"
            r"\u092a\u092a\u094d\u092f\u092a\u094d\u0930\u0930\u094d\u092a\u092b\u092b\u093c\u092b\u0902\u0930\u094d\u092b\u092b\u094d"
            r"\u0930\u092c\u092c\u094d\u092c\u092c\u094d\u0930\u0930\u094d\u092c\u092c\u0952\u092d\u092d\u094d\u0930\u092d\u094d\u092e"
            r"\u0930\u094d\u092d\u092e\u0930\u094d\u092e\u092e\u094d\u0930\u092e\u0948\u0902\u092e\u094d\u092e\u092e\u094d\u0928\u092e"
            r"\u094d\u092c\u092e\u094d\u0939\u092e\u0947\u0902\u092f\u092f\u094d\u0930\u0930\u094d\u092f\u092f\u093c\u097a\u0930\u0931"
            r"\u0930\u0902\u0930\u094d\u0930\u0931\u0930\u094d\u0932\u0932\u094d\u0926\u0932\u094d\u092e\u0932\u094d\u0930\u0930\u094d"
            r"\u0932\u090c\u0961\u0935\u0935\u094d\u092f\u0935\u094d\u0930\u0930\u094d\u0935]")
    elif language == "ro":
        WORD_REGEX = re.compile(
            r"[^qwertțyuīíįìïîopâãăàáäæåāaśșßšsdfghjklzxcvbnmQWERTȚYUIĪÍĮÌÏÎOPÄÆÅĀÃĂÀÁASŚȘSSŠDFGHJKLZXCVBNM']")
    elif language == "hu":
        WORD_REGEX = re.compile(r"[^AaÁáBbCcDdEeÉéFfGgHhIiÍíJjKkLlMmNnOoÓóÖöŐPpQqRrSsTtUuÚúÜüŰűVvWwXxYyZz']")
    elif language == "uk":
        WORD_REGEX = re.compile(r"[^АаБбВвГгҐґДдЕеЄєЖжЗзИиІіЇїЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЬьЮюЯя']")
    elif language == "bg":
        WORD_REGEX = re.compile(
            r"[^у1е2и3ѝш4щ5к6с7д8з9ц0бьяаожгтнвмчюйъэфхпрл, .-:\'@#!,?УЕИЍШЩКСДЗЦБЬЯАОЖГТНВМЧЮЙЪЭФХПРЛ¹½⅓¼⅛1²⅔2³⅜¾34⁴5⅝67⅞89ⁿ∅@#¢€£¥₱$%‰&_"
            r"—–·\-+±(<{[)\]>/†★‡*”„'“«»\"\‚‘’‹›:¡!¿?_, ….~`|♪♣♠♥♦√πΠ÷×§¶∆£€¥¢←↑↓→^°′″=∞≠≈{},\©®™℅\[\]≤‹«<>›≥» ….']")
    elif language == "sl":
        WORD_REGEX = re.compile(
            r"[^1234567890qwertyuiopašsđdfghjklžzxčćcvbnmQWERTYUIOPAŠSĐDFGHJKLŽZXČĆCVBNM, -:'@#!,?. ¹½⅓¼⅛²⅔⅜³¾⁴⅝⅞ⁿ∅@#$¢£¥₱€‰%&—_–·\-±+<{[()\]}>/★†‡*”„“»«\"'’‚‘"
            r"›‹\':;¡!¿?_, ….~`|♣♠♪♥♦•√πΠ÷×§¶∆£¥$¢←↑↓→^′″°∞≠≈={},\©®™℅[\]‹≤«<>»≥› ….']")
    elif language == "et_EE":
        WORD_REGEX = re.compile(
            r"[^1234567890qwêëęěèēėéeřŗŕrtťţyÿýůúûűùūüųuïíîıìīįiøőôœóòõöopüãåæąäāàáâašßśşsďdfģğghjķkľĺļłlõöäźžżzxćččcvbńņñńnmQWÊËĘĚÈĒĖÉERŘŖŔŤŢTŸÝYUŮÚÛŰÙŪÜŲUÏÍÎIÌ"
            r"ĪĮIØŐÔŒÓÒÕÖOPÜÃÅÆĄÄĀÀÁ ASŠSSŚŞSĎDFĢĞGHJĶKĻĽĹŁLÕÖÄŹŽŻZXĆČÇCVBŃŅÑŃNM, -:'@#!,?¹½⅓¼⅛²⅔⅜³¾⁴⅝⅞ⁿ∅@#$¢£¥₱€‰%&—_–·\-±+<{[()\]}>/★†‡*\"”„“«»'’‚‘‹›:;¡!¿?_, …."
            r"~`|♣♠♪♥♦•√πΠ÷×§¶∆£¥$¢←↑↓→^′″°=∞≠≈{},\©®™℅[\]‹≤«<>»≥› …']")
    elif language == "af":
        WORD_REGEX = re.compile(
            r"[^1234567890qwėëęēèéêertĳýyuūüùûúiĳīîįïìíioóôöòõœøōpaáâäàæãåāsdfghjklzxcvbnñńmQWEĖËĘĒÈÉÊRTYĲÝUŪÜÙÛÚIĲĪÎĮÏÌÍOÕŒØŌÓÔÖÒPAÁ ÄÀÆÃÅĀSDFGHJKLZXCVBÑŃNM, .#"
            r"!,?@':\-¹½⅓¼⅛²⅔⅜³¾⁴⅝⅞ⁿ∅@#€¢£¥₱$‰%&—_–·\-+±(<{[\]}>)/★†‡*\"„“”«»'‚‘’‹›':;¡!¿?_, ….~`|♣♠♪♥♦•√πΠ÷×§¶∆£€¥¢←↑↓→^′″°∞≠≈={},\©®™℅[\]‹≤«<>≥»› ….']")
    elif language == "hr":
        WORD_REGEX = re.compile(
            r"[^q1w2e3r4t5z6źžżu7i8o9p0asßšśdđfghjklyxcčçćvbnñńm, .-:\'@#!,?QWERTZŹŽŻUIOPASSSŠŚDĐFGHJKLYXCČÇĆVBNÑŃM¹½⅓¼⅛²⅔⅜³¾⁴⅝⅞ⁿ∅@#€¢£¥₱‰%$&_—–·\-±+<{[\]}>\)(/★†‡*“„”»«\"\'‘‚’›‹:;¡!¿"
            r"?_,….~`|♪♣♠♥♦•√πΠ÷×§¶∆£€¥¢←↑↓→^′″°≠≈∞={},\©®™℅[\]≤‹«<>›≥» .…']")
    elif language == "sr":
        WORD_REGEX = re.compile(
            r"[^љ1њ2е3ѐр4т5з6у7и8ѝо9п0шасдфгхјклчћѕџцвбнмђж,. -:\'@#!,?ЀЍ¹½⅓¼⅛12²⅔3⅜³¾4⁴5⅝6⅞ⁿ∅ЉЊЕРТЗУИОПШАСДФГХЈКЛЧЋЅЏЦВБНМЂЖ@#$€¢£¥₱%‰&-—_–·+±(<{[)\]}>/*★†‡\"”„““»«\'’‚‘›‹:;!¡?¿_,.~`|"
            r"•♣♠♪♥♦√Ππ÷×¶§∆£€¥¢^←↑↓→°′″=∞≠≈{},\©®™℅[\]‹≤«<>›≥»…']")
    elif language == "lt":
        WORD_REGEX = re.compile(
            r"[^q1w2e3éêëěęėēèrř4ŗŕtť5ţyÿ6ýuűûùúůūų7ūüiıïíîìī8įoøőœôóòõö90pâãåæąäāàáasśšßşdďfgģğhjkķlľĺłļzźžżxčcćçvbnńņñńm, .\-:\'@#!,?QWEÉÊËĚĘĖĒÈRŘŖŔTŤŢYŸÝUŰÛÙÚŮŪŲŪÜIIÏÍÎÌĪĮOØŐŒÔÓÒÕÖP"
            r"A ÃÅÆĄÄĀÀÁŚŠSSŞSDĎFGĢĞHJKĶLĽĹŁĻZŹŽŻXCĆČÇVBNŃŅÑŃM, .\-:\'@#!,?¹½⅓¼⅛²⅔³⅜¾⁴⅝⅞ⁿ∅@#€¢£¥₱$%‰&\-—_–·+±({<[)>}\]/*†★‡”„“«»\"\'’‚‘‹›:;¡!¿?_, .,…~`|♣♠♪♥♦√πΠ÷×§¶∆£€¥¢←↑↓→^′″°≠∞≈={}"
            r",\©®™℅[\]‹≤«<>›≥» .…']")
    elif language == "lv":
        WORD_REGEX = re.compile(
            r"[^q1w2e3êëęěėēèérř4ŗŕtť5ţyÿ6ýuůûüűúų7ūùiıïíîìį8īoøőœöõôóò9p0aäåæąāàáâãsśšßşdďfgģğhjķkļłĺľlzźžżxčćçcvbnńņñńm, .-:\'@#!,?QWEÊËĘĚĖĒÈÉRŘŖŔTŤŢYŸÝUŮÛÜŰÚŲŪÙIIÏÍÎÌĮĪOØŐŒÖÕÔÓÒPAÄÅÆ"
            r"ĄĀÀÁ ÃASŚŠSSŞDĎFGĢĞHJKĶLĽĹŁĻZŹŽŻXCĆČÇVBNŃŅÑŃM, -:\'@#!,?¹½⅓¼⅛²⅔⅜³¾⁴⅝⅞ⁿ∅@#€¢£¥₱$%‰&\-—_–·+±(<{[)>}\]/★†‡*\"”„“«»\"\'’‚‘‹›:¡!¿?_ ….~`|♣♠♪♥♦√πΠ÷×§¶∆£€¥¢←↑↓→^°′″=∞≠≈{},\©®™℅[\]‹≤«<>›≥» .…']")
    elif language == "el":
        WORD_REGEX = re.compile(
            r"[^;1:ς2ε3έρ4τ5υϋ6ύύθ7ιΐϊ8ίοό9π0αάσδφγηήξκλζχψωώβνμ, .…¹½⅓¼⅛12²⅔3⅜³¾4⁴5⅝6⅞ⁿ∅;ςΕΡΤΥΘΙΟΠΑΣΔΦΓΗΞΚΛΖΧΨΩΒΝΜ1:;ςΕΈΡΤΥΫΎΫ́ΘΙΪ́ΪΊΟΌΠΑΆΣΔΦΓΗΉΞΚΛΖΧΨΩΏΒΝΜ@#$¢£¥₱€‰%&—_–·\-±+<{[)>\]}/*★†‡„“”«»‚‘’‹›:;¡!\"\'¿?_~`|♣♠♪♥♦•√πΠ÷×§¶∆£¥$¢←↑↓→^′″°∞≠≈={},\©®™℅\[\]‹≤«›≥»<>.']")
    elif language == "sk":
        WORD_REGEX = re.compile(
            r"[^q1w2eèêëęěéēė3r4řŕŗtţ5ťyÿ6ýuûųùűūů7úüiıïìîįī8íoøőœõòöóô90paáåæąáäāàâsśšßşdďfgģğhjķkľĺļłlźžżzxćčçcvbńñňņńm, .QWÈÊËĘĚÉĒĖEŘŔŖRŢŤTŸÝYÛŲÙŰŪŮÚÜUIÏÌÎĮĪÍIØŐŒÕÒÖÓÔ9OPÃÅÆĄÁÄĀÀ AŚŠSSŞSĎDFĢĞGHJĶKŁĻĹĽLŹŽŻZXĆČÇCVBÑÑŇŅŃNM@#$¢£¥₱€‰%&—_–·\-±+<{[(\]}>\)/★†‡*”„“»«\"\'’"
            r"‚‘›‹:;¡!¿?_,….~`|♣♠♪♥♦√πΠ÷×§¶∆£¥$¢←↑↓→^′″°∞≠≈={},\©®™℅[\]‹≤«›≥»<> .…¹½⅓¼⅛12²⅔3⅜³¾4⁴5⅝6⅞ⁿ∅']")
    elif language == "et_EE":
        WORD_REGEX = re.compile(
            r"[^q1w2e3êëęěėēèérř4ŗŕtť5ţyÿ6ýuůûüűúų7ūùiıïíîìį8īoøőœöõôóò9p0aäåæąāàáâãsśšßşdďfgģğhjķkļłĺľlzźžżxčćçcvbnńņñńm, .\-:\'@#!,?QWEÊËĘĚĖĒÈÉRŘŖŔTŤŢYŸÝUŮÛÜŰÚŲŪÙIIÏÍÎÌĮĪOØŐŒÖÕÔÓÒPAÄÅÆĄĀÀÁ ÃASŚŠSSŞDĎFGĢĞHJKĶLĽĹŁĻZŹŽŻXCĆČÇVBNŃŅÑŃM, \-:\'@#!,?¹½⅓¼⅛²⅔⅜³¾⁴⅝⅞\ⁿ∅@#€¢£¥₱$"
            r"%‰&\-—_–·+±(<{[)>}\]/★†‡*\"”„“«»\"\'’‚‘‹›:¡!¿?_ ….~`|♣♠♪♥♦√πΠ÷×§¶∆£€¥¢←↑↓→\^°′″=∞≠≈{},\©®™℅\[\]‹≤«<>›≥» .…']")
    elif language == "nl":
        WORD_REGEX = re.compile(
            r"[^1234567890qwėèęēëéêertĳyuūûùüúiĳīîįìïíiōøœõòôöóopaæãåāáäâàasdfghjklzxcvbñńnmQWĖÈĘĒËÉÊERTYĲŪÛÙÜÚUĲĪÎĮÌÏÍIŌØŒÕÒÔÖÓOPÆÃÅĀÁÄ ÀASDFGHJKLZXCVBÑŃNM, -:'@#!,?¹½⅓¼⅛²⅔⅜³¾⁴⅝⅞ⁿ∅@#$¢£¥₱€‰%&—_–·\-+±<{[()\]}>/★†‡*\"“„”«»'‘‚’‹›':;¡!¿?_, ….~`|♣♠♪♥♦•√πΠ÷×§¶∆£¥$¢←↑↓→^°′"
            r"″=∞≠≈{},\©®™℅[\]‹≤«<>»≥› ….']")
    elif language == "kk":
        WORD_REGEX = re.compile(
            r"[^1234567890йцұүукқеёнңгғшщзхһфыівәапрөолджэячсмитъьбюЙЦҰҮУҚКЁЕҢНҒГШЩЗҺХФІЫВӘАПРӨОЛДЖЭЯЧСМИТЪЬБЮ,-:'@#!,?.¹½⅓¼⅛²⅔⅜³¾⁴⅝⅞ⁿ∅@#€¢£¥₱$‰%&—_–·\-±+<{[()\]}>/★†‡*\"„“”«»'‚‘’’›:;¡!¿?_, …~`|♣♠♪♥♦•√πΠ÷×§¶∆£€¥¢←↑↓→^°′″∞≠≈={},\©®™℅[\]‹≤«<>»≥› ….']")
    elif language == "uk":
        WORD_REGEX = re.compile(
            r"[^1234567890йцукенґгшщзхфїівапролджєячсмитъьбюЙЦУКЕНГ7ШЩЗХФЇІВАПРОЛДЖЄЯЧСМИТЪЬБЮ, -:'@#!,?.¹½⅓¼⅛²⅔⅜³¾⁴⅝⅞ⁿ∅@#€¢£¥₱$‰%&—_–·\-±+<{[()\]}>/★†‡*”„“«»\"\'’‚‘‹›\':;¡!¿?_, ….~`|♣♠♪♥♦•√πΠ÷×§¶∆£€¥¢$←↑↓→^′″°∞≠≈={},\©®™℅[\]‹≤«<>»≥› ….']")
    elif language == "hi_HINGLISH":
        WORD_REGEX = re.compile(
            r"[^1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM, .-:'@#!,?1¹½⅓¼⅛१2²⅔२3¾³⅜३4⁴४5⅝५6६7⅞७8८9९0ⁿ∅०@#€¢£¥₱$‰%&—_–·\-±+<{[()\]}>/★†‡*„“”«»\"'‚‘’’›:;¡!¿?_, ….~`|♣♠♪♥♦•√πΠ÷×§¶∆£€¥¢$←↑↓→^′″°=∞≠≈{},\©®™℅[\]‹≤«<>»≥› ….']")
    return WORD_REGEX


def del_sentence(WORD_REGEX):
    count = 0
    with open(emoji_path, 'r', encoding='utf-8') as f_emoji:
        for line in f_emoji:
            emojis = line.strip().split('\t')
            if emojis[0] not in emojiset:
                emojiset.add(emojis[0])
    with open(sentence_path, 'r', encoding='utf-8') as add_file:
        for line in add_file:
            line = re.sub('\s+', ' ', line)
            centence = line
            # words = regex.split(line)
            for p in pun:
                if line.find(p) >= 0:
                    # print(line)
                    centence = ""
                    break
            for em in emojiset:
                if em in line:
                    centence = ""
                    break
            if centence is not "" and re.search(WORD_REGEX, line) is None:
                if centence.lower() not in result_lower:
                    count += 1
                    result_lower.add(centence.lower())
                    result.add(centence)
    print(count)


def random_pick_freq(word, sequence, freqs):
    if word not in sequence_new.keys():
        sequence_new[word] = []
        for x, y in zip(sequence, freqs):
            for z in [x] * int(y):
                sequence_new[word].append(z)
    while True:
        yield random.choice(sequence_new[word])


def getword_map():
    wordmap = {}
    with open(word_map_path, 'r', encoding='utf-8') as map_:
        current_word = ""
        current_map = {}
        for line in map_:
            items = line.split("\t")
            # print(items)
            desired_word = items[0].strip()
            keys = items[1].strip()
            freq = items[2].strip()

            if keys == "" or len(desired_word) != len(keys) :  # 纠错为空或相同则掠过
                continue
            if desired_word.lower() == keys.lower():
                # freq=int(freq)*1000
                freq = int(int(freq) / 10)
                if freq == 0:
                    freq = 9000000
            if current_word == desired_word:
                current_map[keys] = freq
            else:
                if current_word != "":
                    wordmap[current_word] = current_map
                current_word = desired_word
                current_map = {}
                current_map[keys] = freq

        wordmap[current_word] = current_map
    map_.close()
    return wordmap


def del_space(lines):
    line = lines.strip()
    line = replace_brackets_1(line)
    line = replace_brackets_9(line)
    line = replace_brackets_8(line)
    line = replace_brackets_7(line)
    line = replace_brackets_6(line)
    line = replace_brackets_5(line)
    line = replace_brackets_4(line)
    line = replace_brackets_3(line)
    line = replace_brackets_2(line)
    line = replace_brackets_10(line)
    line = replace_brackets_11(line)
    line = replace_quotes_2(line)
    line = replace_quotes_3(line)
    line = replace_clock_time(line)
    line = replace_quotes_1(line)
    line = replace_quotes_4(line)
    words = re.findall(regex_pun, line)
    for w in words:
        line = re.sub('\s+', ' ', line)
        line = line.replace(' ' + w, w)
        line = re.sub('\s+-\s+', '-', line)
    return line


def getsentence(wordmap_all):
    with open(sentence_path.replace('.txt', '.tsv.fuzzed'), 'w', encoding='utf-8') as f_out:
        result_count = 0
        for line in result:
            words = regex.split(line)
            outputline = []
            for word in words:
                if word.lower() in wordmap_all.keys():
                    wordmap = random_pick_freq(word.lower(), wordmap_all[word.lower()].keys(),
                                               wordmap_all[word.lower()].values())
                    noise_word = ''.join(itertools.islice(wordmap, 1))
                    noise_word_result = ""
                    for w in range(0, len(word)):
                        if word[w].isupper():
                            noise_word_result += noise_word[w].upper()
                        else:
                            noise_word_result += noise_word[w]
                    outputline.append(noise_word_result)
                else:
                    outputline.append(word)
            resultline = " ".join(outputline)
            resultline = del_space(resultline)
            line = del_space(line)
            if len(resultline) == len(line) and result_count < 2000:
                result_count += 1
                # print(resultline,line,(resultline + " WR#CO " + line).strip())
                f_out.write((resultline + " WR#CO " + line).strip())
                f_out.write('\n')
        print("结果行数：" + str(result_count))


if __name__ == '__main__':
    language = "hi_HINGLISH"
    WORD_REGEX = ""
    WORD_REGEX = getregex(language, WORD_REGEX)
    del_sentence(WORD_REGEX)
    wordmap_all = getword_map()
    getsentence(wordmap_all)

    print("Finish line")
