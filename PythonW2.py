# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
a=range(1,10)
print(a)
def add_number(x,y):
    return x+y
add_number(100,19)
for number in a:
    print(number)

import pandas as pd
import numpy as np
animals = [ 'Tiger','Bear','Moose',1,2]
pd.Series(animals)
numbers = [1,2,None]
pd.Series(numbers)
np.nan == np.nan  # FALSE
np.isnan(np.nan) # TRue
sports={'Archery':"Bhutan", 'Golf':"Scotland","Sumo":"Japan",'Taekwondo':'South Korea'}
s=pd.Series(sports)
print(s.index)
s1=pd.Series(sports,index=["Golf",'Sumo',"Cricket"])
print(s1)