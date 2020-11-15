import pyaudio

CHUNK=1024*2
RATE=44100
r= 1.059463094
r12=r*r*r*r
p=pyaudio.PyAudio()

stream=p.open(	format = pyaudio.paInt16,
		channels = 1,
		rate = RATE,
		frames_per_buffer = CHUNK,
		input = True,
		output = True)
stream2=p.open(	format = pyaudio.paInt16,
		channels = 1,
		rate = RATE,
		frames_per_buffer = int(RATE*r12),
		input = True,
		output = True) # inputとoutputを同時にTrueにする


# def audio_trans(input):
    
#     return ret


while stream.is_active():
    input = stream.read(CHUNK)
    output = stream1.write(input)

