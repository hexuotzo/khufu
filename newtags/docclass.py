#encoding: utf-8
from ngram import ngram

def getwords(doc):
    menus = [
        "备孕","怀孕","产后",
        "发烧","胎教","母胎",
        "疾病","营养","护理",
        "疾病","孕妇","孕妈"
    ]
    tg = ngram(menus,min_sim=0.0)
    words = tg.getSimilarStrings(doc.encode("utf8")).keys()
    return dict([(w,1) for w in words])

class classifier(object):
    """docstring for classifier"""
    def __init__(self, getfeatures,filename=None):
        self.fc = {}
        self.cc = {}
        self.getfeatures = getfeatures
        self.filename = filename
    def incf(self,f,cat):
        '''增加对特征/分类组合的计数值'''
        self.fc.setdefault(f,{})
        self.fc[f].setdefault(cat,0)
        self.fc[f][cat]+=1
    def incc(self,cat):
        '''增加对特征/分类组合的计数值'''
        self.cc.setdefault(cat,0)
        self.cc[cat]+=1
    def fcount(self,f,cat):
        """某一特征出现于某一分类中的次数"""
        if f in self.fc and cat in self.fc[f]:
            return float(self.fc[f][cat])
        return 0.0
    def catcount(self,cat):
        """属于某一分类内容项的数量"""
        if cat in self.cc:
            return float(self.cc[cat])
        return 0.0
    def totalcount(self):
        """所有内容项数量"""
        return sum(self.cc.values())
    def categories(self):
        """所有分类的列表"""
        return self.cc.keys()
    def train(self,item,cat):
        """训练,针对分类为每个特征增加计数值"""
        features = self.getfeatures(item)
        for f in features:
            self.incf(f,cat)
        self.incc(cat)
    def fprob(self,f,cat):
        """计算单词在分类中出现的概率"""
        if self.catcount(cat)==0:return 0
        return self.fcount(f,cat)/self.catcount(cat)

def simpletrain(cat):
    c1 = docclass.classifier(docclass.getwords)
    try:
        os.stat('results.pickle')
        c1 = pickle.load(open('results.pickle'))
    except:
        f = open('results.pickle','w')
        #训练备孕
        for r in open('beiyun.train'):
            r = r.strip()
            obj = mc.get(r)
            if obj==None:continue
            obj = loads(obj)
            print obj['title']
            c1.train(obj['body'],cat)
        pickle.dump(c1,f)
    return c1
if __name__ == '__main__':
    import memcache
    import docclass
    import cPickle as pickle
    import os
    from simplejson import dumps,loads

    mc = memcache.Client(['boypark.cn:11211'])
    c1 = simpletrain('备孕')
    print c1.fcount('高血压','备孕')
    print c1.fprob('高血压','备孕')
    
    