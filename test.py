import re
pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
line = "https://www.facebook.com/groups/637252586617595/permalink/904122223263962/ minutes          posted	posted " \
       "https://www.facebook.com/groups/637252586617595/permalink/904122223263962/ minutes	posted	posted"
print(line)
line = re.sub(pattern, "", line)
print(line)
words = line.split('\\s')
print()




print(re.match('www', 'www.runoob.com'))  # 在起始位置匹配
print(re.match('www', 'www.runoob.com').span())  # 在起始位置匹配
print(re.match('com', 'www.runoob.com'))         # 不在起始位置匹配

pattern = re.compile('(.*) are (.*?) (.*)')
pattern = re.compile('(.*) are (.*?) .*')
line = "Cats are smarter than dogs"

matchObj = re.match(pattern, line)

if matchObj:
       print("matchObj.group() : ", matchObj.group())
       print("matchObj.group(1) : ", matchObj.group(1))
       print("matchObj.group(2) : ", matchObj.group(2))
       # print("matchObj.group(3) : ", matchObj.group(3))
       print("matchObj.groups : ", matchObj.groups())
else:
       print("No match!!")


def double(matched):
       value = int(matched.group('value'))
       print(matched)
       print(value)
       return str(value * 2)


s = 'A23G4HFD567'
print(re.sub('(?P<value>\d+)', double, s))



print(re.split('\W+', ' runoob, runoob, runoob.'))
print(re.split('(\W+)', ' runoob, runoob, runoob.'))



#写一个正则表达式，能匹配出多种格式的电话号码，包括：
text = "(021)88776543 010-55667890 02584533622 057184720483 837922740"
text = "grace.guo@kikatech.com2740ddd445677777ffggrace_guor@163.com"
text = "комиссии414949911"
# text = "grace_guor@163.com"
# m = re.findall(r"[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}", text)
m = re.findall(r'[0-9a-zA-Z_]{0,19}@[0-9a-zA-Z]{1,13}\.[com,cn,net]{1,3}', text)
m = re.search(r'[0-9a-zA-Z_]{0,19}@[0-9a-zA-Z]{1,13}\.[com,cn,net]{1,3}', text)
m = re.search("[а-яА-Я .-]{1,}", text)
if m:
    print(m)
else:
    print('not match')



def checkPassword(password):
    passwordReg = re.compile(r'''
        (?=^.{8,}$)     # 八位数及以上
        ((?=.*\d+))     # 至少一位数字
        (?![.\n])       # 没有换行符
        (?=.*[A-Z])     # 大写任意个
        (?=.*[a-z]).*$  # 小写任意个
    ''', re.VERBOSE)

    passwordReg = re.compile(r'''
            (?=^.{8,}$)     # 八位数及以上
            (?=.*\d+)     # 至少一位数字
            (?![.\n])       # 没有换行符
            (?=.*[A-Za-z]).*$  # 小写任意个
        ''', re.VERBOSE)

    match = passwordReg.match(password)
    return match is not None


print(checkPassword('A'))  # False
print(checkPassword('a'))  # False
print(checkPassword('1'))  # False
print(checkPassword('Aa'))  # False
print(checkPassword('A1'))  # False
print(checkPassword('a1'))  # False
print(checkPassword('Aa1'))  # False
print(checkPassword('Aa12345'))  # False
print(checkPassword('AaBbCcDd'))  # False
print(checkPassword('ABCD1234'))  # False
print(checkPassword('abcd1234'))  # False
print(checkPassword('Aa123456  ckjfk'))  # True
print(checkPassword('aa123456dfdfd  ckjfk'))  # True
print(checkPassword('a12adfdfd12  ckjfk'))  # True
print(checkPassword('aadfdfd12  ckjfk'))  # True

from itertools import *

print('Stop at 5:')
for i in islice(range(100), 5):
    print(i, end=' this is end ')
print('\n')


a = ["1", "3"]
b = ["2", "4"]
print("".join(a))
c = a + b
print(c)

for i in range(5-1, 2, -1):
    print(i)

try:
    if xy:
        print("ddddd")
except:
    print("hhhhh")
print()


ss= ["dd", "db", "dd"]
print(ss)
if "dd" in ss:
    ss.remove("dd")
print(ss)

s1 = {1, 3}
s2 = {4}
s1 = s1.union(s2)
print(s1)
s1.add(4)

a = [1, 2]
b = [3, 5]
c = [x/y for x, y in zip(a, b)]
print(c)
print(1/3)
