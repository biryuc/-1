## [imports]
import cv2 as cv
import sys
## [imports]
## [imread]
img = cv.imread(cv.samples.findFile("vm3.jpg"))
## [imread]
## [empty]
if img is None:
    sys.exit("Could not read the image.")
## [empty]
## [imshow]
cv.imshow("Display window", img)
k = cv.waitKey(0)
## [imshow]
## [imsave]
if k == ord("s"):
    cv.imwrite("vm3.jpg", img)
## [imsave]