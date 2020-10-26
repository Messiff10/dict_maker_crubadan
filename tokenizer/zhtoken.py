#coding=utf-8
'''
Created on 2014-3-19
测试结巴中文分词工具
@author: liTC
'''
import jieba
import jieba.posseg as pseg
import time
# t1=time.time()
f=open("/Users/ff/Desktop/maps/mark/zh_20200420.txt","r",encoding='utf-8')#读取文本
f_out=open("/Users/ff/Desktop/maps/mark/zh_20200420_.txt","w",encoding='utf-8')
for string in f:
     if string.strip() is not "":
     # string=f.read().decode("utf-8")
     # string='祖籍浙江省温州市，1975年2月28日出生于浙江温州，歌手。1987年考上浙江温州清县小百花越剧团，在团里唱小生。'
          words = pseg.cut(string)#进行分词
          result=""  #记录最终结果的变量
          for w in words:
               result+= str(w.word)+" " #加词性标注
          # print(result)
           #将结果保存到另一个文档中
          f_out.write(result.strip())
          f_out.write('\n')
          # f.close()
     # t2=time.time()
     # print("分词及词性标注完成，耗时："+str(t2-t1)+"秒。") #反馈结果

