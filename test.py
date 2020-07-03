import numpy as np
import matplotlib.pyplot as plt


# 簡単な信号の作成
N = 8192 # サンプル数
dt = 0.001 # サンプリング周期(sec):100ms =>サンプリング周波数100Hz
freq = 10 # 周波数(10Hz) =>正弦波の周期0.1sec
freq2 = 5
amp = 1 # 振幅
amp2 = 3
t = np.arange(0, N*dt, dt) # 時間軸
f = amp * np.sin(2*np.pi*freq*t) #+ amp2 * np.sin(2*np.pi*freq2*t)# 信号（周波数10、振幅1の正弦波）
# グラフ表示
plt.xlabel('time(sec)', fontsize=14)
plt.ylabel('signal amplitude', fontsize=14)
plt.plot(t, f)

plt.show()


F = np.fft.fft(f) # 高速フーリエ変換(FFT)

# FFTの複素数結果を絶対に変換
F_abs = np.abs(F)
# 振幅をもとの信号に揃える
F_abs_amp = F_abs / N * 2 # 交流成分はデータ数で割って2倍する
F_abs_amp[0] = F_abs_amp[0] / 2 # 直流成分（今回は扱わないけど）は2倍不要
# グラフ表示
# plt.plotw(F_abs_amp) # ->NG、周波数軸に変更する必要あり

# plt.show()

# 周波数軸のデータ作成
fq = np.linspace(0, 1.0/dt, N) # 周波数軸　linspace(開始,終了,分割数)

def minus(n):
    return n * -1

# 周波数軸に変更してグラフを再表示
plt.xlabel('freqency(Hz)', fontsize=14)
plt.ylabel('signal amplitude', fontsize=14)

# print(fq[:int(N/2)+1],)
# print(F_abs_amp[:int(N/2)+1])

# F_abs_amp_comp = np.all(F_abs_amp > 0.1)
print(np.all(F_abs_amp > 0))


# for s in F_abs_amp > 0.1:
#     print(F_abs_amp)

F_abs_amp2 = [s for s in F_abs_amp if s > 0.1]
print(F_abs_amp2)
                
np.savetxt("compare.csv", np.vstack(F_abs_amp2[:int(N/8)+1]).T, delimiter=",")
np.savetxt("x.csv", np.vstack(fq[:int(N/2)+1]).T, delimiter=",")
np.savetxt("y.csv", np.vstack(F_abs_amp[:int(N/2)+1] ).T, delimiter=",")
print(max(F_abs_amp))

max = sorted(F_abs_amp, reverse=True)
np.savetxt("abc.csv", np.vstack(max[:int(N)+1]).T, delimiter=",")
plt.plot(fq[:int(N/16)+1], F_abs_amp[:int(N/16)+1]) # ナイキスト定数まで表示
plt.show()

