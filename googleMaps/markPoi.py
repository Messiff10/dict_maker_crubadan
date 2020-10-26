import os
import re

file_path = "/Users/ff/Desktop/maps/mark/ru_20200420.txt"
out_path = "/Users/ff/Desktop/maps/mark/out_ru.txt"
address_c = set()
address_c_lower = set()
address_t = set()
address_t_lower = set()
address_n = set()
address_n_lower = set()
address_p = set()
address_p_lower = set()
address_b = set()
address_b_lower = set()
address_r = set()
address_r_lower = set()
address_all_set = [{"country": address_c}, {"towns": address_t}, {"province": address_p}, {"type": address_n},
                   {"poi": address_b}
    , {"roads": address_r}]
centence_original = {}
emoji_path = "/Users/ff/Desktop/train_data/all_emojis"
emojiset = set()
regex = re.compile('\s+')
regex_pun = re.compile('[\-±+_·‰%¢$£¥₱€#@†*‡★؟\‚\;/,….~`♪•♣♠♥♦√πΠ÷×§¶∆≠=≈∞°↑^←‚;?/,….~`♪•♣♠♥♦√πΠ÷×§¶←↓→\\©®™℅,'
                       'ـًٌٍَُِّْٰٖٕٓٔ¹½⅓¼⅛²⅔³¾⅜⅝⁴⅞@#¢₱€£¥%٪‰_·+±\\﴾*★٭\‚‹;؛∆≠=≈!∞°،↑)}\]’’>›»’↓→\±+_\·‰٪%¢£¥₱€#@†*‡★\©®™℅]')

regex_line = re.compile("\\|")
data_folder = "/Users/ff/Desktop/maps/ru"
names = []
result = set()


def getemoji():
    with open(emoji_path, 'r', encoding='utf-8') as f_emoji:
        for line in f_emoji:
            emojis = line.strip().split('\t')
            if emojis[0] not in emojiset:
                emojiset.add(emojis[0])


def getAllFile():
    # 无后缀
    for dir_path, subpaths, files in os.walk(data_folder):
        for name in files:  # 文件夹下的所有文件
            if not name.endswith('.DS_Store'):
                file_path = os.path.join(dir_path, name)
                names.append(name)
    for name in names:
        file_path = os.path.join(data_folder, name)
        # print(file_path)
        with open(file_path, 'r', encoding='utf-8') as f_add:
            for line in f_add:
                line = re.sub(regex_pun, ' ', line)
                line = re.sub('\s+', ' ', line)
                if len(line) > 1:
                    # ads = line.split('\t')
                    if name.startswith("country"):
                        if " " + re.sub('\s+', ' ', line.strip()) + " " not in address_c:
                            address_c.add(" " + re.sub('\s+', ' ', line.strip()) + " ")
                            address_c_lower.add(" " + re.sub('\s+', ' ', line.strip().lower()) + " ")
                    if name.startswith("towns"):
                        if " " + re.sub('\s+', ' ', line.strip()) + " " not in address_t:
                            address_t.add(" " + re.sub('\s+', ' ', line.strip()) + " ")
                            address_t_lower.add(" " + re.sub('\s+', ' ', line.strip().lower()) + " ")
                    if name.startswith("province"):
                        if " " + re.sub('\s+', ' ', line.strip()) + " " not in address_p:
                            address_p.add(" " + re.sub('\s+', ' ', line.strip()) + " ")
                            address_p_lower.add(" " + re.sub('\s+', ' ', line.strip().lower()) + " ")
                    if name.startswith("roads"):
                        if " " + re.sub('\s+', ' ', line.strip()) + " " not in address_r:
                            address_r.add(" " + re.sub('\s+', ' ', line.strip()) + " ")
                            address_r_lower.add(" " + re.sub('\s+', ' ', line.strip().lower()) + " ")
                    if name.startswith("poi"):
                        if " " + re.sub('\s+', ' ', line.strip()) + " " not in address_b:
                            address_b.add(" " + re.sub('\s+', ' ', line.strip()) + " ")
                            address_b_lower.add(" " + re.sub('\s+', ' ', line.strip().lower()) + " ")
                    if name.startswith("type"):
                        if " " + re.sub('\s+', ' ', line.strip()) + " " not in address_n:
                            address_n.add(" " + re.sub('\s+', ' ', line.strip()) + " ")
                            address_n_lower.add(" " + re.sub('\s+', ' ', line.strip().lower()) + " ")


