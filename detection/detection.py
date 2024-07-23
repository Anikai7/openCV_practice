import cv2 as cv

win_name = "Face"

vid_capture = cv.VideoCapture(0)

face_cascade = cv.CascadeClassifier("haarcascade_frontalface_default.xml")

def face_detect(face):
    for (x,y,w,h) in face:
        cv.rectangle(frame, (x,y), (x+w,y+h),(155, 155, 155), 4,cv.LINE_AA)

while True:
    has_frame,frame = vid_capture.read()
    face = face_cascade.detectMultiScale(frame)
    face_detect(face)
    key = cv.waitKey(1)
    if key == ord('q'):
        break
       
    cv.imshow(win_name,frame)