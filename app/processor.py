import pvleopard, re

class Processor():
    def __init__(self, access_key, assignments, attendance, time):
        self.leopard = pvleopard.create(access_key = access_key, enable_automatic_punctuation = True)
        self.time = time
        self.assignments = assignments
        self.attendance = attendance

    def process(self, audio):
        result = self.leopard.process(audio)
        transcript = result[0]

        if re.search(r"\btime\b", transcript, re.IGNORECASE):
            current_time = self.time.time()
            return transcript, current_time
        
        elif re.search(r"\bdate\b", transcript, re.IGNORECASE):
            date = self.time.date()
            return transcript, date
        
        elif re.search(r"\bday\b", transcript, re.IGNORECASE):
            day = self.time.day()
            return transcript, day
        
        elif re.search(r"\bassignment\b", transcript, re.IGNORECASE):
            self.assignments.add()
            return transcript, "Assignment added."
        
        elif re.search(r"\bpresent\b", transcript, re.IGNORECASE):
             self.attendance.mark_present()
             return transcript, "Present marked."
        
        elif re.search(r"\babsent\b", transcript, re.IGNORECASE):
             self.attendance.mark_absent()
             return transcript, "Absent marked."
        
        else:
            return transcript, "I did not understand"