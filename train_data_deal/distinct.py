import os
import re

# from utils.reExpression import replace_brackets, replace_clock_time, replace_quotes
import sys

centence = set()
file_path = "/Users/ff/Desktop/测评数据/去重/en_IN_test.txt"
with open(file_path, 'r', encoding='utf-8') as f_in:
    with open(file_path.replace('.txt', '.distinct'), 'w', encoding='utf-8') as f_out:
        for line in f_in:
            if line.strip() not in centence:
                centence.add(line.strip())
                f_out.write(line.strip())
                f_out.write('\n')
print("Finsh line")
