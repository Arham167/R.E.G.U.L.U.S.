import os
from dotenv import load_dotenv
from app.listener import Listener
from app.processor import Processor

load_dotenv()

access_key = os.getenv("ACCESS_KEY")
keyword_path = os.path.join(os.getcwd(), "assets", "start.ppn")

listener = Listener(access_key = access_key, keyword_path = keyword_path)
processor = Processor(access_key = access_key)
audio = listener.listen()
text = processor.process(audio = audio)
print(text[0])