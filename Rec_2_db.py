import warnings
warnings.filterwarnings("ignore")
import pyaudio
import numpy as np
import audioop
import math
import itertools
import os
import subprocess

CHUNK = 1024
WIDTH = 2
CHANNELS = 2
FORMAT = pyaudio.paInt16
RATE = 44100

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,#p.get_format_from_width(WIDTH)
                channels=CHANNELS,
                rate=RATE,
                input=True,#output = True
                frames_per_buffer=CHUNK)

db = 0
frames = []
buffer = []

stream.start_stream()



print("* recording")

for x in itertools.repeat(1):
    data = stream.read(CHUNK)
    frames.append(data) 
    decoded = np.frombuffer(data, 'float32')
    rms = audioop.rms(decoded, 2) # 2 bytes of audio data
    print("rms:{}".format(rms))
    try:
        db = 20 * (math.log(rms,10))
        print("db:{}".format(db))   
    except:
        pass 
    if (db > 84):
        subprocess.run(['python3', 'rec_2_detect.py'])
        


stream.stop_stream()
stream.close()

p.terminate()
#팀 관심법

 
