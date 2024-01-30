# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 12:39:13 2024

@author: DedricksMorake
"""

import pandas

#file = pandas.read_csv('insurance_data.csv', header=[4])

file = pandas.read_csv('insurance_data.csv', skiprows=5)

print(file)

print(file.info())

"""
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 63 entries, 0 to 62
Data columns (total 2 columns):
 #   Column  Non-Null Count  Dtype  
---  ------  --------------  -----  
 0   X       63 non-null     int64  
 1   Y       63 non-null     float64
dtypes: float64(1), int64(1)
memory usage: 1.1 KB
"""

print(file.describe())

"""
 X           Y
count   63.000000   63.000000
mean    22.904762   98.187302
std     23.351946   87.327553
min      0.000000    0.000000
25%      7.500000   38.850000
50%     14.000000   73.400000
75%     29.000000  140.000000
max    124.000000  422.200000
"""