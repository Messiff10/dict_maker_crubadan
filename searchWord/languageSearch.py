"""
筛选相关语言的语句
"""
import re
import sys

no_Character = re.compile(r"[a-zA-Z]+")
korean_path = sys.argv[1]
with open(korean_path, 'r', encoding='utf-8') as f_io:
    with open(korean_path.replace('.txt', '.search'), 'w', encoding='utf-8') as f_out:
        for line in f_io:
            result = re.findall(no_Character, line)
            # print(result)
            if len(result) > 1:
                f_out.write(line.strip())
                f_out.write('\n')

print("Finish Line")
