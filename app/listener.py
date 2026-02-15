import pvporcupine
from pvrecorder import PvRecorder
import struct

class Listener():
    def __init__(self, access_key, keyword_path):
        self.porcupine = pvporcupine.create(
                    access_key = access_key,
                    keyword_paths = [keyword_path]
                    )
        self.recorder = PvRecorder(device_index = -1, frame_length = self.porcupine.frame_length)
    
    def listen(self):
        self.recorder.start()

        try:
            while True:
                audio = self.recorder.read()
                index = self.porcupine.process(audio)

                if index >= 0:
                    print("detected")
                    recorded_audio = []
                    sample_rate = 16000
                    silence_counter = 0
                    silence_threshold = 500
                    max_silence_frames = int(1 * sample_rate / self.porcupine.frame_length)

                    for _ in range(int(3 * sample_rate / self.porcupine.frame_length)):
                        frame = self.recorder.read()
                        recorded_audio.extend(frame)

                        energy = sum(sample**2 for sample in frame) / len(frame)
                        if energy < silence_threshold:
                            silence_counter += 1
                        else:
                            silence_counter = 0

                        if silence_counter > max_silence_frames:
                            break
                        

                    self.recorder.stop()

                    return recorded_audio
                
        except KeyboardInterrupt:
                self.recorder.stop()
                self.recorder.delete()
                self.porcupine.delete()