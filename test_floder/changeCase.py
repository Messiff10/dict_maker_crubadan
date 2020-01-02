import codecs
import re
import sys

s = 'cs'
data_folder = "/Users/ff/Desktop/测评数据/转换大小写"
unigram_path = data_folder + '/' + s + '_unigram_new'  # 词表
file_path2 = data_folder + '/' + s + '_web_space.txt'  # 原始语料
file_out_path1 = data_folder + '/' + s + '_change.txt'  # 将小写形式在词表，大写不在词表中的词转换成小写
# file_out_path2=data_folder+'/vocab_in_new_not_in_old' #在新不在旧

# unigram_path=sys.argv[1]
# file_path2=sys.argv[2]
# file_out_path1=sys.argv[3]
file1 = set()
file2 = set()
regex = re.compile('\s+')
with codecs.open(unigram_path, encoding='utf-8') as f:
    for line in f:
        words = line.strip().split('\t')
        if words[0].strip() not in file1:
            file1.add(words[0])
with codecs.open(file_path2, encoding='utf-8') as f2:
    with open(file_out_path1, 'w', encoding='utf-8') as f_in_old:
        for line in f2:
            centence = []
            words = regex.split(line.strip())
            for w in words:
                if w in file1:
                    centence.append(str(w))
                else:
                    centence.append(str(w.lower()))
                # else:
                #     centence.append(w)
            s = " ".join(centence)
            s=re.sub('\s+',' ',s)
            # print(s)
            f_in_old.write(s.strip())
            f_in_old.write('\n')

print("Finished!")
