import difflib

# d=difflib.Differ()
import numpy as np
## 比较生成训练数据左右两部分键码和单词不一致比例
s="it"
file_path="/Users/ff/Desktop/train_data/"+s+"/"+s+"_user_web_train/train_data_it_user_web_no_emoji_letters/train_data"
with open(file_path,'r',encoding='utf-8') as f_in:
    id=0
    count=0
    for line in f_in:
        alls=line.split('|#|')
        lefts=alls[0]
        rights=alls[1].lower()
        lefts=lefts.replace('\t','|#|')
        lefts=lefts.replace(' ','')
        letters=lefts.split('|#|')
        words=rights.split('\t')
        # diff_index = np.array(list(a)) != np.array(list(b))
        if len(words)==len(letters):
            for i in range(0,len(words)):
                count+=1
                if words[i].lower() != letters[i]:
                    # print("none")
                    id+=1
        else:
            print(words,letters)
            print("split error")
        # print(list(diff))

        # print ('\n'.join(list(diff)))
    print("false error",float(id/count))
print("Finish Line")