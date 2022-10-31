# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 11:58:36 2022

@author: lr22aak
"""
import pandas as pd
import clean_up as cl

with open('C:/Users/lr22aak/OneDrive - University of Hertfordshire/ads1/31_10/big_data.txt', 'r') as text:
    all_words = []
    all_letters = []
    counter = 0
    for line in text:
        words = line.split()
        counter += 1
    # print(counter)
        for word in words:
            word = cl.clean(word)
            letters = list(word)
            for l in letters:
                all_letters.append(l)
            all_words.append(word)
            
# print("all words: ", all_words)

# print("all words: ", len(all_words))

df_words = pd.DataFrame(data = all_words, columns = ('words', ))

count_words = df_words['words'].value_counts()

# print(count_words)

# help(pd.DataFrame())

# print(df_words['words'][100])

df_letters = pd.DataFrame(data = all_words, columns = ('letters', ))

count_words = df_letters['letters'].value_counts()


