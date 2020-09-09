import pyaudio
import numpy as np

 

CHUNK = 1024
RATE = 44100           

p = pyaudio.PyAudio()

stream=p.open(  format = pyaudio.paInt16,

        channels = 1,

        rate = RATE,

        frames_per_buffer = CHUNK,

        input = True,

        output = True)

try:
    while stream.is_active():

        input1=stream.read(CHUNK)

        input2=np.array(np.frombuffer(input1,dtype="int16"))

        input3=-1*input2

        input4=input3.tobytes()

        output = stream.write(input4)

except KeyboardInterrupt:

    stream.stop_stream()

    stream.close()

    p.terminate()

    print("Stop Streaming")