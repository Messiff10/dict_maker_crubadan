import codecs
import re

en_US_noCharacters = re.compile(r"[[0-9a-zA-ZàâäôéèëêïîçùûüÿæœÀÂÄÔÉÈËÊÏÎŸÇÙÛÜÆŒąćęłńóśźżĄĆĘŁŃÓŚŹŻàèéìíîòóùúÀÈÉÌÍÎÒÓÙÚáé"
                                r"íñóúüÁÉÍÑÓÚÜа-яА-Я\u0627-\u064a"
                                r"q1w2e3èéēêër4t5y67uûúūüùiî8íìïīo9óôöòœøōõp0)l(k+j\-h&g%f$d#ßs@aàáâäæãåāz*x\"c'v:ç"
                                r";b!nñm¹½⅓¼⅛²⅔³⅜¾⁴⅝⅞ⁿ∅\]}>{<\[±_—–·‰¢€₱£¥†‡★“”„«»’‘‚‹›¡¿?/.~`|♪•♣♠♥♦√πΠ÷×§¶∆"
                                r"≠=≈∞′°″↑^←↓→\\©®™℅≤≥,…\s]+")

Characters = re.compile(r"[q1w2e3éèêėëęēr4t5y6u7úùūûüi8ìíîįïīo9òóôöõœøōºp0aàáâäæãåāªsdfghjklzxcvbnm¹½⅓¼⅛²⅔³"
                                  r"¾⅜⁴⅝⅞ⁿ∅@#€₱$¢£¥%‰&_\-—–·+±(<{\[)\]}>*†‡★\"„“”«»'‚‘’‹›:;!¡?¿/,.…~`|•♣♠♪♥♦√πΠ÷×§¶∆≠="
                                  r"≈∞°′″↑↓→←^\\©®™℅≥≤\s]+")


regex = re.compile('\s+')
# l="🤣🤣🤣a Prego😉 costez 😂😂😂😂😂😂😂"
# fileds = regex.split(l)
# for word in fileds:
#     print("word+" + word)
#     line = l
#     if not re.match(Characters, word) is None:
#         line = " "
#         print("不带有表情")
#         break
#     else:
#         print("带有表情")
#

all_unigram_count = 0
all_crawl_count = 0
true_count = 0
false_count = 0
true_rate = 0.0
crawl_words = set()
unigram_words = set()
# false_words = set()
# true_words = set()
false_words = set()
true_words = set()
unigram_path = '/Users/ff/Desktop/第一优先级语言词表/desc/第一优先级词表所有降序/it_unigram'
with codecs.open(unigram_path, encoding='utf-8') as f2:
    with codecs.open(unigram_path.replace('_unigram', '_no_emoji_unigram'), 'w', encoding='utf-8') as f_no_emoji:
        for line in f2:
            fileds = line.strip().split('\t')
            if str(line.strip()) is not "":
                if len(fileds) == 2:
                    if not re.match(Characters, fileds[0]) is None:
                        if fileds[0] not in unigram_words:
                            all_unigram_count += 1
                            unigram_words.add(line.strip())
                            f_no_emoji.write(line.strip())
                            f_no_emoji.write('\n')