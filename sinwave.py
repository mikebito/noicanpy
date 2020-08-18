import numpy as np
import matplotlib.pyplot as plt

# 簡単な信号の作成
N = 1000 # サンプル数
dt = 0.0008 # サンプリング周期(sec):100ms =>サンプリング周波数100Hz
fs = 8000
freq = 440 # 周波数(10Hz) =>正弦波の周期0.1sec
amp = 1 # 振幅
sec =  2

swav=[]

for n in np.arange(fs * sec):

    s = amp * np.sin(2.0 * np.pi * freq * n / fs)
    swav.append(s)

# グラフ表示

plt.plot(swav[0:1000])

plt.show()