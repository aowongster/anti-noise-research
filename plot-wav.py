import matplotlib.pyplot as plt
import numpy as np
import wave
import sys


spf = wave.open('output.wav','r')

#Extract Raw Audio from Wav File
signal = spf.readframes(-1)
signal = np.fromstring(signal, 'Int16')
fs = spf.getframerate()

#If Stereo
# if spf.getnchannels() == 2:
#     print 'Just mono files'
#     sys.exit(0)


# divide axis by frame rate to get x axis in seconds
Time=np.linspace(0, len(signal)/fs, num=len(signal))

plt.figure(1)
plt.title('Signal Wave...')
plt.plot(Time,signal)
plt.show()
