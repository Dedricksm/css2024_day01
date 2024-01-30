# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 12:29:25 2024

@author: DedricksMorake
"""

import pandas

column_names = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N"]

file = pandas.read_csv('housing_data.csv',names = column_names)

print(file)

print(file.info())

"""
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 506 entries, 0 to 505
Data columns (total 14 columns):
 #   Column  Non-Null Count  Dtype  
---  ------  --------------  -----  
 0   A       506 non-null    float64
 1   B       506 non-null    float64
 2   C       506 non-null    float64
 3   D       506 non-null    float64
 4   E       506 non-null    float64
 5   F       506 non-null    float64
 6   G       506 non-null    float64
 7   H       506 non-null    float64
 8   I       506 non-null    int64  
 9   J       506 non-null    float64
 10  K       506 non-null    float64
 11  L       506 non-null    float64
 12  M       506 non-null    float64
 13  N       452 non-null    float64
dtypes: float64(13), int64(1)
memory usage: 55.5 KB
"""

print(file.describe())

"""
                A           B           C  ...           L           M           N
count  506.000000  506.000000  506.000000  ...  506.000000  506.000000  452.000000
mean     1.269195   13.295257    9.205158  ...  332.791107   11.537806   23.750442
std      2.399207   23.048697    7.169630  ...  125.322456    6.064932    8.808602
min      0.000000    0.000000    0.000000  ...    0.320000    1.730000    6.300000
25%      0.049443    0.000000    3.440000  ...  364.995000    6.877500   18.500000
50%      0.144655    0.000000    6.960000  ...  390.660000   10.380000   21.950000
75%      0.819623   18.100000   18.100000  ...  395.615000   15.015000   26.600000
max      9.966540  100.000000   27.740000  ...  396.900000   34.410000   50.000000
"""