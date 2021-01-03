
from GI import *
from exponential import *



maxIndex1=model_scaled.index(1)
insulinPeakTime=time_new[maxIndex1]
  
maxIndex2=bg_scaled.index(1)
carbPeakTime=carbtime_new[maxIndex2]
gap= insulinPeakTime - carbPeakTime  

plt.plot(time_new - gap  , model_scaled, "r-", linewidth = 1, label ="Shifted Insulin Curve")
plt.plot(carbtime_new, bg_scaled, linewidth = 1, label ="GI Curve")

plt.xlabel("time", fontsize = 12)
plt.legend(loc ="upper right", fontsize = 12)
      
plt.show()
    
