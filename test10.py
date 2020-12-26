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
RECORD_SECONDS = 1           #３秒録音
inputIndexNumber = int(input('type input index number'))
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
print(all)
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
    else:
        result3[i] = result[i] - resultaverage
#直流成分を除いた
F = np.fft.fft(result3) 
# FFTの複素数結果を絶対に変換
F_abs = np.abs(F)
F_abs2 = F_abs[:int(RATE/2)] #虚像成分を除くために半分にした
# 振幅をもとの信号に揃える
F_abs_amp = F_abs2 / RATE * 2 # 交流成分はデータ数で割って2倍
# 周波数軸のデータ作成
fq = np.linspace(0, RATE/2, RATE/2) # 周波数軸　linspace(開始,終了,分割数) *虚像成分を除くために半分にした
amparraynumber = list(np.where(F_abs_amp > 50)) #10以上の位置を所得
biggestAmp = F_abs_amp[np.argmax(F_abs_amp)]
print("最大振幅 %i"%(F_abs_amp[np.argmax(F_abs_amp)]))
amparraynumber2 = list(itertools.chain.from_iterable(amparraynumber))
print(amparraynumber)