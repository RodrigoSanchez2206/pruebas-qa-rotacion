from dotenv import load_dotenv
import os

load_dotenv()

def get_credentials():
    return os.getenv("SF_USERNAME"), os.getenv("SF_PASSWORD")
