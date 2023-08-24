import cv2 
img = cv2.imread('poster.jpg')
rocket = img[120:360,400:500]
img[0:240,500:600] = rocket
text = 'I love coding at Byjus future school.'
cv2.putText(img,
            text,
            (20,220),
            fontFace= cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale= 1,
            colour = {0,0,255})
cv2.imshow("output",img)
cv2.waitkey(0)
