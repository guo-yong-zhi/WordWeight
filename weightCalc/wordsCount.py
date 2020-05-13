# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 12:17:22 2017

@author: momos
"""
import re
import pandas as pd
DataFrame = pd.DataFrame
rc = re.compile(r"(?<=\w)['’]\w+|\w+")#('\w+')#r"\w[\w']+"#r"[\w']\w+"

def countWords(textfiles=None, sort=False, textStr=None):
    """
    textfiles:list of flies or flienames, 
        or a single flie or a single name
    textStr:a str. Only one of textfiles and textStr should be None.
    """

    words_count={}
    def count_text(t):
        for word in rc.findall(t):
            k = word.replace("’","'")
            words_count[k] = words_count.get(k,0)+1
            
    if textStr:
        count_text(textStr)
    elif textfiles:
        import types
        if not isinstance(textfiles, (list,types.GeneratorType)):
            textfiles = [textfiles]

        for textfile in textfiles:
            if isinstance(textfile,str):
                text = open(textfile,encoding='utf-8')
            else:
                text = textfile
                
            for line in text:
                count_text(line)
         
    if not sort:
        return words_count
    else:
        kvp = list(words_count.items())
        kvp.sort(key=lambda x:-x[-1])
        return words_count, kvp
        
def calc_Sum_Fre(kvPairList):
    df = DataFrame(kvPairList)
    s = df[1].sum()
    df[1]/=s
    return s,df
def df2dict(df):
    return {k:v for _,(k,v) in df.iterrows()}