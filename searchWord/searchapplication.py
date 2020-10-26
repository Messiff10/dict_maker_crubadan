# 查找某个文件包含某个词的句子
import os
import re
"""
查找相关场景的语句
"""
data_folder = '/Users/ff/Desktop/测评数据/获取相关字段文件'
names = []
searchfacebook = set()
searchim = set()

# string="hh hh ?? ?! ????AAA    ?  ?  A ??"
# ss=re.findall(regex,string)
# for s in ss:
#     string=string.replace(re.sub('\s+',string),'')
# print(string)
# regex = re.compile('\|#\|')
facebook=["com.facebook.orca","com.facebook.katana"]
im=["com.whatsapp","com.instagram.android","com.gbwhatsapp","com.snapchat.android","com.vkontakte.android","com.WhatsApp2Plus","com.yowhatsapp","com.whatsapp.w4b"]
for dir_path, subpaths, files in os.walk(data_folder):
    for name in filter(lambda x: x.endswith('.txt'), files):  # 文件夹下的所有文件
        file_path = os.path.join(dir_path, name)
        names.append(name)
for name in names:
    file_path = os.path.join(data_folder, name)
    print(file_path)

    if os.path.exists(file_path.replace('.txt', '.facebook')):
        print("remove:", file_path.replace('.txt', '.facebook'))
        os.remove(file_path.replace('.txt', '.facebook'))
    if os.path.exists(file_path.replace('.txt', '.im')):
        print("remove:", file_path.replace('.txt', '.im'))
        os.remove(file_path.replace('.txt', '.im'))
    with open(file_path, 'r', encoding='utf-8') as f_in:
        with open(file_path.replace('.txt', '.facebook'), 'a', encoding='utf-8') as f_facebook:
            with open(file_path.replace('.txt', '.im'), 'a', encoding='utf-8') as f_im:
                    for line in f_in:
                        words = line.strip().split('\t')
                        if len(words) == 7:
                            # lines = words[1]
                            # start = line.strip()
                            # lines = line.strip()[start:]
                            # print(lines.find(s))
                            # print(words[0])
                            if words[0] in facebook:
                                if words[1].strip() not in searchfacebook:
                                    searchfacebook.add(words[1].strip())
                                    f_facebook.write(words[1].strip())
                                    f_facebook.write('\n')
                            if words[0] in im:
                                if words[1].strip() not in searchim:
                                    searchim.add(words[1].strip())
                                    f_im.write(words[1].strip())
                                    f_im.write('\n')
                        else:
                            print(len(words),line)
                            continue

print("Finish Line")
