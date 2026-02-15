import pvporcupine
from pvrecorder import PvRecorder

class Listener():
    def __init__(self):
        pass

    def create(self, access_key, keyword_path):
        porcupine = pvporcupine.create(
                    access_key = access_key,
                    keyword_paths = [keyword_path]
                    )
        self.listen(porcupine = porcupine)
        
    def listen(self, porcupine):
        print(porcupine)
        recorder = PvRecorder(device_index = -1, frame_length = 512)
        recorder.start()
        try:
            while True:
                audio = recorder.read()
                index = porcupine.process(audio)
                if index >= 0:
                     print("hey")

        except KeyboardInterrupt:
                recorder.stop()
                recorder.delete()
                porcupine.delete()