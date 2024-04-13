import cv2
import random

def print_progress_bar(frame, frame_gauge, total, length=100):
    percent = min(100 * frame_gauge // total, 100)

    if  0 <= percent <= 20:
        color = (0, 0, 255)  
    elif 20 < percent <= 40:
        color = (0, 100, 100)  
    elif 40 < percent <= 60:
        color = (255, 200, 0)  
    elif 60 < percent <= 80:
        color = (0, 255, 255)  
    elif 80 < percent <= 100:
        color = (0, 255, 0)  

    filled_length = int(length * percent // 100)

    cv2.rectangle(frame, (frame.shape[1] - length - 10, 10), (frame.shape[1] - 10, 30), (255, 255, 255), -1)
    cv2.rectangle(frame, (frame.shape[1] - length - 10, 10), (frame.shape[1] - 10 - length + filled_length, 30), color, -1)

    cv2.putText(frame, f'{percent}%', (frame.shape[1] - length - 10, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)

    return frame

def nose(value):
    if value < 0.3:
        return 1
    else:
        return 1

def lefteye(value):
    if value < 0.3:
        return 1
    else:
        return 1 

def righteye(value):
    if value < 0.3:
        return 1
    else:
        return 1 

def rightear(value):
    if value < 0.3:
        return 1
    else:
        return 1 

def leftear(value):
    if value < 0.3:
        return 1
    else:
        return 1 

def leftshoulder(value):
    if value < 0.3:
        return 1
    else:
        return 1 

def rightshoulder(value):
    if value < 0.3:
        return 1
    else:
        return 1 

def leftelbow(value):
    if value < 0.3:
        return 1
    else:
        return 1 

def rightelbow(value):
    if value < 0.3:
        return 1
    else:
        return 1 

def leftwrist(value):
    if value < 0.3:
        return 1
    else:
        return 1 

def rightwrist(value):
    if value < 0.3:
        return 1
    else:
        return 1 

def lefthip(value):
    if value < 0.3:
        return 1
    else:
        return 1 

def righthip(value):
    if value < 0.3:
        return 1
    else:
        return 1 

def leftknee(value):
    if value < 0.3:
        return 1
    else:
        return 1 

def rightknee(value):
    if value < 0.3:
        return 1
    else:
        return 1 

def leftankle(value):
    if value < 0.3:
        return 1
    else:
        return 1 

def rightankle(value):
    if value < 0.3:
        return 1
    else:
        return 1 
