
import numpy as np
from scipy.optimize import curve_fit
from matplotlib import pyplot as plt
  
  
  
def func(t, a, b, c):
    return a * (t**b) * np.exp(- t/c)
  

t = np.array([0,19,25,31,41,60,68,96,118,147,175,212,244,275,308,330])
y = np.array([0,0.352,0.668,1.000,1.296,1.519,1.451,1.332,1.032,0.709,0.438,0.270,0.211,0.091,0.032,0])

  
coefs, covariance = curve_fit(func, t, y)


time_new = np.linspace(0, 330, 330).reshape(330, 1)
model= (coefs[0]*(time_new**coefs[1])*(np.exp(-time_new/coefs[2])))
    
#Min-max normalisation of insulin concentration
model_scaled=[]
for i in range(len(model)):
    model_scaled.append((model[i]-min(model)) / (max(model)-min(model)))

    



