import numpy as py 
import cv2 as cv 

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

