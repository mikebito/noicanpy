import pyaudio                      #録音用    
import numpy as np                  #計算用
import matplotlib.pyplot as plt     #グラフ化用
import itertools
import struct
import wave

chunk = 1024         #音声データメモリーサイズ指定
FORMAT = pyaudio.paInt32        #16進数に指定
CHANNELS = 1                    #モノラルに指定
RATE = 43008             #サンプリング速度-サンプリング周波数(、1秒間に実行する標本化（サンプリング）処理の回数のこと)
T = 1/RATE
RECORD_SECONDS = 1  
slen = int(RATE*5)
freq = [440,554.365,659.255]
amp = []
inputIndexNumber = int(input('type input index number'))
outputIndexNumber = int(1)
t = np.arange(0, RATE*T*RECORD_SECONDS, T)

p = pyaudio.PyAudio()  
stream = p.open(format = FORMAT,
                channels = CHANNELS,
                rate = RATE,
                input = True,
                input_device_index = inputIndexNumber,
                output_device_index = outputIndexNumber,
                output = True,
                frames_per_buffer = chunk
)
s = np.zeros(slen)
sinef = np.zeros(slen)
# for i in range (len(freq)):
#     sinef = np.sin(2*np.pi*np.arange(slen)*freq[i]/(RATE*5))
#     s = s + sinef
sinef1 = np.sin(2*np.pi*np.arange(slen)*440/(RATE*5))
sinef2 = np.sin(2*np.pi*np.arange(slen)*554.365/(RATE*5))
# sinef3 = np.sin(2*np.pi*np.arange(slen)*659.25/(RATE*5))
s = s + sinef1 + sinef2# + sinef3
print("length-%i, dtype-%a"%(len(s),sinef.dtype))
F = np.fft.fft(s)
# FFT結果（複素数）を絶対値に変換
F_abs = np.abs(F)
# 振幅を元に信号に揃える
F_abs_amp = F_abs / RATE * 2 # 交流成分はデータ数で割って2倍する
F_abs_amp[0] = F_abs_amp[0] / 2 # 直流成分（今回は扱わないけど）は2倍不要

# グラフ表示（データ数の半分の周期を表示）

stream.write(s.astype(np.float32).tostring())
stream.stop_stream()
stream.close()

p.terminate()

ax2 = fig.add_subplot(133)
plt.xlabel('time(sec)', fontsize=14)
plt.ylabel('amplitude', fontsize=14)

plt.plot(sinef1+sinef2)
# plt.plot(sinef2)
# plt.plot(sinef3)
plt.plot(s)
plt.plot(F_abs_amp[:int(RATE/2)+1])
plt.show()