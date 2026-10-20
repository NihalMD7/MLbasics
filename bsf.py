import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns

class Fillna:
    def missing(self,df):
        missing=df.isnull().sum()
        missing=missing(missing>0)
        missing=missing.sort_values(assending=False)
        return missing
    
    def fillmean(self,df,col):
        for i in col:
            df[i]=df[i].fillna(df[i].mean())
        return df[col]
    
    def fillmedian(self,df,col):
        for i in col:
            df[i]=df[i].fillna(df[i].median())
        return df[col]
    
    def fillmode(self,df,col):
        for i in col:
            df[i]=df[i].fillna(df[i].mode()[0])
        return df[col]

class plts:

    def corplot10(self,df,target):
        cor= df.corr()
        k=10
        largest=cor.nlargest(k,"targer")["target"].index
        cm=np.corcoef(df[largest].vlaues.T)
        heat=sns.heatmap(cm,yticklables=largest.values,xticklables=largest.values)
        return plt.show()
    

    



