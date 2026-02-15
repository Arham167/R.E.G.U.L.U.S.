import pvporcupine
from pvrecorder import PvRecorder

class Listener():
    def __init__(self, access_key, keyword_path):
        self.porcupine = pvporcupine.create(
                    access_key = access_key,
                    keyword_paths = [keyword_path],
                    sensitivities = [1]
                    )
        self.recorder = PvRecorder(device_index = -1, frame_length = self.porcupine.frame_length)
    
    def listen(self, sample_rate, record_seconds, silence_counter, silence_threshold, active_mode = False):
        self.recorder.start()

        if not active_mode:
            print("Listening")

            try:
                while True:
                    audio = self.recorder.read()
                    index = self.porcupine.process(audio)
                    
                    if index >= 0:
                        print("detected")
                        return
            except KeyboardInterrupt:
                self.recorder.stop()
                self.recorder.delete()
                self.porcupine.delete()

        else:
            print("waiting for commands")
            recorded_audio = []
            max_silence_frames = int(1 * sample_rate / self.porcupine.frame_length)
            max_frames = int(record_seconds * sample_rate / self.porcupine.frame_length)

            for _ in range(max_frames):
                frame = self.recorder.read()
                recorded_audio.extend(frame)

                energy = sum(sample**2 for sample in frame) / len(frame)

                if energy < silence_threshold:
                    silence_counter += 1
                else:
                    silence_counter = 0

                if silence_counter >= max_silence_frames:
                    break

            return recorded_audio
    