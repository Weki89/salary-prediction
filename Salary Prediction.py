# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 19:51:43 2020

@author: Jeffin
"""



import pandas as pd
import numpy as np
import pickle

url = "https://s3.us-west-2.amazonaws.com/public.gamelab.fun/dataset/salary_data.csv"
data = pd.read_csv(url)

x = data.iloc[:,:-1]   #cE
y = data.iloc[:,1]



from sklearn.model_selection import train_test_split #CE
[xtrain, xtest, ytrain, ytest] = train_test_split(x,y,train_size=0.9)



from sklearn.linear_model import LinearRegression
model1 = LinearRegression()
model1.fit(xtrain,ytrain)
print("done")


model1.predict(np.array([10]).reshape(1,1))
'''
# Saving model to disk
pickle.dump(model1, open('spmodel.pkl','wb'))

# Loading model to compare the results
model = pickle.load(open('spmodel.pkl','rb'))
print(model.predict([[2]]))
'''