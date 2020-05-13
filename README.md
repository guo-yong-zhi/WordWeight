# WordWeight
 一种计算文章中单词权重的方法
![](res/myAlg.png)  
***

该方法是在单词独立同分布假设下，对文本中的某单词（例如“Alice”）是来自一般的平均文本进行假设检验，得到概率分布，该分布是二项分布，近似成高斯分布可以计算出权重。该方法不需要“词袋”，对小文本库更友好。  
![](res/myAlg_desp.png)  
与之相应，tf-idf为：  
![](res/tfidf_desp.png)  
两者表现相近（小说《神们自己》）  
![](res/compare.png)  
