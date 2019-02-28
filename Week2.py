# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

print("Hello Anaconda")
import pandas as pd
import numpy as np
#import timeit as timit
animals = [ 'Tiger','Bear','Moose',1,2]
pd.Series(animals)
numbers = [1,2,None]
pd.Series(numbers)
np.nan == np.nan  # FALSE
np.isnan(np.nan) # TRue

sports={'Archery':"Bhutan", 'Golf':"Scotland","Sumo":"Japan",'Taekwondo':'South Korea'}
s=pd.Series(sports)
print(s)
print(s.index)
s1=pd.Series(sports,index=["Golf",'Sumo',"Cricket"])
print(s.iloc[0],s[3],s.loc["Golf"])
#####################################################
s=pd.Series([100.0, 120.0,101.00,3,00])
s=pd.Series(np.random.normal(0,1,10000))
print(s)
#t=timeit.Timer
print(t.timeit(2))
total=0
for i in s:
    total=total+i
print(len(s),total,np.sum(s))
#print(t.timeit(3))
sports = {99: 'Bhutan',
          100: 'Scotland',
          101: 'Japan',
          102: 'South Korea'}
s = pd.Series(sports)
original_sports = pd.Series({'Archery': 'Bhutan',
                             'Golf': 'Scotland',
                             'Sumo': 'Japan',
                             'Taekwondo': 'South Korea'})
cricket_loving_countries = pd.Series(['Australia',
                                      'Barbados',
                                      'Pakistan',
                                      'England'], 
                                   index=['Cricket',
                                          'Cricket',
                                          'Cricket',
                                          'Cricket'])
all_countries = original_sports.append(cricket_loving_countries)
######################################################
# data frame
purchase_1 = pd.Series({'Name': 'Chris',
                        'Item Purchased': 'Dog Food',
                        'Cost': 22.50})
purchase_2 = pd.Series({'Name': 'Kevyn',
                        'Item Purchased': 'Kitty Litter',
                        'Cost': 2.50})
purchase_3 = pd.Series({'Name': 'Vinod',
                        'Item Purchased': 'Bird Seed',
                        'Cost': 5.00})
df = pd.DataFrame([purchase_1, purchase_2, purchase_3], index=['Store 1', 'Store 1', 'Store 2'])
df.head()
#######################################################
df=pd.read_csv('C:/Users/Owner/Documents/Python/olympics.csv')
len(df)
df=pd.read_csv('C:/Users/Owner/Documents/Python/olympics.csv', index_col = 0, skiprows=1)
#df.head()
#df.columns
for col in df.columns: 
    if col[:2]=='01':
        df.rename(columns={col:'Gold' + col[4:]}, inplace=True)
    if col[:2]=='02':
        df.rename(columns={col:'Silver' + col[4:]}, inplace=True)
    if col[:2]=='03':
        df.rename(columns={col:'Bronze' + col[4:]}, inplace=True)
    if col[:1]=='№':
        df.rename(columns={col:'#' + col[1:]}, inplace=True) 
df.drop('Totals')
names_ids = df.index.str.split('\s\(') # split the index by '('

df.index = names_ids.str[0] # the [0] element is the country name (new index) 
df['ID'] = names_ids.str[1].str[:3] # the [1] element is the abbreviation or ID (take first 3 characters from that)
df.head()
def answer_zero():
    return df.iloc[0]
answer_zero() 
df['Gold'].idxmax()
df['delta']=abs(df['Gold']-df['Gold.1'])
df['TotalGolds']=abs(df['Gold']+df['Gold.1'])
df['relativedelta']=((df['Gold']-df['Gold.1']))/(df['TotalGolds'])
df['delta'].idxmax()
df1=(df[(df['Gold']>0) & (df['Gold.1']>0)])
len(df)-len(df1)
df1.columns
df1['relativedelta'].idxmax()
df['Points']=df['Gold.2']*3+df['Silver.2']*2+df['Bronze.2']
s=pd.Series(df['Points'])
type(s)
#######################################################
df = pd.read_csv('C:/Users/Owner/Documents/Python/log.csv')
df
df = df.set_index('time')
df = df.sort_index()
df
df = df.reset_index()
df = df.set_index(['time', 'user'])

df = df.fillna(method='ffill')
df.head
#######################################################
census_df=pd.read_csv('C:/Users/Owner/Documents/Python/census.csv')
census_df.head()
len(census_df)
df0=census_df[census_df['COUNTY']>0]
len(df0)
df1=df0['STNAME']
ans=df1.mode().iloc[0]


df0=census_df[census_df['COUNTY']>0]
df9=df0.sort_values(['STNAME', 'CENSUS2010POP'],ascending=False)
df9[['STNAME','CENSUS2010POP']]

df9.columns
df10=df9[["REGION",'STNAME','CTYNAME','POPESTIMATE2014', 'POPESTIMATE2015']]
df11=df10[df10['CTYNAME'].str.startswith('Washington')]
df11['CTYNAME']


census_df['SUMLEV'].unique()
census_df['STATE'].unique()
census_df.mode()['STATE'][0]
census_df['STNAME'].groupby(lambda x: x).value_counts()
census_df1=census_df[census_df['SUMLEV]==50]




















