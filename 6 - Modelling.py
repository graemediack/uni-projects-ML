# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 21:06:45 2019

@author: graeme
"""


'''
#MLP Classifier
clf = neural_network.MLPClassifier(solver='lbfgs', alpha=1e-5,hidden_layer_sizes=(6,4), random_state=1)
clf.fit(dataX[numericalsCleaned],dataPerformanceTarget)
clf.predict(dataTestX[numericalsCleaned])
clf.score(dataTestX[numericalsCleaned],dataTestPerformanceTarget)

#MLP Regressor
clf = neural_network.MLPRegressor(solver='adam',hidden_layer_sizes=(6,4),random_state=1)
clf.fit(dataX[numericalsCleaned],dataProfitTarget)
clf.predict(dataTestX[numericalsCleaned])
clf.score(dataTestX[numericalsCleaned],dataTestProfitTarget)

#Random Forest Ensemble
clf = RandomForestRegressor()
clf.fit(dataX,dataProfitTarget)
#clf.score(dataX,dataProfitTarget)
clf.score(dataTestX,dataTestProfitTarget)

clf = tree.DecisionTreeClassifier()
clf.fit(dataX,dataPerformanceTarget)
clf.score(dataTestX,dataTestPerformanceTarget)

'''

#testing cross validation
clf = tree.DecisionTreeClassifier()
scores = model_selection.cross_val_score(clf,dataX,dataPerformanceTarget,cv=5)

#testing randomised search cv
param_dist = {"max_depth": [3, None],
              "max_features": [1,2,3,4,5,6],
              "min_samples_leaf": [1,2,3,4,5,6,7,8,9],
              "criterion": ["gini", "entropy"]}
clf = tree.DecisionTreeClassifier()
# Instantiate the RandomizedSearchCV object: tree_cv
clf_cv = model_selection.RandomizedSearchCV(clf, param_dist, cv=5,n_iter=100)
# Fit it to the data
clf_cv.fit(dataX[allAttrs], dataPerformanceTarget)

#Pickled Models
filename = 'MLPCLF_2.sav'
csv = 'MLPCLF_2.csv'
attrs = ['Clearance space', 'Competition number', \
         'Staff', 'Location', 'Floor Space', \
         'Car park', 'Competition score']
MLPCLF_2 = pd.read_csv(csv)


loaded_model = pickle.load(open('MLPCLF_5.sav','rb'))
loaded_model.fit(dataX[allAttrs],dataPerformanceTarget)
metrics.confusion_matrix()
loaded_model.predict()
