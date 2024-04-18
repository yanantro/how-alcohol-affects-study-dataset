import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib
import plotly.express as px

df = pd.read_csv('/Users/yana/Desktop/Maths.csv')

df.isnull().sum().sum() #checking if dataframe has any NaN

#outputing some statistics
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

#the dependence of the final grade on the grades for the 1st and 2nd periods of study
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


df['change'] = df['G3'] - df['G1'] #difference between the first period grade and the last one by creating a new column
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

df['avalc'] = (df['Dalc'] + df['Walc']) / 2 #finding the average alcohol consumption by creating a new column

#relationship of school grades to the amount of alcohol consumed among males and females
sns.jointplot(data=df,
              x="avalc",
              y="change",
              hue="sex",
              palette="Set1")

#seeing in which school the alcohol consumption is higher
GP_df = df[(df['school'].str.contains('GP'))]
sns.displot(data=df, x="avalc", col="school", palette="Set1", hue="school", kde=True)

#checking if romantic relationships influence the grades of students who wants to pursue higher education in the future more than alcohol consumption
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

