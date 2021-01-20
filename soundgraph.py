import pyaudio                      #録音用    
import numpy as np                  #計算用
import matplotlib.pyplot as plt     #グラフ化用
import itertools
import struct
import wave


#設定
chunk = 1024         #音声データメモリーサイズ指定
FORMAT = pyaudio.paInt32        #16進数に指定
CHANNELS = 1                    #モノラルに指定
RATE = 43008             #サンプリング速度-サンプリング周波数(、1秒間に実行する標本化（サンプリング）処理の回数のこと)
T = 1/RATE
RECORD_SECONDS = 2           #３秒録音
inputIndexNumber = int(input('type input index number'))
outputIndexNumber = int(2)
t = np.arange(0, RATE*T*RECORD_SECONDS, T) #時間軸が1/2倍違う

p = pyaudio.PyAudio()           #!!!要調べ！！！

 #!!!要調べ！！！
stream = p.open(format = FORMAT,
                channels = CHANNELS,
                rate = RATE,
                input = True,
                input_device_index = inputIndexNumber,
                output_device_index = outputIndexNumber,
                output = True,
                frames_per_buffer = chunk
)
 #!!!要調べ！！！
print("Now Recording...")
all = [] #リスト作成
for i in range (0,int(RATE / chunk * RECORD_SECONDS)): 
    data = stream.read(chunk)
    all.append(data)

print("Finished Recording.")

data2 = b"".join(all) #b""

result = np.frombuffer(data2,dtype="int32") / float (2**15)

with open ('file1.txt', 'w') as f:
    np.set_printoptions(threshold=np.inf)
    # print(len(all))
    # print(len(data2))
    # print(len(result))
    # print(result, file=ｆ)
    print(RATE / chunk * RECORD_SECONDS)
    print(len(np.frombuffer(data2,dtype="int32")))
    print("loopnumber: %o, all-length: %s, data2-length: %f, result-length: %a," % (i,len(all), len(data2), len(result)))
    print(p.get_device_info_by_index(inputIndexNumber),)

allresult = 0
firstloop = True

for i in range (len(result)):
    if result[i] > 0 or result[i] < 0:
        if firstloop:
            aboveZeroPoint = i
            allresult += result[i]
            firstloop = False
            pass
        else:
            allresult += result[i]
            pass
    else:
        pass

resultaverage = allresult/(len(result) - aboveZeroPoint)
print("平均 %i 最初のゼロ以上の位置 %f"% (resultaverage,aboveZeroPoint))
result3 = np.arange(len(result))
for i in range (len(result)):
    if i < aboveZeroPoint:
        result3[i] = result[i]
        pass
    else:
        result3[i] = result[i] - resultaverage
waruni = int(len(result3)/2)
print(waruni)
result4 = result3[waruni:]

#直流成分を除いた
WindowHn = np.hanning(len(result4))
result5 = result4*WindowHn
F = np.fft.fft(result5) 
cut = 50
F2 = np.where(2*abs(F)/RATE>cut,0,F)

IF = np.fft.ifft(F2)
F3 = np.fft.fft(IF)
IF2 = np.tile(IF,3)
# FFTの複素数結果を絶対に変換
F_abs = np.abs(F)
F_abs2 = F_abs[:int(RATE/2)] #虚像成分を除くために半分にした
# 振幅をもとの信号に揃える
F_abs_amp = F_abs2 / RATE * 2 # 交流成分はデータ数で割って2倍
# 周波数軸のデータ作成
fq = np.linspace(0, RATE/2, RATE/2) # 周波数軸　linspace(開始,終了,分割数) *虚像成分を除くために半分にした

F3_abs = np.abs(F3)
F3_abs2 = F3_abs[:int(RATE/2)] #虚像成分を除くために半分にした
# 振幅をもとの信号に揃える
F3_abs_amp = F3_abs2 / RATE * 2 # 交流成分はデータ数で割って2倍
# 周波数軸のデータ作成


amparraynumber = np.where(F_abs_amp > cut) #10以上の位置を所得
biggestAmp = F_abs_amp[np.argmax(F_abs_amp)]
print("最大振幅 %i"%(F_abs_amp[np.argmax(F_abs_amp)]))
amparraynumber2 = list(itertools.chain.from_iterable(amparraynumber))

print(len(amparraynumber2))
print("F_amp_abs - length %a, amparrraynumber2 - length %o, " % (len(F_abs_amp),len(amparraynumber2)))
print(amparraynumber2)
s = 0
sin_curve = 0
slen = int(RATE*5)
print("now generating sound...")
# for i in range (len(amparraynumber2)):
#     s +=  (np.sin(2*np.pi*np.arange(slen)*amparraynumber2[i]/(RATE*5)) * (F_abs_amp[amparraynumber2[i]]*10000/biggestAmp) )
# Fs = np.fft.fft(s)
# Fs_abs = np.abs(Fs)
# Fs_abs2 = Fs_abs[:int(RATE/2)] #虚像成分を除くために半分にした
# # 振幅をもとの信号に揃える
# Fs_abs_amp = Fs_abs2 / RATE * 2 # 交流成分はデータ数で割って2倍
# # 周波数軸のデータ作成
# IFs = np.fft.ifft(Fs)



print("sound generate ended")


# print(F_abs_amp)
# グラフ表示
fig = plt.figure(figsize=(12, 4))

# plt.plot(samples)
# 信号のグラフ（時間軸）
ax2 = fig.add_subplot(161)
plt.xlabel('time(sec)', fontsize=14)
plt.ylabel('amplitude', fontsize=14)
plt.plot(t,result3)

# FFTのグラフ（周波数軸）
ax2 = fig.add_subplot(162)
plt.xlabel('freqency(Hz)', fontsize=14)
plt.ylabel('amplitude', fontsize=14)
plt.plot(fq[:int(RATE/2)+1], F_abs_amp[:int(RATE/2)+1]) # ナイキスト定数まで表示
print("plotting graph...")

ax2 = fig.add_subplot(163)
plt.plot(IF)


ax2 = fig.add_subplot(164)
plt.xlabel('time(sec)', fontsize=14)
plt.ylabel('amplitude', fontsize=14)
plt.plot(s)

ax2 = fig.add_subplot(165)
plt.xlabel('freqency(Hz)', fontsize=14)
plt.ylabel('amplitude', fontsize=14)
plt.plot(fq[:int(RATE/2)+1], F3_abs_amp[:int(RATE/2)+1]) # ナイキスト定数まで表示

# ax2 = fig.add_subplot(166)
# plt.xlabel('freqency(Hz)', fontsize=14)
# plt.ylabel('amplitude', fontsize=14)
# plt.plot(fq[:int(RATE/2)+1], Fs_abs_amp[:int(RATE/2)+1])
# print(Amp)
# plt.plot(fq, Amp)
# plt.xlabel('Frequency', fontsize=20)
# plt.ylabel('Amplitude', fontsize=20)
# plt.grid()


stream.write(IF2.astype(np.float32).tostring())
stream.stop_stream()
stream.close()

p.terminate()
plt.show()
plt.plot(WindowHn)
plt.show()