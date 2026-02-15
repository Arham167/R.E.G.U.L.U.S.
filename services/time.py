import datetime

class Time():
    def __init__(self):
        self.time()
        self.date()

    def time(self):
        return datetime.datetime.now().time().strftime("%I:%M %p")
    
    def date(self):
        return datetime.datetime.today().strftime("%b %d, %Y")
    
