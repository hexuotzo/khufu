# encoding: utf-8
import random
from pinyin import hanzi2pinyin

def addpinyin(text):
    """docstring for addpinyin"""
    pass
    textcount=len(text)
    replace_dict={}
    pinyincount=5#最小添加拼音的字数,1个字
    for i in range(pinyincount):
        s = random.choice(text)#要替换的文字
        if s.strip()=="":continue
        news = "%s(%s)" % (s,hanzi2pinyin(s))
        replace_dict[s]=news
    for k,v in replace_dict.items():
        text=text.replace(k,v)
    return text

if __name__ == '__main__':
    text=open("text1.txt").read().decode("utf8")
    print addpinyin(text)