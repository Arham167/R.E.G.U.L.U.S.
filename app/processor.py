import pvleopard

class Processor():
    def __init__(self, access_key):
        self.leopard = pvleopard.create(access_key = access_key, enable_automatic_punctuation = True)

    def process(self, audio):
        transcript = self.leopard.process(audio)
        if "tell me time" in transcript:
            print("time")
        return transcript