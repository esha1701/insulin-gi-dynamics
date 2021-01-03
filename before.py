
from GI import *
from exponential import *
plt.plot(time_new, model_scaled, "r-", linewidth = 1, label ="Insulin Curve")
plt.plot(carbtime_new, bg_scaled, linewidth = 1, label ="GI Curve")

plt.xlabel("time", fontsize = 12)
plt.legend(loc ="upper right", fontsize = 12)
      
plt.show()
    


  
