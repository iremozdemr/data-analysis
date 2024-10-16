#kategorik değişkenler:
#bool
#object
#category

#kardinalitesi yüksek değişkenler:
#fazla sınıfa sahip değişkenler

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option("display.max_columns",None)
pd.set_option("display.width",500)
df = sns.load_dataset("titanic")
df.head()

types1 = ["category","object","bool"]
columns1 = [column for column in df.columns if str(df[column].dtypes) in types1]
#kategorik değişkenler

types2 = ["int","float"]
columns2 = [column for column in df.columns if df[column].nunique() <= 3 and df[column].dtypes in types2]
#sayısal olarak gösterilen kategorik değişkenler

types3 = ["category","object","bool"]
columns3 = [column for column in df.columns if str(df[column].dtypes) in types3 and df[column].nunique() > 20]
#kategorik olarak gösterilen sayısal değişkenler

categorical_variables = columns1 + columns2
categorical_variables = [column for column in categorical_variables if column not in columns3]

df[categorical_variables]

def categorical_summary(dataframe):
    i = 1
    for column in categorical_variables:
        print("###########################")
        new_df = pd.DataFrame(
            {
                column: dataframe[column].value_counts(),
                "ratio": 100 * dataframe[column].value_counts() / len(dataframe)
            }
        )
        print(new_df)
        print("###########################")
        plt.subplot(5,3, i)
        sns.countplot(x=dataframe[column])
        i = i+1
    plt.show()

categorical_summary(df)