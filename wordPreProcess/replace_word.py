# import os
# from utils.reExpression import replace_quotes, replace_clock_time, replace_brackets
import re

from utils.reExpression import getCharacterPattern

Czech_noCharacters = re.compile(r'[AaÁáBbCcČčDdĎďEeÉéĚěFfGgHhChchIiÍíJjKkLlMmNnŇňOoÓóPpQqRrŘřSsŠšTtŤťUuÚúŮůVvWwXxYyÝýZzŽž\s]+')
# AaÁáBbCcČčDdĎďEeÉéĚěFfGgHhChchIiÍíJjKkLlMmNnŇňOoÓóPpQqRrŘřSsŠšTtŤťUuÚúŮůVvWwXxYyÝýZzŽž
data_folder = '/Users/ff/Desktop/jieke_replace.txt'
names = []
# for dir_path, subpaths, files in os.walk(data_folder):
#     for name in filter(lambda x: x.endswith('_tok.txt'), files):  # 文件夹下的所有文件
#         file_path = os.path.join(dir_path, name)
#         names.append(name)

# for name in names:
# file_path = os.path.join(data_folder, name)
print(data_folder)
# characterPattern = getCharacterPattern("cs")
with open(data_folder, encoding='utf-8') as f:
    with open(data_folder.replace('.txt', '_replace14.txt'), 'w', encoding='utf-8') as f2:
        # print(f2)
        for line in f:
            line = line.lstrip()
            isMathch = re.findall(Czech_noCharacters, line)
            # print(isMathch, line)
            if(len(isMathch)==1 & isMathch[0]!="\n"):
            # # print(isMathch)
            # # print(isMathch)
            # # if(isMathch!=None):
            # # print(line.index("("))
            # if(isMathch):
            #     # print(line)
                print(isMathch,line)
                while(line.find("(")!=-1 & line.find(")")!=-1):
                    begin = line.index('(')
                    end = line.index(')')
                    line = str(line[0:begin])+str(line[end+1:])
                article = line.replace('/', '\n').replace(' ','\n').strip()
            # # line = replace_brackets(line)
            # # line = replace_clock_time(line)
            # # line = replace_quotes(line)
                f2.writelines(article.strip())
                f2.writelines("\n")
print("Finished!")
