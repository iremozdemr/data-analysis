import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# korelasyon variable'ların birbiriyle ilişkisini ölçer
# -1<korelasyon<+1
# -1'e yaklaştıkça ilişkinin şiddeti artar
# 0'a yakınsa korelasyon yoktur
# 1'e yaklaştıkça ilişkinin şiddeti artar
# korelasyon değeri pozitif ise bir variable'ın değeri arttıkça diğer variable'ın değeri azalır
# korelasyon değeri pozitif ise bir variable'ın değeri arttıkça diğer variable'ın değeri artar

pd.set_option("display.max_columns",None)
pd.set_option("display.width",500)
df = pd.read_csv("./breast_cancer.csv")
df.head()

# axis = 0 ise:
# satır silinir
# axis = 1 ise:
# sütun silinir

df = df.drop(df.columns[0],axis=1)
# 1. sütun silinir

length = len(df.columns)
df = df.drop(df.columns[length-1],axis=1)
# sonuncu sütun silinir

numeric_columns = [column for column in df.columns if df[column].dtype in ["int","float"]]

corr = df[numeric_columns].corr()
# korelasyon alma
corr = df[numeric_columns].corr().abs()
# negatif değerleri pozitife çevirme
mask = np.tril(np.ones(corr.shape), k=0).astype(bool)
corr.where(~mask, other=np.nan, inplace=True)
# matristeki alt üçgeni silme

delete_list = [column for column in corr.columns if any(corr[column] > 0.9)]

for column in corr.columns:
    if column in delete_list:
        corr = corr.drop(column, axis=1)
# yüksek korelasyonlu sütunlar silinir

sns.set(rc={"figure.figsize":(12,12)})
sns.heatmap(corr,cmap="RdBu")
plt.show()