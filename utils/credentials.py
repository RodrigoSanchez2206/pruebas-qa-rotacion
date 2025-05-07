from dotenv import load_dotenv
import os

load_dotenv()

def get_credentials():
    return os.getenv("user"), os.getenv("pass")
