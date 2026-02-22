import os, re
from dotenv import load_dotenv
from app.listener import Listener
from app.processor import Processor
from services.assignmentsheet import Assignments
from services.attendance import Attendance
from services.time import Time

# load stuff from env

load_dotenv()

access_key = os.getenv("ACCESS_KEY")
keyword_path = os.path.join(os.getcwd(), "wake-words", "start.ppn")
google_console_creds_path = os.getenv("GOOGLE_CONSOLE_CREDS")
test_sheet_id = os.getenv("TEST_SHEET")
assignments_sheet_id = os.getenv("ASSIGNMENTS_SHEET")
attendance_sheet_id = os.getenv("ATTENDANCE_SHEET")

# set variables

sample_rate = 16000
record_seconds = 3
silence_counter = 0
silence_threshold = 500

# instantiate the class methods

assignments = Assignments(creds_path = google_console_creds_path, sheetid = test_sheet_id)
attendance = Attendance(creds_path = google_console_creds_path, sheetid = attendance_sheet_id)
time = Time()
listener = Listener(access_key = access_key, keyword_path = keyword_path)
processor = Processor(access_key = access_key, assignments = assignments, attendance = attendance, time = time)

# main loop for continuous input

try:
    while True:
        # call listener class to listen for wake word
        listener.listen(sample_rate, record_seconds, silence_counter, silence_threshold, active_mode = False)

        # set session active and start listening for commands
        session_active = True
        while session_active:
            audio = listener.listen(sample_rate, record_seconds, silence_counter, silence_threshold, active_mode = True)
            energy = sum(sample**2 for sample in audio) / len(audio)

            if energy > 500:  
                text, result = processor.process(audio)
                print(text,"\n",result)

            if re.search(r"\b(stop|exit)\b", text, re.IGNORECASE):
                print("bye")
                session_active = False

except KeyboardInterrupt:
    print("tata")