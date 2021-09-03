import pyaudio                      #録音用    
import numpy as np                  #計算用
import matplotlib.pyplot as plt     #グラフ化用
import wave




#設定
chunk = 2 ** 10        #音声データメモリーサイズ指定
FORMAT = pyaudio.paInt16        #16進数に指定
CHANNELS = 1                    #モノラルに指定
RATE = 43008 #サンプリング速度-サンプリング周波数(、1秒間に実行する標本化（サンプリング）処理の回数のこと)
T = 1/RATE
RECORD_SECONDS = 3        #6秒録音
inputIndexNumber = int(2)
outputIndexNumber = int(input())
t = np.arange(0, RATE*T*RECORD_SECONDS, T) #時間軸が1/2倍違う

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


def audio_trans(data):
    all = []
    all.append(data)
    data2 = b"".join(all) #b""
    all = []
    result = np.frombuffer(data2,dtype="int16") / float (2**15)
    # print(result,len(result))
    result = result * -100000
    return result

while stream.is_active(): 
    data = stream.read(chunk,exception_on_overflow = False)
    data = audio_trans(data)
    stream.write(data.astype(np.int16).tobytes())
	
stream.stop_stream()
stream.close()
p.terminate()

print ("Stop Streaming")