def makeMark():
    with open(file_path, 'r', encoding='utf-8') as f_in:
        with open(out_path, 'w', encoding='utf-8') as f_out:
            for line in f_in:
                type_count = 0
                for a in emojiset:
                    if line.find(a) >= 0:
                        line = line.replace(a, ' ')
                line_original = line.strip()
                line_original = re.sub('\s+', ' ', line_original)
                line = line_original
                line = re.sub(regex_pun, ' ', line)
                line = re.sub('\s+', ' ', line)
                line = " " + str(line) + " "
                # print(line)
                line_result = []
                for acb in address_b_lower:
                    if acb in line.lower():
                        # reg = re.compile(re.escape(acb), re.IGNORECASE)
                        if not "POI" in line_result:
                            line_result.append("POI")
                        type_count += 1
                        # line = str.sub(" |" + re.sub('\s+', '^', acb) + "： &&poi| ",line,re.IGNORECASE)
                        start = line.lower().index(acb)
                        line = line.replace(line[start:start + len(acb)]," |" + re.sub('\s+', '^', line[start:start + len(acb)]) + "： &&poi| ")
                        # print("poi", acb, line)
                for acc in address_c_lower:
                    if acc in line.lower():
                        if not "地址" in line_result:
                            line_result.append("地址")
                        type_count += 1
                        start = line.lower().index(acc)
                        line = line.replace(line[start:start + len(acc)]," |" + re.sub('\s+', '^', line[start:start + len(acc)]) + "： &&country| ")
                for act in address_t_lower:
                    if act in line.lower():
                        if not "地址" in line_result:
                            line_result.append("地址")
                        type_count += 1
                        start = line.lower().index(act)
                        line = line.replace(line[start:start + len(act)], " |" + re.sub('\s+', '^', line[start:start + len(act)]) + "： &&city&towns| ")
                for acp in address_p_lower:
                    if acp in line.lower():
                        if not "地址" in line_result:
                            line_result.append("地址")
                        type_count += 1
                        start = line.lower().index(acp)
                        line = line.replace(line[start:start + len(acp)], " |" + re.sub('\s+', '^', line[start:start + len(acp)]) + "： &&provinces&states| ")
                for acr in address_r_lower:
                    if acr in line.lower():
                        if not "地址" in line_result:
                            line_result.append("地址")
                        type_count += 1
                        start = line.lower().index(acr)
                        line = line.replace(line[start:start + len(acr)]," |" + re.sub('\s+', '^', line[start:start + len(acr)]) + "： &&roads| ")
                for acn in address_n_lower:
                    if acn in line.lower():
                        if not "类型" in line_result:
                            line_result.append("类型")
                        type_count += 1
                        start = line.lower().index(acn)
                        line = line.replace(line[start:start + len(acn)]," |" + re.sub('\s+', '^', line[start:start + len(acn)]) + "： &&type| ")
                all_words = regex_line.split(line)
                # print(all_words, line_result)
                for word in range(0, len(all_words)):
                    if " " not in all_words[word].strip() and all_words[word].strip() != "":  # 只有一个单词
                        if word != 0 and word != len(all_words) - 1 and not re.search(regex_pun,
                                                                                      all_words[word]):  # 属于过渡词
                            if all_words[word].strip().isdigit():
                                all_words[word] = " |" + re.sub('\s+', '^', all_words[word]) + "： &&number| "
                            else:
                                all_words[word] = " |" + re.sub('\s+', '^', all_words[word]) + "： &&prop| "
                        else:
                            if "&&" not in all_words[word]:  # 属于噪声数据
                                if len(all_words[word].strip()) > 1 and all_words[word].strip().isdigit():
                                    all_words[word] = " |" + re.sub('\s+', '^', all_words[word]) + "： &&number| "
                                else:
                                    all_words[word] = ""
                    else:
                        if "&&" not in all_words[word]:  # 属于噪声数据
                            all_words[word] = ""
                        else:
                            all_words[word] = all_words[word]
                line = "|".join(all_words)
                # print("-----",line)
                line = line.replace('|^', '|').replace('^： &&', ': ').replace('^', ' ').replace('||', '|')
                line = re.sub('\\|\s+\\|', '|', line.strip())
                # print(line)
                if line.strip().startswith("|"):
                    line = line.strip()[1:]
                if line.strip().endswith("|"):
                    line = line.strip()[:len(line.strip()) - 1]
                # print(line)
                line_result = "+".join(line_result)
                if line.strip() != "" and int(type_count) > 1 and len(line_original.lower()) <= len(
                        line.lower()) and line.strip() not in result:
                    result.add(line.strip())
                    f_out.write((line_original + "\t" + line_result + "\t" + line).strip())
                    f_out.write('\n')


if __name__ == '__main__':
    getemoji()
    getAllFile()
    makeMark()

    print("Finish line")
