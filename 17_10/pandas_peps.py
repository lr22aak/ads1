# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 11:33:01 2022

@author: lr22aak
"""
# import numpy as np
import pandas as pd

df_countries = pd.read_csv('C:/Users/lr22aak/Desktop/countries_top10 .csv')

# print(df.to_string()) 

# df_countries = pd.DataFrame(data=df,columns=("Country", "Population", "Area", "GDP"))
# df_gdp = pd.DataFrame(data=df.to_string,columns=("Country", "Population", "Area", "GDP", "GDP per Head"))

df_countries["GDP per head"] = df_countries["GDP"] / df_countries["Population"]

df_countries["Population per square km"] = df_countries["Population"] / df_countries["Area"]

print(df_countries)