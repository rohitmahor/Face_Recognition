import numpy as np
import cv2
import matplotlib.pyplot as plt

# on webcam
webcam = cv2.VideoCapture(0)

# read frame
ret, frame = webcam.read()
webcam.release()

if ret:
    # used to save an image
    cv2.imwrite('face.png', frame)

# start a window
cv2.startWindowThread()

# create a window holder to show the image
cv2.namedWindow("Face", cv2.WINDOW_NORMAL)
cv2.imshow("Face", frame)

# Press any key to close external window
cv2.waitKey()
cv2.destroyAllWindows()



# first u need to convert scheme from BGR to RGB
frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
plt.imshow(frame)
plt.show()

# Read image from directory
plt.imshow(frame)
frame = cv2.imread('/media/rohitkumar/Rohit-Sonu/python3/projects/my_face.png', 1)
cv2.imshow("Face", frame)
cv2.waitKey()
cv2.destroyAllWindows()