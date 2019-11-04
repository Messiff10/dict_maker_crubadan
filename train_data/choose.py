import codecs
import os
## 筛选30词以上
import re

data_folder = '/Users/ff/Desktop/train_data/ru/outaaac_detok.txt'
regex = re.compile('\s+')
# line=" ha messo in commercio edizioni con località francesi ,  olandesi ,  spagnole ,  statunitensi  e messicane .  try  {  MNZ_RICH ( 'Bottom' )  ;  }  catch ( e )   {  }"
with codecs.open(data_folder, encoding='utf-8') as f:
    with codecs.open(data_folder.replace('.txt', '_more30.txt'), 'w', encoding='utf-8') as f2:
        # print(f2)
        for line in f:
            items = regex.split(line.strip())
            print("len:"+str(len(items)))
            if len(items) >= 30:
                print("line:"+line)
                f2.writelines(line)
print("Finished!")