import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option("display.max_columns",None)
pd.set_option("display.width",500)
df = sns.load_dataset("titanic")
df.head()

variables1 = [column for column in df.columns if df[column].dtype in ["int","float"] and df[column].nunique() > 3]
variables2 = [column for column in df.columns if df[column].dtype in ["category","object","bool"] and df[column].nunique() > 20]

numeric_variables = variables1 + variables2

def numeric_summary(dataframe,column_name):
    print("###########################")
    print("name:" + column_name)
    print("nunique:" + str(df[column_name].nunique()))
    print(dataframe[column_name].describe())
    print("###########################")

for variable in numeric_variables:
    numeric_summary(df,variable)