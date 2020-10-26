import re
"""
处理纠错log
"""
file = open("/Users/ff/Desktop/word_output_huawei_ur_correct_17_0831_1598943561.txt", 'r', encoding='utf-8')
file_out = open("/Users/ff/Desktop/word_output_huawei_ur_correct_17.txt", 'w', encoding='utf-8')
regex = re.compile('input=(.*),\s+desire=(.*)\t(.*)screen=\[(.*)\]\):')
for l in file:
    # l="TASK: input=a, desire=b 	WORD(input=[آفریدی]|desire=[آفریدی]|screen=[آفریدی]): (autoCorrectHappen=0, correctPositiveCount=0, needToCorrectWordCount=0, autoCorrectHappenIncandidateTop3=0) "
    if l.startswith("TASK") and '\t' in l:
        # print(l)
        # input= l.split('\t')[0]
        input = regex.search(l)
        if input.group(1).strip() != input.group(2).strip():
            result="input="+input.group(1)+'\t'+"desire="+input.group(2)+'\t'+"screen="+input.group(4)
            file_out.write(result.strip() + '\n')
    else:
        file_out.write(l.strip() + '\n')

# if regex.match(input):
#     input1 = lambda x: x.group(1)
#     print(input1)
