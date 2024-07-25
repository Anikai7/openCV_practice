import cv2 as cv
import numpy as np


drawing = False # true if mouse is pressed
mode = True # if True, draw rectangle. Press 'm' to toggle to curve
ix,iy = -1,-1

# mouse callback function
def draw_circle(event,x,y,flags,param):
    global ix,iy,drawing,mode
    if event == cv.EVENT_LBUTTONDOWN:
     drawing = True
     ix,iy = x,y
    elif event == cv.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                cv.rectangle(paintWindow,(ix,iy),(x,y),(0,255,0),-1)
        else:
            cv.circle(paintWindow,(x,y),5,(0,0,255),-1)
    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv.rectangle(paintWindow,(ix,iy),(x,y),(0,255,0),-1)
        else:
            cv.circle(paintWindow,(x,y),5,(0,0,255),-1)


cap = cv.VideoCapture(0)

# Load the image
pic = cv.imread("chill_kr.png")
if pic is None:
    print("Error: Image not loaded properly. Make sure 'chill_kr.png' exists.")
    exit()

# Create a window for displaying frames
win_name = "chill kr"
win = cv.namedWindow(win_name, cv.WINDOW_NORMAL)
paintWindow = np.zeros((471,636,3))  + 255 

def image():
    while True:
        key = cv.waitKey(1)

        if key == ord('q'):
            exit()
        elif key == ord('v'):
            video()
        elif key == ord('w'):
            board()
    
        cv.imshow(win_name, pic)

def video():
    while True:
        key = cv.waitKey(1)

        if key == ord('q'):
            exit()
        elif key == ord('c'):
            image()
        elif key == ord('w'):
            board()

        has_frame, frame = cap.read()

        if not has_frame:
            print("Error: Could not read frame.")
            break

        cv.imshow(win_name, frame)

def board():
    while True:
        key = cv.waitKey(1)

        if key == ord('q'):
            exit()
        elif key == ord('c'):
            image()
        elif key == ord('v'):
            video()

        cv.imshow(win_name, paintWindow)
        cv.setMouseCallback(win_name,draw_circle)


while True:
    key = cv.waitKey(1) & 0xFF

    if key == ord('q'):
        break
    elif key == ord('c'):
        print("Displaying image...")
        image()
    elif key == ord('v'):
        print("Displaying Video...")
        video()
    elif key ==ord('w'):
        print("Displaying white board")
        board()

cap.release()
cv.destroyAllWindows()