# -*- coding: utf-8 -*-
from matplotlib import pylab  as pltx

import numpy as np

a = 1     #振幅
fs = 96 * (10**3) #サンプリング周波数
f0 =  20 #周波数
sec = 0.005  #秒
tpi = 2 * np.pi
la = 1000 #波長
T = 2 #周期
time = 1 #時刻
 
yx=[]

for num in np.arange(10000): 
    y = a * np.sin( 2 * np.pi * (time / T - num / la ))
    yx.append(y)

    
plt.plot(yx)
plt.show()
plt.ioff()
