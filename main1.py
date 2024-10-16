#genel resim
#kategorik değişken analizi (analysis of categorical variables)
#sayısal değişken analizi (analysis of numerical variables)
#hedef değişken analizi (analysis of target variable)
#korelasyon analizi (analysis of correlation)

import pandas as pd
import seaborn as sns

pd.set_option("display.max_columns",None)
pd.set_option("display.width",500)

df1 = sns.load_dataset("titanic")
df1.head()

df2 = sns.load_dataset("tips")
df2.head()

df3 = sns.load_dataset("flights")
df3.head()

def check_df(dataframe,head=5):
    print("#################### shape ####################")
    print(dataframe.shape)
    print("#################### types ####################")
    print(dataframe.dtypes)
    print("#################### head ####################")
    print(dataframe.head(head))
    print("#################### tail ####################")
    print(dataframe.tail(head))
    print("#################### is null (NA) ####################")
    print(dataframe.isnull().sum())
    print("#################### describe ####################")
    print(dataframe.describe())

check_df(df1)
check_df(df2)
check_df(df3)