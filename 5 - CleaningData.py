# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 10:53:32 2019

@author: graeme
"""


'''
*******************************
******** DATA CLEANING ********
*******************************

Following understanding and visualisation of raw data, some cleaning can be 
carried out
'''

#Replace values
data['Staff'].replace(-2,pd.np.nan,inplace=True)# switch outlier in Staff to NaN
data['Staff'].replace(300,pd.np.nan,inplace=True)# switch outlier in Staff to NaN
data['Staff'].replace(600,pd.np.nan,inplace=True)# switch outlier in Staff to NaN
#optional - drop instances/rows with undesirable NAN values
data = data.dropna()

data['Location'].replace('Village',pd.np.nan,inplace=True)# switch single instance of Village to NaN
data['Car park'].replace('Yes','Y',inplace=True)# switch Yes string to Y
data['Car park'].replace('No','N',inplace=True)# switch No string to N
data['Car park'].replace('Y',1,inplace=True)# switch Y string to 1
data['Car park'].replace('N',0,inplace=True)# switch N string to 0
#create a binomial classification of performance
data['perfbinom'] = data['Performance']
data['perfbinom'].replace('Poor',0,inplace=True)
data['perfbinom'].replace('Reasonable',0,inplace=True)
data['perfbinom'].replace('Good',1,inplace=True)
data['perfbinom'].replace('Excellent',1,inplace=True)

data['perfnum'] = data['Performance']
data['perfnum'].replace('Poor',1,inplace=True)
data['perfnum'].replace('Reasonable',2,inplace=True)
data['perfnum'].replace('Good',3,inplace=True)
data['perfnum'].replace('Excellent',4,inplace=True)

#Perform One Hot Encoding for Location column
data['Location'] = pd.Categorical(data['Location'])
dataOHE = pd.get_dummies(data['Location'])
data = pd.concat([data,dataOHE],axis=1)
#set Store ID as new index
data.set_index('Store ID',drop=True,inplace=True)
#Drop columns
data = data.drop(['Manager name','Town','Country','Window','Location'],axis=1)
#Rescale profit to 100,000GBP
data['Profit'] = data['Profit']/100000
data['Profit'] = data['Profit'].round(0)

#I can make some similar changes to the test data, without breaking the ethic
#of not touching this data.

dataTest['Car park'].replace('Yes','Y',inplace=True)# switch Yes string to Y
dataTest['Car park'].replace('No','N',inplace=True)# switch No string to N
dataTest['Car park'].replace('Y',1,inplace=True)# switch Y string to 1
dataTest['Car park'].replace('N',0,inplace=True)# switch N string to 0

dataTest['perfbinom'] = dataTest['Performance']
dataTest['perfbinom'].replace('Poor',0,inplace=True)
dataTest['perfbinom'].replace('Reasonable',0,inplace=True)
dataTest['perfbinom'].replace('Good',1,inplace=True)
dataTest['perfbinom'].replace('Excellent',1,inplace=True)

dataTest['perfnum'] = dataTest['Performance']
dataTest['perfnum'].replace('Poor',1,inplace=True)
dataTest['perfnum'].replace('Reasonable',2,inplace=True)
dataTest['perfnum'].replace('Good',3,inplace=True)
dataTest['perfnum'].replace('Excellent',4,inplace=True)

#Perform One Hot Encoding for Location column
dataTest['Location'] = pd.Categorical(dataTest['Location'])
dataTestOHE = pd.get_dummies(dataTest['Location'])
dataTest = pd.concat([dataTest,dataTestOHE],axis=1)
#set Store ID as new index
dataTest.set_index('Store ID',drop=True,inplace=True)
#Drop columns
dataTest = dataTest.drop(['Manager name','Town','Country','Window','Location'],axis=1)
#Rescale profit to 100,000GBP
dataTest['Profit'] = dataTest['Profit']/100000
dataTest['Profit'] = dataTest['Profit'].round(0)


#Final prep - split data into samples/features and targets
dataX = data.drop(['Performance','Profit','perfbinom','perfnum'],axis=1)
dataProfitTarget = data['Profit']
dataPerformanceTarget = data['Performance']
dataPerfbinomTarget = data['perfbinom']
dataPerfNumTarget = data['perfnum']

dataTestX = dataTest.drop(['Performance','Profit','perfbinom','perfnum'],axis=1)
dataTestProfitTarget = dataTest['Profit']
dataTestPerformanceTarget = dataTest['Performance']
dataTestPerfbinomTarget = dataTest['perfbinom']
dataTestPerfNumTarget = dataTest['perfnum']

columns = ['Staff', 'Floor Space', 'Demographic score', \
           '40min population', '30 min population', '20 min population', \
           '10 min population', 'Store age', 'Clearance space', \
           'Competition number', 'Competition score']

#scaling
scaler = preprocessing.StandardScaler()
scaler.fit(dataX[columns])
dataX[columns] = scaler.transform(dataX[columns])
dataTestX[columns] = scaler.transform(dataTestX[columns])
