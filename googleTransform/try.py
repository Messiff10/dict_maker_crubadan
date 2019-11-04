from googletrans import Translator
import emoji
import time
import re


en_US_noCharacters = re.compile(r"[[0-9a-zA-Z)l(k+j\-h&g%f$d#ßs@aàáâäæãåāz*x\"c'v:ç"
                                r";b!nñm¹½⅓¼⅛²⅔³⅜¾⁴⅝⅞ⁿ∅\]}>{<\[±_—–·‰¢€₱£¥†‡★“”„«»’‘‚‹›¡¿?/.~`|♪•♣♠♥♦√πΠ÷×§¶∆"
                                r"≠=≈∞′°″↑^←↓→\\©®™℅≤≥,…\s]+")

def tx(t):
    return Translator().translate(t, dest=language).text

def transform(language):
    translator = Translator()
    regex = re.compile('\s+')
    setence = []

    with open('/home/zhangzhongfang/news_data/en_US_business.txt', 'r', encoding='utf-8') as en_US:
        with open('/home/zhangzhongfang/news_data/trans_data/business_' + str(language) + '.txt', 'a',encoding='utf-8') \
                as outpath:
            for l in en_US:
                line = l
                print("l--------"+l)
                fileds = regex.split(l.strip())
                for word in fileds:
                    print("word:"+word)
                    # print("trans:"+tx(word))
                    translations = translator.translate(word, dest=language)
                    print("trans:"+translations.text)
                    if (re.match(en_US_noCharacters, word) is None):
                        line = " "
                        print("word:"+word)
                        print("@@@@@@@@@@@@@@@@false")
                        break

                # if(line != " "):
                #     print("=============================")
                #     txd = tx(line)
                #     outpath.write(txd)
                #     outpath.write("\n")
                    # setence.append(txd)
                time.sleep(0.1)

    # translations = translator.translate(setence, dest=language)
    # with open('/home/zhangzhongfang/news_data/trans_data/business'+str(language)+'.txt','a',encoding='utf-8') as outpath:
        # for translation in translations:
        # for i in setence:
        #     print("translation:"+i)
        #     outpath.write(i)
        #     outpath.write("\n")
    # for sen in setence:
    #     if()cd d
    #     print()

if __name__ == '__main__':
    # "zu", "zh-TW"'zh-CN','vi','uk','tr','th','sw','sv','sr','sl','sk','ru','ro','pl','no','nl','ms','lv','lt','ko','ja','it','is','id','et''el','de',
    #                 'da','cs','ca','bg','am','af'
    # 'zh-HK','pt-PT''pt-BR','in''hu','hr''hi','he','fr-FR','fr-CA','fil','fi','es-ES''es-419','en-US','en-GB','it','is','id','et',
    # "ar","de","it","es","ru","pl","fi","sv","da","nb",
    languages = ["ar","de","it","es","ru","pl","fi","sv","da","no","tr","ms_MY","th","es_US"]
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

    # LANGCODES = dict(map(reversed, LANGUAGES.items()))
    # languages = ["ar"]
    # transform(language)
    for language in languages:
        print("language:"+language)
        transform(language)
    print("Finish")




# def translate_doc(filename, destination='zh-CN', mix=False):
#     """
#     translate a word document type of file and save the result as document and keep the exactly same file format.
#         :param filename: word doc file
#         :param destination='zh-CN':
#         :param mix=True: if True, will have original language and target language into the same doc. paragraphs by paragraphs.
#     """
#     def tx(t): return Translator().translate(t, dest=destination).text
#     # doc = Document(filename)
#     for p in doc.paragraphs:
#         txd = tx(p.text)
#
#         p.text = p.text + ('\n' + txd if mix else '')
#
#     # for table in doc.tables:
#     #     for row in table.rows:
#     #         for cell in row.cells:
#     #             txd = tx(cell.text)
#     #             p.text = cell.text + ('\n' + txd if mix else '')
#
#     f = filename.replace('.doc', destination.lower() + '.doc')
#     doc.save(f)
#
# if __name__ == '__main__':
#     filename = 'p1.docx'
#     translate_doc(filename)