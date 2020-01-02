import codecs
import os
from utils.reExpression import replace_quotes, replace_clock_time, replace_brackets
import re
##  去中括号
# data_folder = '/Users/ff/Desktop/train_data/ms_MY/ms_MY_web.txt'
# with codecs.open(data_folder, encoding='utf-8') as f:
#     with codecs.open(data_folder.replace('.txt', '_script.txt'), 'w', encoding='utf-8') as f2:
#         # print(f2)
#         for line in f:
#             line = re.sub("\\[.*?]|\\{.*?}|\\(.*?\\)", "", line)
#             # line.replaceAll("\\{.*?}", "")
#             f2.writelines(line)
# print("Finished!")
line=" ha messo in commercio ” edizioni „ sddff con località \"\ francesi \"\,  [olandesi] ,  spagnole ,  statunitensi  e messicane .  try  {  MNZ_RICH ( 'Bottom' )  ;  }  catch ( e )   {  }"

def isValid(s):
        """
        :type s: str
        :rtype: bool
        """
        ss=s.strip().split('\\s+')
        temp_str = []       #存放临时开括号
        openParentheses = ["(","[","{"]
        combineParentheses = ["()","[]","{}"]
        for cha in ss:
            print(cha)
            if cha in openParentheses:       #如果是开括号就放入temp_str中
                temp_str.append(cha)
                print(cha)
            else:
                if not temp_str:       #如果temp_str为空，返回False
                    return False
                else:
                    temp_cha = temp_str.pop() + cha     #弹出，组合
                    if temp_cha not in combineParentheses:
                        pass
        print(temp_cha)
                        # return False
        # return temp_cha
        # if not temp_str:     #判断是否存在多余开括号
        #     return True
        # else:
        #     return False
# print(f2)
# regex=re.compile('([\w+])|({\w+})|((\w+))|')
# words=regex.split(line)
# for w in words:
#     print(w)
# line = re.sub("\\[\w+]|{\w+}|\\(\w+\\)|", "", line)
# # line.replaceAll("\\{.*?}", "")
#
# print(line)
# print("Finished!")

if __name__ == '__main__':
    isValid(line)

