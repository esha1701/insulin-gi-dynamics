
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
  



x = np.array([0,19,25,31,41,60,68,96,118,147,175,212,244,275,308,330])
time = x.reshape(-1, 1)
insulin_conc= np.array([0,0.352,0.668,1.000,1.296,1.519,1.451,1.332,1.032,0.709,0.438,0.270,0.211,0.091,0.032,0])



def checkfit(deg):
    
    poly_features = PolynomialFeatures(degree = deg, include_bias = False)
    time_poly = poly_features.fit_transform(time)
    lin_reg = LinearRegression()
    lin_reg.fit(time_poly, insulin_conc)
    insulin_bic = lin_reg.predict(time_poly)


    res = np.subtract(insulin_bic, insulin_conc)
    n=len(insulin_conc)
    RSS = np.sum(np.power(res, 2))
    BIC = n*np.log(RSS/n) + 1*np.log(n)
    return BIC
    
    



    
