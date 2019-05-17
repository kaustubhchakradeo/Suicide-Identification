#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 16 20:27:54 2019

@author: kaustubh
"""

import pandas as pd

data = pd.read_csv('master.csv')
print("Data Head \n",data.head())
print("\n Len of Data \n",len(data))
print("\n Shape of data \n",data.shape)
data.drop(['HDI for year', 'country-year','age'],axis=1,inplace=True )
print("Data after deletion",data.head())
data = data.dropna()
print("Data after removing NA",data.head())
data = data.replace(0,pd.np.nan)
data = data.dropna()
export_csv = data.to_csv(r'data.csv', header = True, index = None)


import matplotlib.pyplot as plt
datahead = data[0:1000]
x=datahead.sex
#y=datahead.generation
z=datahead.suicides_no
plt.scatter(x,z,color='r')
#plt.scatter(y,z,color='g')
plt.xlabel('Sex and Generation')
plt.ylabel('Suicide Rate')
plt.clf()
print("Correlation",data.corr())

import seaborn as sns
plt.figure(figsize=(10,10))
sns_plot = sns.heatmap(data.corr(),cmap='coolwarm',linewidth=1,annot=True,annot_kws={"size": 9}, label='big')
fig = sns_plot.get_figure()
fig.savefig("HeatMap")
plt.clf()

sns.countplot(data.generation,hue=data.sex)
pop=plt.title('Generation hue Gender Counter')
plt.show()
fig = pop.get_figure()
fig.savefig('Generation VS Sex')
plt.clf()

f=plt.subplots(1,figsize=(18,8))
pie = data['generation'].value_counts().plot.pie(explode=[0.1,0.1,0.1,0.1,0.1,0.1],autopct='%1.1f%%',shadow=True)
fig = pie.get_figure()
fig.savefig('Pie Chart')
plt.clf()

plt.figure(figsize=(15,8))
pp = sns.stripplot(x='year',y='suicides/100k pop',data=data)
#plt.xticks(rotation=45)
plt.show()
fig = pp.get_figure()
fig.savefig('Year Vs Suicides')
plt.clf()

suicides_no=[]
for country in data.country.unique():
     suicides_no.append(sum(data[data['country']==country].suicides_no))   

suicides_no = pd.DataFrame(suicides_no,columns=['suicides_no'])
country = pd.DataFrame(data.country.unique(),columns=['country'])
data_suicide_country = pd.concat([suicides_no,country],axis=1)
data_suicide_country = data_suicide_country.sort_values(by='suicides_no',ascending = False)
rank = sns.barplot(y=data_suicide_country.country[:25],x=data_suicide_country.suicides_no[:25])
plt.show()
fig = rank.get_figure()
fig.savefig('Rank')


