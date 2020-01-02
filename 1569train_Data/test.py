import re
## 筛选韩语
regex2=re.compile('r[\0x3100\-\0x31BF\s]+')
regex=re.compile('')
s="ㅂㄷㅈㄱㅃㄸㅉㄲㅍㅌㅊㅋㅅㅎㅆㅁㄴㅇㄹㅣㅔㅚㅐㅏㅗㅜㅓㅡㅢㅖㅒㅑㅛㅠㅕㅟㅞㅙㅘㅝ"
alist = [ch for ch in s]
chInt=0
for w in alist:
    chInt=ord(w)
    if chInt>=12592 and chInt<=12735 or chInt >=44032 and chInt<=55203:
        print(w)