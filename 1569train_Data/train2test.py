train_date="/Users/ff/Desktop/测评数据/训练数据转测评格式/train_data"
with open(train_date,'r',encoding='utf-8') as f_in:
    with open(train_date.replace(train_date,train_date+'_original'),'w',encoding='utf-8') as f_out:
        for line in f_in:
            words=line.split('|#|')
            sencentes=words[1]
            sencentes=words[1].replace('\t',' ')
            f_out.write(sencentes.strip())
            f_out.write('\n')
print("Finish Line")