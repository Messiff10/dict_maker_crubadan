"""
处理表情词典 去重
"""

language = "en"
file_emoji = "/Users/ff/Desktop/data/dict/input/" + language + "/" + language + "_shortcutTargets_out.txt"
file_emoji_out = "/Users/ff/Desktop/data/dict/input/" + language + "/" + language + "_shortcutTargets.txt"
unigram = {}
# with open(file_emoji, 'r', encoding='utf-8') as f_in:
#     for line in f_in:
#         words = line.strip().split('\t')
#         # print(line)
#         if len(words) == 3:
#             if words[0] in unigram.keys():
#                 if int(words[2]) > int(unigram[words[0]][0]):
#                     unigram[words[0]] = (words[2], words[1])
#                     # unigram[words[0][1]] = words[2]
#             else:
#                 print(line)
#                 unigram[words[0]] = (words[2], words[1])
#                 # print(unigram)
#                 # unigram[words[0][1]] = words[2]
#
# with open(file_emoji_out, 'w', encoding='utf-8') as f_out:
#     for line in unigram.items():
#         print(line[1][0])
#         if int(line[1][0]) > 250:
#             freq = 250
#         else:
#             freq = int(line[1][0])
#         result = line[0] + "\t" + "false" + "\t" + str(freq) + "\t" + line[1][1] + "\t" + str(15)
#         f_out.write(result.strip())
#         f_out.write('\n')

# with open(file_emoji, 'r', encoding='utf-8') as f_in:
#     with open(file_emoji_out, 'w', encoding='utf-8') as f_out:
#         for line in f_in:
#             print(line)
#             words = line.strip().split('\t')
#             if len(words)==3:
#                 ls = words[2].strip().split(',')
#                 for l in ls:
#                     f_out.write((l + "\t" + words[1] + "\t" + words[0]).strip())
#                     f_out.write('\n')
print("Finish line")
