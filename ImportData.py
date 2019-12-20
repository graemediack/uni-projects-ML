# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 12:11:22 2019

@author: graeme
"""
'''
*******************************
********  DATA IMPORT  ********
*******************************
'''
#Import csv file into Pandas dataframe
dataFull = pd.read_csv('storedata.csv',encoding='latin-1')
'''
*******************************
********  DATA SPLIT  *********
*******************************
'''
#Using scikit built in tool, split the data into train and test set
data, dataTest = model_selection.train_test_split(dataFull,test_size=0.2,shuffle=True,random_state=42)
