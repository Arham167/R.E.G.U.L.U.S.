import datetime

class Time():
    def time(self):
        return datetime.datetime.now().time().strftime("%I:%M %p")
    
    def date(self):
        return datetime.datetime.today().strftime("%d-%b-%y")
    
    def day(self):
        return datetime.datetime.today().strftime("%A")