# Note that in case you are NOT using the English client, you will need to upload a screenshot of the
# accept button in your language and provide the URL of the uploaded screenshot below, OR you can 
# keep it saved on your PC and provide the full path to the screenshot in PICTURE below.

# Import pyautogui to search for images ("Accept" button) and control the mouse to click it.
import pyautogui as pg

from datetime import datetime
import time

import requests
from PIL import Image
from io import BytesIO

PICTURE = r''
URL = 'https://i.imgur.com/093Oe8v.png'

if PICTURE == r'':
    response = requests.get(URL)
    PICTURE = BytesIO(response)

img = Image.open(PICTURE)

pos = None
print("LOCATING ...")

while True:
    time.sleep(3)
    pos = pg.locateCenterOnScreen(img,confidence = 0.7)
    if pos != None:
        pg.moveTo(pos)
        pg.click()
        
        print(' ')
        print("\nQueue Accepted!")
        print('Timestamp:',datetime.now().time())
        pos = None
        
