import cv2
import tkinter as tk
from tkinter import Button
import mediapipe as mp
import speech_recognition as sr
import pyautogui
import numpy as np
import math
from gtts import gTTS
import os
from playsound import playsound
from voicer import chat
import time
from datetime import datetime, timedelta

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, max_num_hands=1)
LMS = mp_hands.HandLandmark
screen_width, screen_height = pyautogui.size()

def count_fingers(hand_landmarks):
    finger_tip_ids = [4, 8, 12, 16, 20]
    finger_count = 0

    for finger_tip_id in finger_tip_ids:
        tip_x, tip_y = hand_landmarks.landmark[finger_tip_id].x, hand_landmarks.landmark[finger_tip_id].y

        if tip_y < hand_landmarks.landmark[finger_tip_id - 2].y:
            finger_count += 1

    return finger_count

rightx=0
righty=0

def get_click(hand_landmarks,image,h,w):
        global rightx,righty
        lm = hand_landmarks.landmark

        x,y = int(lm[LMS.INDEX_FINGER_TIP].x*w), int(lm[LMS.INDEX_FINGER_TIP].y*h)
        cv2.circle(image,(x,y),20,(0, 255, 0),cv2.FILLED)

        x,y = int(lm[LMS.INDEX_FINGER_MCP].x*screen_width), int(lm[LMS.INDEX_FINGER_MCP].y*screen_height)
        pyautogui.moveTo(screen_width-x,y)

        thumb = np.array([lm[LMS.THUMB_TIP].x,        lm[LMS.THUMB_TIP].y])
        index = np.array([lm[LMS.INDEX_FINGER_TIP].x, lm[LMS.INDEX_FINGER_TIP].y])
        wrist = np.array([lm[LMS.WRIST].x,            lm[LMS.WRIST].y])

        indexLength = np.linalg.norm(index - wrist)
        thumbLength = np.linalg.norm(thumb - wrist)
        maxDistance = 0.7 * math.hypot(indexLength, thumbLength)

        length = np.linalg.norm(index - thumb)
        if length < 0.05:
            pyautogui.click(screen_width-x,y)
            rightx=screen_width-x
            righty=y

def auto_scroll(hand_landmarks,image,h,w):
    lm = hand_landmarks.landmark
    x,y = int(lm[LMS.MIDDLE_FINGER_TIP].x*w), int(lm[LMS.MIDDLE_FINGER_TIP].y*h)
    cv2.circle(image,(x,y),20,(0, 255, 0),cv2.FILLED)
    if y < 100:
        pyautogui.scroll(-10)
    elif y > 300:
        pyautogui.scroll(10)

def speak(text):
    tts = gTTS(text=text,lang="en",tld="co.uk")  
    tts.save("voice.mp3")
    playsound("voice.mp3")
    os.remove("voice.mp3")

def commands(tag,got):
    speak(got)
    if "task" in tag:
        if "1" in tag:
            pyautogui.hotkey('win', '1')
        if "2" in tag:
            pyautogui.hotkey('win', '2')
        if "3" in tag:
            pyautogui.hotkey('win', '3')
        if "4" in tag:
            pyautogui.hotkey('win', '4')
    elif "opt" in tag:
        pass
    else:
        os.system(tag)

timer=0

def start_camera():
    global cap, root, timer
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    timer=datetime.now()+timedelta(hours=1)
    update_frame()

def pause_camera():
    global cap
    if cap.isOpened():
        cap.release()

def stop_camera():
    global cap
    if cap.isOpened():
        cap.release()
    cv2.destroyAllWindows()

audio=""
assistant = False
def update_frame():
    global cap, root, audio, assistant, timer
    if timer < datetime.now():
        stop_camera()
        speak("Cooldown")
        return
    ret, frame = cap.read()
    if not ret:
        return
    h,w,c=frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)
    finger_count = 0
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp.solutions.drawing_utils.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            finger_count = count_fingers(hand_landmarks)

            if finger_count ==2:
                get_click(hand_landmarks,frame,h,w)
            elif finger_count == 3:
                auto_scroll(hand_landmarks,frame,h,w)
            elif finger_count == 4:
                recognizer = sr.Recognizer()
                timeout_duration = 5

                with sr.Microphone() as source:
                    print("Say something: ")
                    try:
                        audio = recognizer.listen(source, timeout=timeout_duration)
                    except sr.WaitTimeoutError:
                        print("No speech detected")

                try:
                    text = recognizer.recognize_google(audio)
                    print("You said:", text)
                    if text =="assistant":
                        speak("Assistant mode activated")
                        time.sleep(2)
                        assistant = True
                    elif text == "right click":
                        pyautogui.rightClick(rightx,righty)
                    elif text == "exit":
                        speak("Assistant mode deactivated")
                        assistant = False
                    elif assistant==False:
                        time.sleep(2)
                        pyautogui.typewrite(text)
                    if assistant and text != "assistant" and text != "exit":
                        got,tag = chat(text)
                        print(got,tag)
                        commands(tag,got)
                except sr.UnknownValueError:
                    print("Sorry, could not understand audio.")
                except sr.RequestError as e:
                    print("Error fetching results; {0}".format(e))
                except Exception as e:
                    print(e)
    frame = cv2.flip(frame, 1)
    cv2.putText(frame, f'Fingers: {finger_count}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
    cv2.imshow('Hand Tracking', frame)
    if cap.isOpened():
        root.after(10, update_frame)

root = tk.Tk()
root.title("Hand Tracking")
root.geometry("400x200")  

frame_buttons = tk.Frame(root)
frame_buttons.pack()

start_button = Button(frame_buttons, text="Start", command=start_camera)
start_button.pack(side=tk.LEFT, padx=10, pady=10)

pause_button = Button(frame_buttons, text="Pause", command=pause_camera)
pause_button.pack(side=tk.LEFT, padx=10, pady=10)

stop_button = Button(frame_buttons, text="Stop", command=stop_camera)
stop_button.pack(side=tk.LEFT, padx=10, pady=10)

# Center the frame containing the buttons
frame_buttons.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

root.mainloop()