# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 10:25:27 2017

@author: momos
"""

import re
import pandas as pd
DataFrame = pd.DataFrame
rc = re.compile(r"(?<=\w)['’]\w+|\w+")#('\w+')#r"\w[\w']+"#r"[\w']\w+"

def count_idf(textfiles, sort=False):
    """
    textfiles:list of flies or flienames, 
        or a single flie or a single name 
    """
    import types
    if not isinstance(textfiles, (list,types.GeneratorType)):
        textfiles = [textfiles]
        
    words_count = {}
    file_num = 0
    for textfile in textfiles:
        file_num += 1
        if isinstance(textfile,str):
            textStr = open(textfile,encoding='utf-8').read()
            wordSet = {word.replace("’","'") for word in set(rc.findall(textStr))}
            for w in wordSet:
                words_count[w] = words_count.get(w,0)+1
    return words_count, file_num

import os
txtPath = r".\2554\txt"
def countAll(txtPath,**kw):
    filenames = (os.path.join(path,file)
                    for path,dire,files in os.walk(txtPath) 
                    for file in files)
    return count_idf(filenames,**kw)

wc,fn = countAll(txtPath)