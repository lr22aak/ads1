# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 11:27:12 2022

@author: lr22aak
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

bcyData = pd.read_csv('C:/Users/lr22aak/Desktop/BCS_ann.csv')
bpData = pd.read_csv('C:/Users/lr22aak/Desktop/BP_ann.csv')
tescoData = pd.read_csv('C:/Users/lr22aak/Desktop/TSCO_ann.csv')
VodaData = pd.read_csv('C:/Users/lr22aak/Desktop/VOD_ann.csv')

print(bpData)

def subPlots():
    # data = [bcyData, bpData, tescoData, VodaData]
    plt.figure()
    # adjust space between plots
    plt.subplots_adjust(hspace=0.4, wspace=0.4)
    # loop over list of samples
    
    plt.subplot(2, 2, 1) # subplot count starts at 1
    plt.xlim(1990, 2020)
    plt.plot(bcyData["year"], bcyData["ann_return"], label= 'Barclays')
    plt.legend()
    
    plt.subplot(2, 2, 2) # subplot count starts at 1
    plt.xlim(1990, 2020)
    plt.plot(bpData["year"], bpData["ann_return"], label= 'BP')
    plt.legend()
    
    plt.subplot(2, 2, 3)
    plt.xlim(1990, 2020)
    plt.plot(tescoData["year"], tescoData["ann_return"], label= 'Tesco')
    plt.legend()
    
    plt.subplot(2, 2, 4)
    plt.xlim(1990, 2020)
    plt.plot(VodaData["year"], VodaData["ann_return"], label= 'Vodaphone')
    plt.legend()
    # for i in range(4):
    #     plt.subplot(2, 2, i+1) # subplot count starts at 1
    #     plt.xlim(1990, 2020)
    #     # plt.ylim(-200, 200)
    #     plt.plot(data[i]["year"], data[i]["ann_return"])
    #     # plt.xlabel("Sample "+str(i+1))
    #     # plt.ylabel("N")
    #     plt.legend()
    plt.show()
    
def dispData():
    plt.figure()
    
    plt.plot(bcyData["year"], bcyData["price"], label= 'BCY Data')
    plt.plot(bpData["year"], bpData["price"], label= 'BP Data')
    plt.plot(tescoData["year"], tescoData["price"], label= 'Tesco Data')
    plt.plot(VodaData["year"], VodaData["price"], label= 'Vodaphone Data')
    
    plt.legend()
    
    plt.show()

def piePlot():
    mcm = np.array([33367, 68785, 20979, 29741])
    countries = ["Barclays", "BP", "Tesco", "Vodaphone"]
    ftse = 1814000
    mcm = mcm/ftse
    
    plt.figure()
    plt.pie(mcm, labels=countries, normalize=False)
    plt.title("Market capitalisation Mill. £")
    plt.show()
    
def histogramPlot():
    plt.figure()
    
    plt.subplots_adjust(hspace=0.4, wspace=0.4)

    plt.subplot(2, 2, 1)
    plt.hist(bcyData["ann_return"],density = True, label= 'Barclays')
    plt.legend()
    
    plt.subplot(2, 2, 2) # subplot count starts at 1
    plt.hist( bpData["ann_return"], label= 'BP')
    plt.legend()
    
    plt.subplot(2, 2, 3)
    plt.hist(tescoData["ann_return"], label= 'Tesco')
    plt.legend()
    
    plt.subplot(2, 2, 4)
    plt.hist(VodaData["ann_return"], label= 'Vodaphone')
    plt.legend()
    
    plt.show()
    
def comparePlot():
    plt.figure()
    
    plt.subplots_adjust(hspace=0.4, wspace=0.4)
    
    plt.hist(bcyData["ann_return"],density = True, label= 'Barclays', alpha=0.6)
    
    plt.hist( bpData["ann_return"],density = True, label= 'BP',alpha=0.2)
    plt.legend()
    
    plt.show()

def boxplot():
    data = [bcyData["ann_return"], bpData["ann_return"], tescoData["ann_return"], VodaData["ann_return"]]
    plt.figure()
    plt.boxplot(data)
    plt.show()
    
def violineplot():
    data = [bcyData["ann_return"], bpData["ann_return"], tescoData["ann_return"], VodaData["ann_return"]]
    plt.figure()
    plt.violinplot(data, showmedians=True)
    plt.xticks([1,2,3,4], ['Barclays','BP','TESCO','Vodaphone'])
    plt.show()
    
# display data 
# dispData()
# display subplots
# subPlots()
# display pie plot
# piePlot()
# histogramPlot()
# comparePlot()
# boxplot()
violineplot()