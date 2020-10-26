import re
"""
爬取词典处理
"""
file_in = "/Users/ff/Desktop/第一优先级语言词表/desc/dictionary_crawl/de_dict_uniq.txt"
file_out = "/Users/ff/Desktop/第一优先级语言词表/desc/dictionary_crawl/de_dict_uniq_.txt"
result = set()
with open(file_in, 'r', encoding='utf-8') as f_in:
    with open(file_out, 'w', encoding='utf-8') as f_out:
        for lin in f_in:
            lin = re.sub('[^\w+]', '', lin)
            if lin.strip() not in result:
                result.add(lin.strip())
                print(lin.strip())
                f_out.write(lin.strip())
                f_out.write('\n')
print("finish")
