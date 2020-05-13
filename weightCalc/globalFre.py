# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 13:54:35 2017

@author: momos
"""
import os
from . import wordsCount as wc

txtPath = r".\2553\txt"

def countAll(txtPath,**kw):
    filenames = (os.path.join(path,file)
                    for path,dire,files in os.walk(txtPath) 
                    for file in files)
    return wc.countWords(filenames,**kw)

#glDic,glList = countAll(txtPath,sort=True)
#glSize,glFreListA = wc.calc_Sum_Fre(glList)
#glFreList = glFreListA#[:10000]
#glFreDic = wc.df2dict(glFreList)

txtPath2 = r"..\BNC\2554\txt"
glDic2,glList2 = countAll(txtPath2, sort=True)
glSize2,glFreListA2 = wc.calc_Sum_Fre(glList2)
glFreList2 = glFreListA2
glFreDic2 = wc.df2dict(glFreList2)