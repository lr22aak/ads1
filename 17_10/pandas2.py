# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 12:21:53 2022

@author: lr22aak
"""
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('C:/Users/lr22aak/Desktop/GDP_2015dollars.xls')

# print(df.to_string())

print(df.iloc[41:-1])

plt.figure(dpi = 144)

plt.plot(df["Year"], df["China"], label= 'China')
plt.plot(df["Year"], df["Germany"], label= 'Germany')
plt.plot(df["Year"], df["Japan"], label= 'Japan')
plt.plot(df["Year"], df["United States"], label= 'United States')

plt.xlabel("country")
plt.ylabel("year")

plt.xlim(1970, 2020)

plt.legend()

plt.show()

plt.plot(df["Year"],(df["China"]/df["United States"])* 100, label= 'China')
plt.plot(df["Year"], (df["Germany"]/df["United States"]) * 100, label= 'Germany')
plt.plot(df["Year"], (df["Japan"]/df["United States"]) * 100, label= 'Japan')

plt.xlim(1970, 2020)

plt.title('% of GDP')

plt.legend()

plt.show()