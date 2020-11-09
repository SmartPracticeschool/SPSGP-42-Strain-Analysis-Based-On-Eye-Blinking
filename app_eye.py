#importing necessary libraries(TSK-572)
from imutils.video import FileVideoStream
from imutils.video import VideoStream
from imutils import face_utils
import numpy as np
import argparse
import imutils
import time
import dlib
import cv2
import datetime
from gtts import gTTS
import tkinter as tk
from tkinter import ttk
from playsound import playsound
from scipy.spatial import distance as dist


#Defining Necessary Functions(TSK-573)
def playaudio(text):
    speech = gTTS(text)
    print(type(speech))
    speech.save("../output1.mp3")
    playsound("../output1.mp3")
    return

LARGE_FONT = ("Verdana",12)
NORM_FONT = ("Helvetica",10)
SMALL_FONT = ("Helvetica",8)

def popupmssg(msg):
    popup = tk.Tk()
    popup.wm_title("Urgent")
    style = ttk.Style(popup)
    style.theme_use("Classic")
    style.configure('Test.TLabel',background = 'aqua')
    label = ttk.Label(popup,txt=msg,style = 'Test.TLabel')
    label.pack(side='top',fill='x',pady=10)
    B1 = ttk.Button(popup,text='Okay',command=popup.destroy)
    B1.pack()
    popup.mainloop()

def eye_aspect_ratio(eye):
    A = dist.euclidean(eye[1], eye[5])
    B = dist.euclidean(eye[2], eye[4])
    C = dist.euclidean(eye[0], eye[3])
    ear = (A + B) / (2.0 * C)
    return ear

#constructing parser(TSK-574)
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--shape-predictor",required=True,help="path to facial landmark predictor")
#ap.add_argument("-v","--video",type=str,default="",help="path to input video file")
args = vars(ap.parse_args())


#defining important constants(TSK-575)
EYE_AR_THRESH = 0.3
EYE_AR_CONSEC_FRAMES = 3

COUNTER = 0
TOTAL = 0




