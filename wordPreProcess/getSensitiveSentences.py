import re
import os
from config.conf import languages, priority, scenes_names
from utils.reExpression import pattern_email, pattern_phoneNum, pattern_password, pattern_continuousNum, pattern_at

# 提取敏感词
regex = re.compile('\s+')


def containSensitiveInfo(sentence):
    isContainSensitiveInfo = False

    isContainEmail = re.search(pattern_email, sentence)
    isContainContinuousNum = re.search(pattern_continuousNum, sentence)
    isContainAt = re.search(pattern_at, sentence)
    items = sentence.strip().split(' ')
    for item in items:
        isContainPhoneNum = re.search(pattern_phoneNum, item)
        isContainPassword = re.search(pattern_password, item)

        if isContainEmail or isContainPhoneNum or isContainPassword or isContainContinuousNum or isContainAt:
            isContainSensitiveInfo = True
            break

    return isContainSensitiveInfo


def getSensitiveSent():
    # 去除包含敏感信息的句子
    print("languages", languages)
    print("scenes_names", scenes_names)
    for language in languages:
        for scene in scenes_names:
            if scene == "":
                suffix = priority + '/' + language + '_.txt'
            else:
                suffix = priority + '/' + language + '_' + scene + '_.txt'
            # 直接运行spark所提取的语料位置
            input_file_name = '/Users/ff/Desktop/data/word/spark_language_data/' + suffix
            # 处理过后敏感词存放的位置
            output_file_name = '/Users/ff/Desktop/data/word/sensitive/' + suffix

            if not os.path.exists(input_file_name):
                print(input_file_name, "doesn't exists!")
                continue

            with open(input_file_name, 'r', encoding='utf-8') as input_file:
                count = 0
                res_sensitive = []
                res_not_sensitive = []
                with open(output_file_name, 'w', encoding='utf-8') as output_file:
                    for line in input_file:
                        fileds = regex.split(line.strip())
                        if len(fileds) >= 3:
                            count += 1
                            if containSensitiveInfo(line):
                                res_sensitive.append(line)
                                # print(line)
                                output_file.write(line + '\n')
                            else:
                                res_not_sensitive.append(line)
                        else:
                            print(line)
                            continue

                print(language, ":", count, ",", "count_sensitive:", str(len(res_sensitive)))

            with open(input_file_name, 'w', encoding='utf-8') as output_file:
                print("rewriting", input_file_name, "size:", str(len(res_not_sensitive)))
                output_file.writelines(res_not_sensitive)


if __name__ == "__main__":
    getSensitiveSent()
    print("Finished!")
