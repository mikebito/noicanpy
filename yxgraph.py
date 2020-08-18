from matplotlib import pylab  as plt
import numpy as np

a = 1     #振幅
fs = 96 * (10**3) #サンプリング周波数
f0 =  20 #周波数
sec = 0.005  #秒
tpi = 2 * np.pi
 
yx=[]

for num in np.arange(10000): 
    y = a * np.sin( 2 * np.pi * (0 / 2 - num / 100))
    yx.append(y)
    
plt.plot(yx)
plt.show()
plt.ioff()
