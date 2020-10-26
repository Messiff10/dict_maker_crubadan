import re
import sys

file = sys.argv[1]
f_out = open(sys.argv[2], 'w', encoding='utf-8')
regex = re.compile('[^a-zA-Z0-9\'\s+]')
with open(file, 'r', encoding='utf-8') as f_in:
    for l in f_in:
        l = re.sub(regex, '\n', l)
        lsn = l.split('\n')
        for ls in lsn:
            if len(ls.strip()) > 1:
                f_out.write(l.strip())
                f_out.write('\n')
