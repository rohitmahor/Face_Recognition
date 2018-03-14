# Face Recognition using openCV

Recognize faces using python and openCV library.
OpenCV has three built in face recognizers.
1. EigenFaces Face Recognizer Recognizer - cv2.face.EigenFaceRecognizer_create()
2. FisherFaces Face Recognizer Recognizer - cv2.face.FisherFaceRecognizer_create()
3. Local Binary Patterns Histograms (LBPH) Face Recognizer - cv2.face.LBPHFaceRecognizer_create()

## Required libraries
1. numpy
2. os
3. cv2
4. matplotlib

## Steps for preprocessing of image.
1. Cut the extra unneccessary part of images 
2. Normalization
3. Resize
4. Alignment

## Use LBPH model to predict faces
LBPH model takes a 3x3 window and move it on one image, at each move, It compares centre pixel intensity with its neighbour if
neighbour's pixels intensity is less than or equal to centre pixel it's denoted by 0 otherwise it's denoted by 1. Then read 
the 0/1 in clockwise order from window and convert it from binary to decimal. This process is repeated for whole image and we 
get a list of decimal values for different face's areas and create a histogram using these decimal values. 
Model creates a different histogram for different faces. LBPH algorithm also keeps track of which histogram belongs to which 
person.

## 
