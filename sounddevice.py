import pyaudio
 
pa = pyaudio.PyAudio()
for i in range(pa.get_device_count()):
    print(pa.get_device_info_by_index(i),)
    #{'index': 6, 'structVersion': 2, 'name': 'Mic/Inst/Line In 1/2 (Studio 26', 'hostApi': 0, 'maxInputChannels': 2, 'maxOutputChannels': 0, 'defaultLowInputLatency': 0.09, 'defaultLowOutputLatency': 0.09, 'defaultHighInputLatency': 0.18, 'defaultHighOutputLatency': 0.18, 'defaultSampleRate': 44100.0}
    #{'index': 9, 'structVersion': 2, 'name': 'Main Out 1/2 (Studio 26c)', 'hostApi': 0, 'maxInputChannels': 0, 'maxOutputChannels': 2, 'defaultLowInputLatency': 0.09, 'defaultLowOutputLatency': 0.09, 'defaultHighInputLatency': 0.18, 'defaultHighOutputLatency': 0.18, 'defaultSampleRate': 44100.0}