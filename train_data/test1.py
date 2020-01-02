# import os
# ## 测试ar_unigram
# import re
#
# from utils.reExpression import replace_brackets, replace_clock_time, replace_quotes
#
# regex = re.compile(r'[,ـًٌٍَُِّْٰٖٕٓٔ¹½⅓¼⅛²⅔³¾⅜⅝⁴⅞@#¢$₱€£¥%٪‰&_\-—–·+±)}>﴿({<﴾*★٭"„“”»«\'‚‘’›‹:;؛¡!?؟'
#                                  r'/،.~`|♪•√πΠ÷×§¶∆≠≈∞′″←↑↓→^\\©®™℅\]\[\s]+')
# # regex2 = re.compile('[^\s+abcdefghijklmnopqrstuvwxyzåäöABCDEFGHIJKLMNOPQRSTUVWXYZAÅÄOÖ0-9]')
# # regex3=re.compile('[ـ]')
# # line='وتدعـــــــو لــــــــه بظهـــــــــر الغيـــب ان يكـــــــــون سعيـــــــــداليس بالضروري ان يكون لديك أصدقاء كثيرون لتكون ذو شخصية معروفه'
# # line = "Ei saa tarpeeks ruutuaikaa koosteessa. 24/7 heittää hemmetin hyvää läppää! "
# # regex2 = re.compile('"\s+\w+\s+"')
# # s=' Olgi Tokarczuk " a " b " c " s "'
# # words=regex.split(s.strip())
# # s.replace(r'["\s+\w+\s+"]')
# # for w in re.findall(regex2,s):
# #     a=w[2:3]
# #     print(a)
# #     w=re.sub('','',w)
# #     print(w)
# s='ⁿ∅\])}>{<(\[±+_\-—–·&‰%¢$£¥€₱#@†*‡★„“\"”«»’‚‘‹›:;¡!¿?/,….~`|♪♣♠♥♦•√÷πΠ×§"¶∆≠=≈∞′″↑^←↓→°\\' \
#   '\]}>{<\[±_—–·‰¢€₱£¥†‡★“”„«»’‘‚‹›¡¿?/.~`|♪•♣♠♥♦√πΠ÷×§¶∆≠=≈∞′°″↑^←↓→\\©®™℅≤≥,…©®™℅≤≥,ـًٌٍَُِّْٰٖٕٓٔ' \
#   '∅@#€₱$¢£¥‰%&\-—_–·+±{<\[()\]}>*†‡★\"„“”«»:;¡!¿?~`\|•♣♠♪♥♦√Ππ÷×§¶∆^←↑↓→′″°∞=≠≈\\©®™℅≤≥…,' \
#   '¹ⁿ฿₱£¥€$¢%‰&—–·+±(<{[)>}\]*†‡★"„“”«»‚‘’‹›;¡¿…~`|•♣♠♪♥♦√Ππ÷×§¶∆←↑↓→^′″°∞≠≈=\\©®™℅≤≥½⅓¼⅛²⅔³¾' \
#   '⅜⅝⁴⅞@#¢$₱€£¥%٪‰&_\-—–·+±)}>﴿({<﴾*★٭„“”»«\'‚‘’›‹:;؛¡!?؟ /،.~`|♪•√πΠ÷×§¶∆≠≈∞′″←↑↓→^\\©®™℅\]\['
# a=set()
# regex2=re.compile('')
# s=re.compile('\\[\\ٍ„”←×¢€ْٕ¿%:~★}¶³;″¹♦≈²⅞⅜⅝‘ٓ{–\\^\\$?¼≤⅓¡\\[±♥↑→↓÷؟ّٰ«∞•\\]\\=°⅛`⁴₱♪£٭ً≠\\)<‡⅔#√؛‚“′¾\s]+'\\›|\\∆»&π§\\ـ\\\(\\\\@\"\\+_\\∅ٖ‹*®Π﴿ٌُ½…﴾©!>,℅\-‰≥—♣·ٔⁿ٪♠.™¥†َ’\\/฿ِ،]')
# # # s='\\ٍ„”←×¢€ْٕ¿%:~★}¶³;″¹♦≈²⅞⅜⅝‘ٓ{–^$?¼≤⅓¡[±♥↑→↓÷؟ّٰ«∞•]=›|∆»&π§ـ(@"+_∅ٖ‹*®Π﴿ٌُ½…﴾©!>,℅-‰≥—♣·ٔⁿ٪♠.™¥†َ’/฿ِ،'°⅛`⁴₱♪£٭ً≠)<‡⅔#'√؛‚“′¾'\\
# # words=regex2.split(s)
# # for w in words:
# #     if w.strip() not in a:
# #         a.add(w.strip())
# #     else:
# #         continue
# # aaa="".join(a)
# # print(aaa)
# # with open("/Users/ff/Desktop/data/word/runword/notAddNoise/scenes/1/pl_web_tok.txt", 'r', encoding='utf-8') as f_in:
# #     for line in f_in:
# #         aaa = regex.split(line.strip())
# #         # print(len(aaa))
# #         if len(aaa) >= 3:
# #             pass
# #             # print(1)
# #         else:
# #             print(line)
# #             continue
# # line = line.lstrip()
# # line = replace_brackets(line)
# # line = replace_clock_time(line)
# # line = replace_quotes(line)
# # print(line)
# # print()
#
# # line.replace()
# # words=re.find(regex2,line)
# # words=re.findall(regex3,line)
# # for w in words:
# #     line=line.replace(w,'')
# #     print(w)
# # # line=line.replace()
# # print(line)
#
# # 测词频
# # language = "it"
# # data_folder = '/Users/ff/Desktop/train_data/' + language + '/' + language + '_user_web_train'
# # names = []
# # for dir_path, subpaths, files in os.walk(data_folder):
# #     for name in filter(lambda x: x.endswith('w'), files):  # 文件夹下的所有文件
# #         file_path = os.path.join(dir_path, name)
# #         names.append(name)
# # file_path = '/Users/ff/Desktop/train_data/' + language + '/' + language + '_user_web_train/vocab_words_true'
# # count_all = 0
# # count=0
# # with open(file_path, 'r', encoding='utf-8') as f_all:
# #     for line in f_all:
# #         fileds = line.strip().split('\t')
# #         count+=1
# #         count_all += int(fileds[1])
# # print("all count:",count_all)
# # count_all_2w = 0
# # count_all_3w = 0
# # count_all_4w = 0
# # count_all_5w = 0
# # for name in names:
# #     file_path = os.path.join(data_folder, name)
# #     # print(file_path)
# #
# #     with open(file_path, 'r', encoding='utf-8') as f:
# #         if file_path.endswith('2w'):
# #             for line in f:
# #                 fileds = line.strip().split('\t')
# #                 count_all_2w += int(fileds[1])
# #         if file_path.endswith('3w'):
# #             for line in f:
# #                 fileds = line.strip().split('\t')
# #                 count_all_3w += int(fileds[1])
# #         if file_path.endswith('4w'):
# #             for line in f:
# #                 fileds = line.strip().split('\t')
# #                 count_all_4w += int(fileds[1])
# #         if file_path.endswith('5w'):
# #             for line in f:
# #                 fileds = line.strip().split('\t')
# #                 count_all_5w += int(fileds[1])
# # print(count,"\t",count_all,"\t",float(count_all_2w/count_all),"\t",float(count_all_3w/count_all),"\t",float(count_all_4w/count_all),"\t",float(count_all_5w/count_all))

import re

s = 'American ( United ? \' 2 States of ) '
l=re.sub(r"(\w+) ?\' (\w+)?",r"\1'\2",s)
print(l)
# r = re.search('(\(.*?\))', s)
# if r:
#     print(r.group())
