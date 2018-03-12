import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('/media/rohitkumar/Rohit-Sonu/python3/projects/Face_Recognition/haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in face:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    cv2.imshow('img', img)

    # 27 is for ESC key
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()