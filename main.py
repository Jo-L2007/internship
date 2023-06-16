import numpy as np
import cv2

image = cv2.imread("F:\Personal\Internship\week_2\day5\image2.jpg", 0)

output = cv2.imread("F:\Personal\Internship\week_2\day5\image2.jpg", 1)
cv2.imshow("Original image", image)
cv2.waitKey()

blurred = cv2.GaussianBlur(image, (11, 11), 0)
cv2.imshow("Blurred image", blurred)
cv2.waitKey()
setItem=set()
previous=0;
minR=4
for maxR in range(9,300,9):
    circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, 1, 100,
                             param1=100,param2=100,minRadius=minR,maxRadius=maxR)
    minR+=8
    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")

        for (x, y, r) in circles:
            cv2.circle(output, (x, y), r, (0,255,0), 1)
            setItem.add(r)

lst=sorted(setItem)
print("Length of List =", len(lst))
for item in lst:
    print(item)

cv2.imshow("Detections",output)
cv2.imwrite("CirclesDetection.jpg",output)
cv2.waitKey()