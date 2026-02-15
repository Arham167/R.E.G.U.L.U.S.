import pvleopard

class Processor():
    def __init__(self, access_key):
        self.leopard = pvleopard.create(access_key = access_key)

    def process(self, audio):
        transcript = self.leopard.process(audio)
        return transcript