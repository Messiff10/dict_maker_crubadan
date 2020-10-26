import re

file = "/Users/ff/Downloads/es_SA.txt"
file_out = "/Users/ff/Downloads/es_SA_choose.txt"
result = []
regex = re.compile('\s+')
with open(file, 'r', encoding='utf-8') as f_in:
    with open(file_out, 'w', encoding='utf-8') as f_out:
        for l in f_in:
            word = l.strip().split('\t')[0]
            words = regex.split(word.strip())
            for w in words:
                if w not in result:
                    result.append(w)
                    f_out.write(w.strip())
                    f_out.write('\n')
        # for r in result:
        #     f_out.write(r.strip())
        #     f_out.write('\n')

