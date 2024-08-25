#this code is to count the number of fingers pointed using opencv
import cv2 as cv
import mediapipe as mp
import math

cap=cv.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

def nearest(p):

    if p[8][1]<p[6][1] and p[20][1]<p[17][1] and p[12][1]>p[10][1] and p[16][1]>p[14][1]:
        return 'I Love You'
    elif p[8][1]<p[6][1] and p[20][1]<p[17][1] and p[12][1]<p[10][1] and p[16][1]<p[14][1]:
            if p[4][0]<p[17][0]:
                return 'Hello'
            else:
                return 'Thank You'
    else:
        
        if p[4][1]>p[0][1] and p[13][0]>p[1][0]:
            return 'Yes'
        elif p[4][1]>p[0][1] and p[13][0]<p[1][0]:
                return 'No'
        elif p[13][0]<p[1][0] and p[4][1]<p[0][1]:
            return 'Yes'
        elif p[20][0]<p[18][0] and p[16][0]<p[14][0]:
                return 'Good Bye'
        elif p[20][0]>p[18][0] and p[16][0]>p[14][0]:
                return 'No'
        return ''
    

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
    
                        cv.putText(img, nearest(g), (20, 20), cv.FONT_HERSHEY_COMPLEX, 0.5, (255, 0, 0), 1)

                       
                mpDraw.draw_landmarks (img, handLms, mpHands. HAND_CONNECTIONS)
                
        
        cv.imshow("ok",img)
        cv.waitKey(1)

x=yes()
    
