import os
from dotenv import load_dotenv
from app.listener import Listener
from app.processor import Processor
from services.assignmentsheet import Assignments

# load stuff from env

load_dotenv()

access_key = os.getenv("ACCESS_KEY")
keyword_path = os.path.join(os.getcwd(), "wake-words", "start.ppn")
google_console_creds_path = os.getenv("GOOGLE_CONSOLE_CREDS")
test_sheet_id = os.getenv("TEST_SHEET")
assignments_sheet_id = os.getenv("ASSIGNMENTS_SHEET")

assignments = Assignments(creds_path = google_console_creds_path, sheetid = test_sheet_id)
listener = Listener(access_key = access_key, keyword_path = keyword_path)
processor = Processor(access_key = access_key, assignments = assignments)
audio = listener.listen()
text, result = processor.process(audio = audio)
print(text, "\n", result)