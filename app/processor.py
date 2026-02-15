import pvleopard, re
from services.time import Time

class Processor():
    def __init__(self, access_key, assignments):
        self.leopard = pvleopard.create(access_key = access_key, enable_automatic_punctuation = True)
        self.time = Time()
        self.assignments = assignments

    def process(self, audio):
        result = self.leopard.process(audio)
        transcript = result[0]

        if re.search(r'\btime\b', transcript, re.IGNORECASE):
            current_time = self.time.time()
            return transcript, current_time
        
        elif re.search(r'\bdate\b', transcript, re.IGNORECASE):
            date = self.time.date()
            return transcript, date
        
        elif re.search(r'\bassignment\b', transcript, re.IGNORECASE):
                self.assignments.add()
                return transcript, "Assignment added."
        else:
            return transcript, "I did not understand"