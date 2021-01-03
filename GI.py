import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.linear_model import LinearRegression 
from sklearn.preprocessing import PolynomialFeatures 
import csv

with open('data.csv') as csvfile:
    reader= csv.reader(csvfile)
    bg=list(reader)

arr= np.array([i for i in range(0,120,5)])
carbtime=arr.reshape(-1, 1)

carbpoly_features = PolynomialFeatures(degree=5, include_bias = False)
carbtime_poly = carbpoly_features.fit_transform(carbtime)
carblin_reg = LinearRegression()
carblin_reg.fit(carbtime_poly, bg)


carbtime_new = np.linspace(0, 105, 105).reshape(105, 1)
carbtime_new_poly = carbpoly_features.transform(carbtime_new)
bg_fit = carblin_reg.predict(carbtime_new_poly)


#Min-max normalisation of blood sugar values

bg_scaled=[]
for i in range(len(bg_fit)):
    bg_scaled.append((bg_fit[i]-min(bg_fit)) / (max(bg_fit)-min(bg_fit)))

    


