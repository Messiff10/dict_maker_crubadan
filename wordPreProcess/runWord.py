from utils.is_emoji import is_emoji
from utils.getWordMap import getWordMap
from utils.getUnigram import getUnigram
from utils.reExpression import pattern_delete, getCharacterPattern
from config.conf import languages, scenes_names, scenes_ratios, priority, addNoise, \
    max_out_num, isPrint, ifRemoveNoCharacter, filterWordThreshold, dict_dir
import re
import os
import time

# 生成相对应命中率的语料
def runWord():
    # 产生形如"context \t keys \t desired_word"的结果，可用于测试输入效率
    print("languages", languages)
    print("scenes_names", scenes_names)
    print("filterWordThreshold:", str(filterWordThreshold))

    if ifRemoveNoCharacter:
        print("ifRemoveNoCharacter:", ifRemoveNoCharacter)
    # 去掉敏感词的语料所在位置
    input_file_dir = '/Users/ff/Desktop/data/word/spark_language_data/'

    for language in languages:
        if ifRemoveNoCharacter:
            characterPattern = getCharacterPattern(language)
            # print("characterPattern:", characterPattern)

        dict_file_path = dict_dir + language + "_unigram"
        dict_lang = getUnigram(dict_file_path)

        if addNoise:
            print("getting", language, "word_map...")
            wordmap_all = getWordMap(language)
            output_file_dir = '/Users/ff/Desktop/data/word/runword/addNoise/'
        else:
            output_file_dir = '/Users/ff/Desktop/data/word/runword/notAddNoise/'
        # 按照场景以及比例生成相关语料
        output_file_name = output_file_dir + priority + '/' + language + '_tok.txt'

        if os.path.exists(output_file_name):
            print("remove", output_file_name)
            os.remove(output_file_name)
        # else:
        #     print(output_file_name, ' does not exists')

        with open(output_file_name, 'a', encoding='utf-8') as output_file:
            count_line = 0
            count_outs = []
            count_inVocabs = []
            for scene, scenes_ratio in zip(scenes_names, scenes_ratios):
                if isPrint:
                    print("start processing", language, scene, "in",
                          time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

                if scene == "":
                    input_file_name = input_file_dir + priority + '/' + language + '_.txt'
                    output_file_scene_name = output_file_dir + 'scenes/' + priority + '/' + language + '_tok.txt'
                else:
                    input_file_name = input_file_dir + priority + '/' + language + '_' + scene + '_.txt'
                    output_file_scene_name = output_file_dir + 'scenes/' + priority + '/' + language + '_' + scene + '_tok.txt'

                max_out_num_scene = max_out_num * scenes_ratio

                if not os.path.exists(input_file_name):
                    print(input_file_name, "doesn't exists!")
                    continue

                with open(input_file_name, 'r', encoding='utf-8') as input_file:
                    count_out = 0  # 处理了多少个词，不包括包含emoji和包含非该语言键盘能敲出来的符号的句子
                    count_inVocab_all = 0  # 语料中在词表中的词的总数
                    count_noCharacter = 0  # 包含非该语言键盘能敲出来的符号的句子
                    count_emoji = 0  # 包含emoji的句子
                    count_noiseword = 0  # 添加的噪声数
                    count_longSent = 0  # 长句数量
                    isAddCountout = False
                    output_scene_res = []
                    for line in input_file:
                        # line = re.sub(pattern_delete, "", line).lower()  # 删除某些符号
                        line = re.sub(pattern_delete, "", line)  # 删除某些符号
                        words = line.strip().strip('"').split(' ')
                        has_emoji = False
                        count_inVocab = 0
                        for word in words:
                            if is_emoji(word):
                                has_emoji = True
                                break
                            if word in dict_lang:
                                count_inVocab += 1
                        wordInVocaRatio = count_inVocab / len(words)
                        if wordInVocaRatio < filterWordThreshold:  # 每句话中在词典中的词小于过滤阈值，则删除整句话
                            continue
                        if has_emoji:
                            count_emoji += 1
                            continue
                        if ifRemoveNoCharacter:
                            isNoCharacter = re.search(characterPattern, line.lower())
                            if isNoCharacter:
                                count_noCharacter += 1
                                # print(language, ":\t", line)
                                continue
                        if len(words) > 15:
                            count_longSent += 1
                            # continue
                        count_line += 1
                        # for i in range(0, len(words)):
                        #     fore = ' '.join(words[:i])
                        #     word = words[i]
                        #     word_lower = words[i].lower()
                        #     if addNoise and (word_lower in wordmap_all):
                        #         wordmap = random_pick_freq(wordmap_all[word_lower].keys(), wordmap_all[word_lower].values())
                        #         noise_word = ''.join(itertools.islice(wordmap, 1))
                        #         output_line = fore + '\t' + noise_word + '\t' + word + '\n'
                        #         if noise_word != word:
                        #             count_noiseword += 1
                        #     else:
                        #         output_line = fore + '\t' + word + '\t' + word + '\n'
                        #     output_file.write(output_line)
                        #     output_scene_res.append(output_line)
                        #
                        #     count_out += 1

                        output_file.write(line)
                        output_scene_res.append(line)
                        count_out += len(words)
                        count_inVocab_all += count_inVocab

                        if count_out >= max_out_num_scene:
                            isAddCountout = True
                            count_outs.append(count_out)
                            count_inVocabs.append(count_inVocab_all)
                            break

                    if not isAddCountout:
                        count_outs.append(count_out)
                        count_inVocabs.append(count_inVocab_all)

                if scene != "":
                    with open(output_file_scene_name, 'w', encoding='utf-8') as output_file_scene:
                        print("writing", output_file_scene_name, "...")
                        output_file_scene.writelines(output_scene_res)

            wordInVocaRatios = [count_inVocab / (count + 1e-4) for count_inVocab, count in zip(count_inVocabs, count_outs)]
            print("language:", language, "\tcount_line:", count_line,
                  "\tcount_out:", count_outs,
                  "\tcount_inVocab:", count_inVocabs,
                  "\twordInVocaRatio:", wordInVocaRatios,
                  "\tcount_noCharacter:", count_noCharacter,
                  "\tcount_emoji:", count_emoji,
                  "\tcount_noiseword:", count_noiseword,
                  "\tcount_longSent:", count_longSent, "in", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))


if __name__ == "__main__":
    runWord()
    print("Finished!")
