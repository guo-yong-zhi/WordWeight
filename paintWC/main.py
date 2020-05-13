# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 20:03:40 2017

@author: momos
"""
import sys
sys.path.append("..")

import weightCalc.wordsCount as wc

import shelve

glFre_dat = "glFre_dat"
glFreList = None
glFreDic = None
sf = shelve.open(glFre_dat)
if not ("glFreList" in sf and "glFreDic" in sf):
    import weightCalc.globalFre as gl
    glFreList = gl.glFreList2
    glFreDic = gl.glFreDic2
    sf["glFreList"] = glFreList
    sf["glFreDic"] = glFreDic
else:
    glFreList = sf["glFreList"]
    glFreDic = sf["glFreDic"]
sf.close()

idf_dat = "idf_dat"
sf = shelve.open(idf_dat)
if not ("idf_wc" in sf and "idf_fn" in sf):
    import idf_count
    idf_wc = idf_count.wc
    idf_fn = idf_count.fn
    sf["idf_wc"] = idf_wc
    sf["idf_fn"] = idf_fn
else:
    idf_wc = sf["idf_wc"]
    idf_fn = sf["idf_fn"]
sf.close()

import pandas as pd
glFreDic = {k:v for i,k,v in glFreList[:50000].itertuples()}
idf_df = pd.DataFrame([*idf_wc.items(),])  
idf_wc = dict(idf_df.nlargest(50000, 1).values)
  
textflie = r"The Gods Themselves - Isaac Asimov.txt"
#r"The Gods Themselves - Isaac Asimov.txt"
#'Alice.txt'

wordsCountDic,wordsCount = wc.countWords(textflie, sort=True)
n_all,freList = wc.calc_Sum_Fre(wordsCount)



import scipy as sp
import numpy as np
from scipy.stats import norm
norm_cdf = norm.cdf

err_uncover_prob = min(glFreDic.values())
weight1=[]
weight2=[]

for _,(k,p) in freList.iterrows():
    g_p = glFreDic.get(k,err_uncover_prob)
    w1 = (p-g_p)/np.sqrt(g_p*(1-g_p)/n_all)

    w2 = np.log(idf_fn/idf_wc.get(k,1)) * p

    weight1.append(w1)
    weight2.append(w2)
    
#x = np.array(xlist)
#unusualProb = norm_cdf(x)
#freList['unusual']=unusualProb
freList["weight1"]=weight1
freList["weight2"]=weight2
freList["coverd"]=freList[0].isin(glFreDic)
freList["count"]=freList[0].apply(wordsCountDic.get)
kwDict = {k:p for _,(k,p) in freList[[0,"weight1"]].iterrows() if p>0}
kwDict2 = {k:p for _,(k,p) in freList[[0,"weight2"]].iterrows() if p>0}
import matplotlib.pyplot as plt   
from wordcloud import WordCloud
wc = WordCloud(background_color="white", max_words=2000, stopwords={})
wc.generate_from_frequencies(kwDict)
wc.to_file("myAlg.png")
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.show()
wc2 = WordCloud(background_color="white", max_words=2000, stopwords={})
wc2.generate_from_frequencies(kwDict2)
wc2.to_file("tfidf.png")
plt.imshow(wc2, interpolation='bilinear')
plt.axis("off")
plt.show()

def top_1(n):
    return {k for _,(k,p) in freList.sort_values(
            "weight1",ascending=False)[:n][[0,"weight1"]].iterrows()}
def top_2(n):
    return {k for _,(k,p) in freList.sort_values(
        "weight2",ascending=False)[:n][[0,"weight2"]].iterrows()}

