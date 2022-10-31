# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 11:58:36 2022

@author: lr22aak
"""
import pandas as pd
import clean_up as cl

with open('C:/Users/lr22aak/OneDrive - University of Hertfordshire/ads1/31_10/big_data.txt', 'r') as text:
    all_words = []
    counter = 0
    for line in text:
        words = line.split()
        counter += 1
    # print(counter)
        for word in words:
            word = cl.clean(word)
            all_words.append(word)
            
# print("all words: ", all_words)

# print("all words: ", len(all_words))

df_words = pd.DataFrame(data = all_words, columns = ('words', ))

count_words = df_words['words'].value_counts()

# print(count_words)

# help(pd.DataFrame())

print(df_words['words'][100])