import codecs
import os
"""
筛选30词以上
"""
import re
import sys
import textwrap

data_folder = sys.argv[1]
data_folder_out = sys.argv[2]
num=sys.argv[3]
regex = re.compile('\s+')

# line=" ha messo in commercio edizioni con località francesi ,  olandesi ,  spagnole ,  statunitensi  e messicane .  try  {  MNZ_RICH ( 'Bottom' )  ;  }  catch ( e )   {  }"
with open(data_folder, 'r', encoding='utf-8') as f:
    with open(data_folder_out, 'w', encoding='utf-8') as f2:
        # print(f2)
        for line in f:
            # print(line)
            items = regex.split(line.strip())
            lineresult = ""
            for i in range(len(items)):
                # print(i%10)
                # print(items[i], end=' ')
                # lineresult+=items[i]+" "
                f2.write((items[i] + ' '))
                if (i + 1) % int(num) == 0:
                    # print("\n")
                    # lineresult+='\n'
                    f2.write('\n')
print("\nFinish line")
