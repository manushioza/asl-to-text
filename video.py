import numpy as py 
import cv2 as cv 
import mediapipe as mp 

mp_hands=mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
# 0 = Camerea
video = cv.VideoCapture(0)

#Exit if camaera not detected/opened
if not video.isOpened():
    print("Cannot Open Camera!")
    exit()

#Read Video
while True:
    #Capture Frame 
    #TODO Change frame rate
    ret, frame = video.read()
    #ret = bool T/F if video is read
    if not ret: 
        print("Cannot recieve frame!")
        break
    
    #OpenCV uses BGR -> to use Mediapipe have to convert from BGR to RGB
    frame = cv.cvtColor(frame,cv.COLOR_BGR2RGB)
    cv.flip(frame,1)
    hands = mp_hands.Hands().process(frame)

    #Concert back to BGR from RGB to use with opencv
    frame = cv.cvtColor(frame, cv.COLOR_RGB2BGR)
    #If hands have been detected
    if hands.multi_hand_landmarks:
        for hand in hands.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand, connections=mp_hands.HAND_CONNECTIONS)

    #Use opencv to covert fram to BGR
    display = cv.cvtColor(frame, cv.COLOR_BGR2BGRA)

    #Open GUI to display
    cv.imshow('ASL TO TEXT', display)
    #Exit program if key pressed
    if cv.waitKey(1) == ord('q'):
        break

#Exit
video.release()
cv.destroyAllWindows()

