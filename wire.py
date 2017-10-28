"""
PyAudio Example: Make a wire between input and output (i.e., record a
few samples and play them back immediately).

This is the callback (non-blocking) version.
"""

import pyaudio
import time
import numpy as np

WIDTH = 2
CHANNELS = 2
RATE = 44100

p = pyaudio.PyAudio()

def callback(in_data, frame_count, time_info, status):

    # take the max and clamp it?
    # max_val = max(in_data)
    # in_data = in_data[::-1] # simple inversion
    # print(in_data)
    # TODO , need to take into account the delay.


    decoded = np.fromstring(in_data, 'Float32')
    max_val = max(decoded)
    min_val = min(decoded)
    # print(decoded)
    print(max_val, min_val)
    # decoded = np.array_str(decoded)
    return (in_data, pyaudio.paContinue)

stream = p.open(format=p.get_format_from_width(WIDTH),
                channels=CHANNELS,
                rate=RATE,
                input=True,
                output=True,
                stream_callback=callback)

stream.start_stream()

while stream.is_active():
    time.sleep(0.1)

stream.stop_stream()
stream.close()

p.terminate()
