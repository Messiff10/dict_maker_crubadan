import imageio as igo
import cv2
import numpy as np

"""
读取gif，将每一帧存储在pics数组中
将现有gif重新生成新的gif
"""

pics = igo.mimread('/Users/ff/Documents/0_1.gifDeal')
print(np.array(pics).shape)
A = []
# 允许出现的字符数
string = '~!@#$%^&*()_+-{}|":?><[]\;'
count = len(string)
# 对每一帧的图片进行处理
for img in pics:
    u, v, _ = img.shape
    c = img * 0 + 255
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    for i in range(0, u, 6):
        for j in range(0, v, 6):
            pix = gray[i, j]
            b, g, r, _ = img[i, j]
            zifu = string[int(((count - 1) * pix) / 256)]
            cv2.putText(c, zifu, (j, i), cv2.FONT_HERSHEY_COMPLEX, 0.2, (int(b), int(g), int(r), 1))
    # 色度处理的图片存储于数组
    A.append(c)
# 存储成新的gif
igo.mimsave('/Users/ff/Documents/0_2.gifDeal', A, 'GIF', duration=0.1)

