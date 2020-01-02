import re

all_path="/Users/ff/Desktop/测评数据/筛选新闻/it_user_web_noemoji.txt"
user_path="/Users/ff/Desktop/测评数据/筛选新闻/it_web_script.txt"
user=set()
with open(user_path,'r',encoding='utf-8') as f_user:
    for linr in f_user:
        linr=re.sub('\s+',' ',linr.strip())
        user.add(linr.strip().lower())
with open(all_path,'r',encoding='utf-8') as f_in:
    with open(all_path.replace('.txt','_web'),'w',encoding='utf-8') as f_web:
        with open(all_path.replace('.txt', '_user'), 'w', encoding='utf-8') as f_u:
            for line in f_in:
                if line.strip().lower() not in user:
                    f_web.write(line.strip())
                    f_web.write('\n')
                else:
                    f_u.write(line.strip())
                    f_u.write('\n')
print("Finish line")


