import numpy as np
import matplotlib.pyplot as plt

from scipy import signal

N = 2048 # データ数
n = np.arange(N)
f1 = 20
f2 = 22
a1 = 2
a2 = 5
f = a1 * np.sin(f1 *2*np.pi*n/N) + a2 * np.sin(f2 * 2 * np.pi * (n/N)) 

# グラフ表示
plt.figure(figsize=(8, 4))
plt.xlabel('n')
plt.ylabel('Signal')
plt.plot(f)
plt.show()


F = np.fft.fft(f) # 高速フーリエ変換(FFT)
print(type(F), F.dtype)
print(F) # FFT結果
# FFT結果（複素数）を絶対値に変換
F_abs = np.abs(F)
# 振幅を元に信号に揃える
F_abs_amp = F_abs / N * 2 # 交流成分はデータ数で割って2倍する
F_abs_amp[0] = F_abs_amp[0] / 2 # 直流成分（今回は扱わないけど）は2倍不要
np.savetxt("points.csv", np.vstack(F_abs_amp[:int(N/8)+1]).T, delimiter=",")
# グラフ表示（データ数の半分の周期を表示）
plt.plot(F_abs_amp[:int(N/2)+1], marker="o")

plt.show()
