import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib
import plotly.express as px

df = pd.read_csv('/Users/yana/Desktop/Maths.csv')

df.columns
df.isnull().sum().sum()

print(df['G1'].describe())
print(df['G1'].median())

print(df['G2'].describe())
print(df['G2'].median())

print(df['G3'].describe())
print(df['G3'].median())

print(df['Dalc'].describe())
print(df['Dalc'].median())

print(df['Walc'].describe())
print(df['Walc'].median())

sns.set_palette('vlag')
df['G3'] = df['G3'].astype('int')
sns.lineplot(x="G3", 
             y="G1", 
             data=df)
print(df['G3'].corr(df['G1']))

df['G3'] = df['G3'].astype('int')
sns.lmplot(x="G3", 
             y="G2", 
             data=df)
print(df['G3'].corr(df['G2']))

df['change'] = df['G3'] - df['G1']

sns.barplot(data=df, 
            x="Dalc", 
            y="change", 
            hue="Dalc", 
            palette="vlag", 
            legend=False)
print(df['Dalc'].corr(df['change']))

sns.barplot(data=df, 
            x="Walc", 
            y="change", 
            hue="Walc", 
            palette="vlag", 
            legend=False)
print(df['Walc'].corr(df['change']))

df['avalc'] = (df['Dalc'] + df['Walc']) / 2

sns.jointplot(data=df, 
              x="avalc", 
              y="change", 
              hue="sex", 
              palette="Set1")

GP_df = df[(df['school'].str.contains('GP'))]

sns.displot(data=df, x="avalc", col="school", palette="Set1", hue="school", kde=True)

sns.barplot(GP_df, 
            x='romantic', 
            y='change', 
            hue='higher', 
            palette="Set1")

sns.lineplot(GP_df, x='avalc', 
             y='change', 
             hue='higher', 
             palette="Set1", 
             errorbar=None)
