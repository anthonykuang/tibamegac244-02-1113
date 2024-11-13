import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import missingno as msno

df = pd.read_csv('Planilha sem ttulo - cscpopendata.csv', encoding='ISO-8859-1')
print("df.head():",df.head(),"\n")
print("df.describe().transpose:",df.describe().transpose(),"\n")
print("df.info():",df.info(),"\n")
print("df.shape:",df.shape,"\n")
print("df.isnull().sum():",df.isnull().sum(),"\n")
print("df.select_dtypes(include=['int64']).columns:",df.select_dtypes(include=['int64']).columns,"\n")
print("df.select_dtypes(include=['object']).columns:",df.select_dtypes(include=['object']).columns,"\n")
print("df.drop_duplicates():",df.drop_duplicates(),"\n")

# df = df.dropna()#刪除缺失值             
print(df.isnull().sum(),"\n")

#將 ChemicalCount 小於5和大於等於5的產品進行分類，並按化學成分數量排序
below_five = df[df["ChemicalCount"] < 5]
above_five = df[df["ChemicalCount"] >= 5]
sorted_df = above_five.sort_values(by='ChemicalCount', ascending=False)

plt.barh(sorted_df['ProductName'], sorted_df['ChemicalCount'])
plt.xlabel("Number of Chemicals used")
plt.title("Cosmetic Products with 5 or more toxic chemicals")
plt.show()