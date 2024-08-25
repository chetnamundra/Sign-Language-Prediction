#this code is to count the number of fingers pointed using opencv
import cv2 as cv
import mediapipe as mp
import math
from model import nearest

cap=cv.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

ls=['hello', 'goodbye', 'no', 'yes', 'thankyou', 'iloveyou', 'cant']

newl= [[1050.7623762376238, 2464.5643564356437], [995.8613861386139, 2040.1881188118812], [930.6435643564356, 1602.1881188118812], [1093.0891089108911, 486.05940594059405], [672.0693069306931, 2054.19801980198], [738.2673267326733, 2387.4455445544554]]

def preprocess(l):
    x , y = 0 , 0
    xin, yin = l[0][0], l[0][1]
    for i in range(len(l)):
        l[i][0]-=xin
        l[i][1]-=yin
        x+=abs(l[i][0])
        y+=abs(l[i][1])
    
    return [x,y]

def Nearest(p):
    min=99999999
    mini=0
    for i in range(len(newl)):
        x=distance (p, newl[i])
        if x<min:
            min=x
            mini=i
            
    return mini

def distance (x, y):
    return math.sqrt((x[0]-y[0])**2 + (x[1]-y[1])**2)

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
                        #print(g)
                        x,y=preprocess(g)
                        index = Nearest([x,y])
                        cv.putText(img, nearest(g), (20, 20), cv.FONT_HERSHEY_COMPLEX, 0.5, (255, 0, 0), 1)

                       
                mpDraw.draw_landmarks (img, handLms, mpHands. HAND_CONNECTIONS)
                
        
        cv.imshow("ok",img)
        cv.waitKey(1)

x=yes()
    
