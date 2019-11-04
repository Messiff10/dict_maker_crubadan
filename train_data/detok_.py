import codecs
import os
from utils.reExpression import replace_quotes, replace_clock_time, replace_brackets
import re
##  去中括号
data_folder = '/Users/ff/Desktop/train_data/ms_MY/ms_MY_web.txt'
# line=" ha messo in commercio edizioni con località francesi ,  olandesi ,  spagnole ,  statunitensi  e messicane .  try  {  MNZ_RICH ( 'Bottom' )  ;  }  catch ( e )   {  }"
with codecs.open(data_folder, encoding='utf-8') as f:
    with codecs.open(data_folder.replace('.txt', '_script.txt'), 'w', encoding='utf-8') as f2:
        # print(f2)
        for line in f:
            line = re.sub("\\[.*?]", "", line)
            # line.replaceAll("\\{.*?}", "")
            f2.writelines(line)
print("Finished!")



