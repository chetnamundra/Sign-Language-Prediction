#this code is to count the number of fingers pointed using opencv
import cv2 as cv
import mediapipe as mp
import math
from model import nearest

cap=cv.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

dataset=[]

def yes():
    while True:
        success, img = cap.read()
        img=cv.flip(img,1)
        i1 = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        results = hands.process(i1)
        
        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                g=[]
                for id, lm in enumerate(handLms.landmark):
                    h, w, c = img.shape
                    cx, cy= int(lm.x*w), int(lm.y*h)
                    
                    g.append([cx,cy])
                    cv.putText(img, str(id), (cx, cy),cv.FONT_HERSHEY_COMPLEX, 0.5, 0, 1)
                    if len(g)==21:
                        dataset.append(g)
                        print(g)
                        if len(dataset)==50:
                            return
                        

                       
                mpDraw.draw_landmarks (img, handLms, mpHands. HAND_CONNECTIONS)
                
        
        cv.imshow("ok",img)
        cv.waitKey(1)


x=yes()
print(dataset)
    
