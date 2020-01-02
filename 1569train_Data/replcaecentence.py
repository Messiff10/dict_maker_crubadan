
## 替换单词
file_path="/Users/ff/Desktop/测评数据/替换句子/it_user_web_case.txt"
with open(file_path,'r',encoding='utf-8') as f_in:
    with open(file_path.replace('.txt','.replace'),'w',encoding='utf-8') as f_out:
        for line in f_in:
            line=line.replace('p . domanda p . intertitolo','').replace(' . try catch','')
            f_out.write(line.strip())
            f_out.write('\n')
print("Finish Line")