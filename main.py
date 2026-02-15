import os
from dotenv import load_dotenv
from app.listener import Listener

load_dotenv()
listener = Listener()

access_key = os.getenv("ACCESS_KEY")
keyword_path = os.path.join(os.getcwd(), "assets", "start.ppn")

listener.create(access_key = access_key, keyword_path = keyword_path)