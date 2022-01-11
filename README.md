# LoLAutoMatchAccept
A python script that accepts League of Legends matches using pyautogui and openCV modules

# Usage
Start the queue, then launch the script. The CMD will pop up to indicate a successful launch, and a message will be displayed when the match is accepted along with a timestamp.

# Languages other than English
The script uses an uploaded screenshot of the accept button in English. If you use a different language for the client, you can take the screenshot yourself and upload the image online and put the URL 
inside the script OR you can save it locally on your PC and provide the full path to the screenshot. The script will protrize paths over URLs.

# Modules needed
The script uses pyautogui, openCV, requests, PIL, io, datetime and time. You will need to install the first 3, you probably won't need to install the others as they are installed alongside Python by default.

# Detailed Description
The script is written in Python. It uses pyautogui module to find the screenshot on the screen and control the mouse to click its center. OpenCV is needed by pyautogui to be able to use the "confidence" 
parameter. Confidence parameter, which takes values between 0 and 1, makes sure that the script will identify the screenshot even if the button on screen is different from the screenshot. Some of these differences include:
- If the mouse is on the center of the button
- If the user uses a wider screenshot where some features, like the loading bar or ranked banner, can change over time or from user to user.

Setting the confidence to a much higher value can cause the script to not be able to locate the button in some cases, like those mentioned above. However, setting the confidence to a much lower value
can cause bugs, for example, it can cause the script to keep clicking on the accept button even after it turns grey after the first click. 
The locating is placed inside an infinite loop. In case someone dodges the champ select and you are returned to the queue, the script will accept the other matches too. When a queue is accepted a message
is displayed in the CMD alongside a timestamp to show how long the queue was and how many queues were accepted.
A sleep timer is used to avoid unnecessary CPU consumption.
Changing the sleep timer and slightly changing the confidence should be safe.

