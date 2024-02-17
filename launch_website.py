import os
from dotenv import load_dotenv
load_dotenv()

url = os.getenv('URL')

print(f"The Google URL is: {url}")