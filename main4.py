import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option("display.max_columns",None)
pd.set_option("display.width",500)
df = sns.load_dataset("titanic")
df.head()

for column in df.columns:
    if df[column].dtype == "bool":
        df[column] = df[column].astype(int)

types = [df[column].dtype for column in df.columns]

def categorize_columns(dataframe):
    categorical_columns = []
    numerical_columns = []

    for column in dataframe.columns:
        if dataframe[column].dtype in ["int","float"] and dataframe[column].nunique() > 20:
            numerical_columns.append(column)
        if dataframe[column].dtype in ["int","float"] and dataframe[column].nunique() <= 20:
            categorical_columns.append(column)
        if dataframe[column].dtype in ["category","object","bool"] and dataframe[column].nunique() > 20:
            numerical_columns.append(column)
        if dataframe[column].dtype in ["category","object","bool"] and dataframe[column].nunique() < 20:
            categorical_columns.append(column)

    return categorical_columns,numerical_columns

def analysis_by_target_variable(dataframe, target):
    for column in dataframe.columns:
        print("###########################")
        if column != target:
            print(df.groupby(df[column])[target].mean())
        print("###########################")

categorical_columns,numerical_columns = categorize_columns(df)
analysis_by_target_variable(df,"survived")