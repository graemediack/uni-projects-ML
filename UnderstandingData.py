# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 10:49:56 2019

@author: graeme
"""

'''
*******************************
******** DATA ANALYSIS ********
*******************************
'''
#Display Column Headers
data.columns
#Display first 3 rows of data
data.head(3)
#Display Column Data Types
data.dtypes
#Display unique dtypes that occur in the DF
data.dtypes.unique()
#Find out if there are any missing values
data.isnull().sum()
'''
Do the data types chosen by Pandas make sense?
In the case of the dataframe created from this projects csv, there are only
2 dtypes, int64 and O for strings.
'''
#Create a lists of each dtype attribute, for use in later functions
numericals = ['Staff', 'Floor Space', 'Window', \
              'Demographic score', '40min population', \
              '30 min population', '20 min population', \
              '10 min population', 'Store age', 'Clearance space', \
              'Competition number', 'Competition score', 'Profit']

nominals = ['Town', 'Country', 'Manager name', 'Car park', \
            'Location','Performance']

