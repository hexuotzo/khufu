# encoding: utf-8
import random
from pinyin import hanzi2pinyin

def findindex(n,index):
    '''判断索引标号是否用过'''
    for i in index:
        if n<i+5 and n>i-5:
            return True
    return False

def addpinyin(text):
    ltext = list(text)
    textcount=len(text)
    pinyin = []#用过的拼音
    index = []#用过的索引
    pinyincount=int(textcount*0.5)#最小添加拼音的字数,1个字
    print textcount,pinyincount
    for i in range(pinyincount):
        j = random.randint(0,textcount-1)#随机抽取一个文字的索引
        if findindex(j,index):continue
        index.append(j)
        s = ltext[j]#随机抽取一个文字
        if s.strip()=="":continue
        if s.strip().isdigit():continue
        p = hanzi2pinyin(s)#获取这个字的拼音
        if p in pinyin:continue
        pinyin.append(p)#添加到已用拼音列表中
        news = "%s(%s)" % (s,hanzi2pinyin(s))
        ltext[j] = news
    return "".join(ltext)

if __name__ == '__main__':
    text=open("text1.txt").read().decode("utf8")
    print addpinyin(text)