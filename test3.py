from matplotlib import pylab  as plt
import numpy as np

a = 1     #振幅
fs = 96 * (10**3) #サンプリング周波数
f0 =  20 #周波数
sec = 0.1  #秒
 
swav=[]
yx=[]
 
ti3 = fs * 3
for num in np.arange(fs * sec):
    #サイン波を生成
    y = a * np.sin(2.0 * np.pi * num / 5 - num / 3)
    s = a * np.sin(2.0 * np.pi * f0 * num / fs)
    swav.append(s)
    yx.append(y)
    if num == fs * 1:
    	break
    	
 
#サイン波を表示
siny = np.arange(0,1000)
plt.plot(swav)
plt.show()
plt.plot(yx)
plt.show()
plt.ioff()
