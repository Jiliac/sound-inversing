import pyaudio
import wave
from pydub import AudioSegment
from pydub.playback import play

def record_10sec(outputFile):
    CHUNK = 512
    FORMAT = pyaudio.paInt16

    p = pyaudio.PyAudio()
    stream = p.open(
      format = FORMAT,
      channels = 1,
      rate = 44100,
      input = True,
      frames_per_buffer = 512
    )

    print("Recording")

    frames = []

    for i in range(0,int(44100/512*10)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("** Done Recodring **")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(outputFile, 'wb')
    wf.setnchannels(1)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(44100)
    wf.writeframes(b''.join(frames))
    wf.close()

FILE = "output.wav"
REPLAY_X = 1
record_10sec(FILE)

audio = AudioSegment.from_file(FILE, 'wav')
invers = audio.invert_phase()
print("ca joue")
play(invers * REPLAY_X)

print('** Finished **')
