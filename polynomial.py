import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.linear_model import LinearRegression 
from sklearn.preprocessing import PolynomialFeatures 
  





x = np.array([0,19,25,31,41,60,68,96,118,147,175,212,244,275,308,330]) 
time = x.reshape(-1, 1)





insulin_conc=[]
l=np.array([0,0.352,0.668,1.000,1.296,1.519,1.451,1.332,1.032,0.709,0.438,0.270,0.211,0.091,0.032,0])
for i in range(len(l)):
    insulin_conc.append((l[i]-min(l)) / (max(l)-min(l)))


poly_features = PolynomialFeatures(degree =7, include_bias = False)
time_poly = poly_features.fit_transform(time)
lin_reg = LinearRegression() 
lin_reg.fit(time_poly, insulin_conc)


score=lin_reg.score(time_poly,insulin_conc)
coefs=lin_reg.coef_
intercept=lin_reg.intercept_


time_new = np.linspace(0, 330, 330).reshape(330, 1) 
time_new_poly = poly_features.transform(time_new) 
insulin_conc_new = lin_reg.predict(time_new_poly)



plt.plot(x, insulin_conc, "b.", label ="Manufacturer Data")
plt.plot(time_new, insulin_conc_new, "r-", linewidth = 1, label ="Fitted Curve")



plt.xlabel("time", fontsize = 12) 
plt.ylabel("insulin concentration", rotation =90, fontsize = 12) 
plt.legend(loc ="upper right", fontsize = 12) 
  
  
  
  
  
  
  
  

plt.show()
