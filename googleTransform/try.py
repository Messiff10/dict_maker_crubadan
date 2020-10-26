from googletrans import Translator
import emoji
import time
import re


def transform(language):
    translator = Translator()
    # regex = re.compile('\s+')
    # setence = []


    # with open('/data/python/data/web/transform/type.txt', 'r', encoding='utf-8') as en_US:
    # with open('/data/python/data/web/transform/type_' + str(language) + '.txt', 'w',encoding='utf-8') \
    #         as  /outpath:
        # for l in en_US:
        #     text.append(l.strip())
        # print("append",text)
    translations = translator.translate(['hospital','school','university','gym','shopping','center','shopping','mall','store','hotel','restaurant','church','bookshop','airport','station','subway','station','bus','stop','street','city','town','road','village','bank','campus','tower','colony','Broadway','park','bookstore','supermarket','market','cinema','post','office','library','museum','science','zoom','stand','fruit','stand','factory','Garden','Company','parking','lot','circle','expressway','Boulevard'], dest = language)
    for translation in translations:
        print(translation.origin)
        print(translation.origin, ' -> ', translation.text)
        # outpath.write(str(translation.text).strip())
        # outpath.write('\n')

if __name__ == '__main__':

    languages = ["fr","ru"]
    # DEFAULT_USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    #
    # SPECIAL_CASES = {
    #     'ee': 'et',
    # }
    #
    # LANGUAGES = {
    #     # 'af': 'afrikaans',
    #     # 'sq': 'albanian',
    #     # 'am': 'amharic',
    #     # 'ar': 'arabic',
    #     # 'hy': 'armenian',
    #     # 'az': 'azerbaijani',
    #     # 'eu': 'basque',
    #     # 'be': 'belarusian',
    #     # 'bn': 'bengali',
    #     # 'bs': 'bosnian',
    #     # 'bg': 'bulgarian',
    #     # 'ca': 'catalan',
    #     # 'ceb': 'cebuano',
    #     # 'ny': 'chichewa',
    #     'zh-cn': 'chinese (simplified)',
    #     'zh-tw': 'chinese (traditional)',
    #     'co': 'corsican',
    #     'hr': 'croatian',
    #     'cs': 'czech',
    #     'da': 'danish',
    #     'nl': 'dutch',
    #     'en': 'english',
    #     'eo': 'esperanto',
    #     'et': 'estonian',
    #     'tl': 'filipino',
    #     'fi': 'finnish',
    #     'fr': 'french',
    #     'fy': 'frisian',
    #     'gl': 'galician',
    #     'ka': 'georgian',
    #     'de': 'german',
    #     'el': 'greek',
    #     'gu': 'gujarati',
    #     'ht': 'haitian creole',
    #     'ha': 'hausa',
    #     'haw': 'hawaiian',
    #     'iw': 'hebrew',
    #     'hi': 'hindi',
    #     'hmn': 'hmong',
    #     'hu': 'hungarian',
    #     'is': 'icelandic',
    #     'ig': 'igbo',
    #     'id': 'indonesian',
    #     'ga': 'irish',
    #     'it': 'italian',
    #     'ja': 'japanese',
    #     'jw': 'javanese',
    #     'kn': 'kannada',
    #     'kk': 'kazakh',
    #     'km': 'khmer',
    #     'ko': 'korean',
    #     'ku': 'kurdish (kurmanji)',
    #     'ky': 'kyrgyz',
    #     'lo': 'lao',
    #     'la': 'latin',
    #     'lv': 'latvian',
    #     'lt': 'lithuanian',
    #     'lb': 'luxembourgish',
    #     'mk': 'macedonian',
    #     'mg': 'malagasy',
    #     'ms': 'malay',
    #     'ml': 'malayalam',
    #     'mt': 'maltese',
    #     'mi': 'maori',
    #     'mr': 'marathi',
    #     'mn': 'mongolian',
    #     'my': 'myanmar (burmese)',
    #     'ne': 'nepali',
    #     'no': 'norwegian',
    #     'ps': 'pashto',
    #     'fa': 'persian',
    #     'pl': 'polish',
    #     'pt': 'portuguese',
    #     'pa': 'punjabi',
    #     'ro': 'romanian',
    #     'ru': 'russian',
    #     'sm': 'samoan',
    #     'gd': 'scots gaelic',
    #     'sr': 'serbian',
    #     'st': 'sesotho',
    #     'sn': 'shona',
    #     'sd': 'sindhi',
    #     'si': 'sinhala',
    #     'sk': 'slovak',
    #     'sl': 'slovenian',
    #     'so': 'somali',
    #     'es': 'spanish',
    #     'su': 'sundanese',
    #     'sw': 'swahili',
    #     'sv': 'swedish',
    #     'tg': 'tajik',
    #     'ta': 'tamil',
    #     'te': 'telugu',
    #     'th': 'thai',
    #     'tr': 'turkish',
    #     'uk': 'ukrainian',
    #     'ur': 'urdu',
    #     'uz': 'uzbek',
    #     'vi': 'vietnamese',
    #     'cy': 'welsh',
    #     'xh': 'xhosa',
    #     'yi': 'yiddish',
    #     'yo': 'yoruba',
    #     'zu': 'zulu',
    #     'fil': 'Filipino',
    #     'he': 'Hebrew'
    # }
#
    # LANGCODES = dict(map(reversed, LANGUAGES.items()))
    # languages = ["ar"]
    # transform(language)
    for language in languages:
        print("language:"+language)
        transform(language)
    print("Finish")
