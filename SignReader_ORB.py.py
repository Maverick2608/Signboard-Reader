import numpy as np
import cv2
from matplotlib import pyplot as plt
from gtts import gTTS
from playsound import playsound
import os

img = cv2.imread('A:\VIT_Projects\EDI_TY_SEM1\CODE\stop.jpg',0)
cv2.imshow("Template",img)
cv2.waitKey(0)
cv2.destroyAllWindows
orb = cv2.ORB_create(nfeatures=2500)    #Initializing ORB and no of features
kp_img, des_img = orb.detectAndCompute(img, None)
img2 = cv2.drawKeypoints(img,kp_img,None,color=(0,255,0))
cv2.imshow("KP map",img2)
cv2.waitKey(0)
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

cap = cv2.VideoCapture(1)

def play_audio(audio):
    playsound(audio)

def convert_to_audio(text):
    my_audio=gTTS(text)
    path=text+".mp3"
    if not os.path.exists(path):
        my_audio.save(path)
    play_audio(path)

flagimg = 0
Nthreshold = 9
Dthreshold = 40
while(True):
    check, frame = cap.read()
    grayframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    kp_grayframe, des_grayframe = orb.detectAndCompute(grayframe, None)

    matches = bf.match(des_img,des_grayframe)
    nmatches = []
    for m in matches:
        if m.distance<Dthreshold:
            nmatches.append(m)
    dmatches = sorted(nmatches, key = lambda x:x.distance)
    prelim = cv2.drawMatches(img, kp_img, grayframe, kp_grayframe,dmatches[:15],grayframe,flags = 2) #testing
    cv2.imshow("Figure", prelim)

    if len(dmatches)>Nthreshold:
        convert_to_audio("Stop")

    key = cv2.waitKey(1)&0xFF
    if key == ord('q'):
        break
cv2.destroyAllWindows()
cap.release()
 