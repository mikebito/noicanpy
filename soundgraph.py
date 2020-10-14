import pyaudio                      #録音用    
import numpy as np                  #計算用
import matplotlib.pyplot as plt     #グラフ化用
import pandas

#設定
chunk = 2048         #音声データメモリーサイズ指定
FORMAT = pyaudio.paInt32        #16進数に指定
CHANNELS = 1                    #モノラルに指定
RATE = 43008             #サンプリング速度-サンプリング周波数(、1秒間に実行する標本化（サンプリング）処理の回数のこと)
T = 1/RATE
RECORD_SECONDS = 1           #３秒録音
inputIndexNumber = int(2)
outputIndexNumber = int(1)
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

# print(all)
print("Finished Recording.")


 #!!!要調べ！！！
data2 = b"".join(all)

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

# result2 = np.where((result > -300) & (result < 300) , 0 , result) 

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
    else:
        result3[i] = result[i] - resultaverage


F = np.fft.fft(result3) 
# FFTの複素数結果を絶対に変換
F_abs = np.abs(F)
# 振幅をもとの信号に揃える
F_abs_amp = F_abs / RATE * 2 # 交流成分はデータ数で割って2倍

# F_abs_amp2 = np.where((F_abs_amp < 10) , 0 , F_abs_amp) 
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
    else:
        result3[i] = result[i] - resultaverage

# l = [0] * (len(t) - len(result3))
# result4 = np.insert(result3,0,l)
# F_abs_amp[0] = F_abs_amp[0] / 2 # 直流成分（今回は扱わないけど）は2倍不要

# 周波数軸のデータ作成


# F_abs_amp[0:19] = 0
fq = np.linspace(0, 1.0/T, RATE) # 周波数軸　linspace(開始,終了,分割数)
amparraynumber = np.where(F_abs_amp > 10) #10以上の位置を所得
biggestAmp = F_abs_amp[np.argmax(F_abs_amp)]
# print(np.where(F_abs_amp > 10))
print("最大振幅 %i"%(F_abs_amp[np.argmax(F_abs_amp)]))
fqarray = fq[amparraynumber] 
print("F_amp_abs - length %a, amparrraynumber - length %o, fqarray - length %f" % (len(F_abs_amp),len(amparraynumber),len(fqarray)))
samples = 0
for i in range (len(amparraynumber)):
    samples += (np.sin(2*np.pi*(F_abs_amp[i]/biggestAmp)*10000*np.arange(RATE*20.0)*fqarray[i]/RATE)).astype(np.float32)
    # samples += (np.sin(2*np.pi*np.arange(RATE*20.0)*fqarray[i]/RATE)).astype(np.float32)
    print(F_abs_amp[i]/biggestAmp)
stream.write(1.0*samples)
# print(samples)

stream.stop_stream()
stream.close()

p.terminate()
# print(F_abs_amp)
# グラフ表示
fig = plt.figure(figsize=(12, 4))
# 信号のグラフ（時間軸）
ax2 = fig.add_subplot(121)
plt.xlabel('time(sec)', fontsize=14)
plt.ylabel('amplitude', fontsize=14)
plt.plot(t,result3)

# FFTのグラフ（周波数軸）
ax2 = fig.add_subplot(122)
plt.xlabel('freqency(Hz)', fontsize=14)
plt.ylabel('amplitude', fontsize=14)
plt.plot(fq[:int(RATE/2)+1], F_abs_amp[:int(RATE/2)+1]) # ナイキスト定数まで表示
plt.show()