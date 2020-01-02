# 查找某个文件包含某个词的句子
import os
import re

data_folder = '/Users/ff/Desktop/测评数据/查找句子'
names = []
search1 = set()
search2 = set()
search3 = set()

# string="hh hh ?? ?! ????AAA    ?  ?  A ??"
# ss=re.findall(regex,string)
# for s in ss:
#     string=string.replace(re.sub('\s+',string),'')
# print(string)
regex = re.compile('\|#\|')
for dir_path, subpaths, files in os.walk(data_folder):
    for name in filter(lambda x: x.endswith('.txt'), files):  # 文件夹下的所有文件
        file_path = os.path.join(dir_path, name)
        names.append(name)
for name in names:
    file_path = os.path.join(data_folder, name)
    print(file_path)

    if os.path.exists(file_path.replace('.txt', '.search1')):
        print("remove:", file_path.replace('.txt', '.search1'))
        os.remove(file_path.replace('.txt', '.search1'))
    with open(file_path, 'r', encoding='utf-8') as f_in:
        with open(file_path.replace('.txt', '.search1'), 'a', encoding='utf-8') as f_out:
            with open(file_path.replace('.txt', '.search2'), 'a', encoding='utf-8') as f_out2:
                with open(file_path.replace('.txt', '.search3'), 'a', encoding='utf-8') as f_out3:
                    for line in f_in:
                        words = regex.split(line.strip())
                        if len(words) == 2:
                            lines = words[1]
                            # start = line.strip()
                            # lines = line.strip()[start:]
                            s = "dads"
                            s2 = "Fathers"
                            s3 = "Christian"
                            # print(lines.find(s))
                            if lines.find(s) >= 0:
                                if lines not in search1:
                                    print(lines)
                                    search1.add(lines)
                                    f_out.write(lines.strip())
                                    f_out.write('\n')
                                else:
                                    continue
                            if lines.find(s2) >= 0:
                                if lines not in search2:
                                    search2.add(lines)
                                    print(lines)
                                    f_out2.write(lines.strip())
                                    f_out2.write('\n')
                                else:
                                    continue
                            if lines.find(s3) >= 0:
                                if lines not in search3:
                                    print(lines)
                                    search3.add(lines)
                                    f_out3.write(lines.strip())
                                    f_out3.write('\n')
                                else:
                                    continue
                            else:
                                continue
                        else:
                            continue
print("Finish Line")
