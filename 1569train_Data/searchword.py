import re

search_path = "/Users/ff/Desktop/第一优先级语言词表/desc/wy筛选词表/es_US_dict.txt"
regex = re.compile('\w+,\s+\w')
unigram=set()
with open(search_path, 'r', encoding='utf-8') as f_in:
    with open(search_path.replace('.txt', '_search2'), 'w', encoding='utf-8') as f_out:
        for line in f_in:
            if re.search(regex, line) is not None:
                if line.strip() not in unigram:
                    print(line.strip())
                    f_out.write(line.strip())
                    f_out.write('\n')
print("Finish Line")
