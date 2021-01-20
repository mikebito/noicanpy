import pyaudio                      #録音用    
import numpy as np                  #計算用
import matplotlib.pyplot as plt     #グラフ化用
import itertools
import struct
import wave

def fft():
    """
    docstring
    """
    pass
def main():
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
     
    print("Now Recording...")
    all = [] #リスト作成
    for i in range (0,int(RATE / chunk * RECORD_SECONDS)): 
        data = stream.read(chunk)
        all.append(data)
    print("Finished Recording.")

        pass