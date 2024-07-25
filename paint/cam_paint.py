import cv2 as cv
import numpy as np

cam = cv.VideoCapture(0)
cv.namedWindow("paint", cv.WINDOW_NORMAL)  # Use the named window
flag = False
ix=-1
iy=-1

white_background = np.zeros((400,400,3))+255

def button(frame):
    cv.rectangle(frame, (100, 50), (540, 150), (255, 0, 0), 3, cv.LINE_4)
    cv.putText(frame, "Blue", (270, 100), cv.FONT_HERSHEY_PLAIN, 4, (255, 0, 0), 3, cv.LINE_4)

def onMouse(event, x, y, flags, param):
    global flag,white_background,ix,iy
    if event == cv.EVENT_LBUTTONDOWN:
        if 540 > x > 100 and 150 > y > 50:
            flag = not flag  # Toggle flag when clicking inside the button area
            print(f'Left button down at ({x}, {y})')

    elif event == cv.EVENT_MOUSEMOVE:
        if flag:  # Only draw if flag is True
            print(f'Mouse moved to ({x}, {y})')
            if ix and iy == -1:
                ix=x
                iy=y
            cv.line(white_background,(ix,iy),(x,y),(0,0,255),10)
            ix=x
            iy=y

while True:
    has_frame, frame = cam.read()

    button(frame)  # Draw the button on the frame
    cv.setMouseCallback('paint', onMouse)  # Set mouse callback on the named window

    key = cv.waitKey(1)
    
    if not has_frame:
        break

    cv.imshow('paint', frame)
    cv.imshow('paint_background',white_background)

    if key == ord('q'):
        break

cam.release()
cv.destroyAllWindows()

