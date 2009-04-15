from ngram import ngram

def getwords(doc):
    tg = ngram(menus,min_sim=0.0)
    words = tg.getSimilarStrings(smart_str(obj["title"],"utf8")).keys()
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