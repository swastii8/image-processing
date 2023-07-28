import cv2
import numpy as np
img_path="./sherlock_kid.png"
img=cv2.imread(img_path)
print(img.shape)
cv2.imshow("Image",img)

cv2.waitKey(2000)
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2LAB)
cv2.imshow("Image",img)
cv2.imshow("Image",img)
cv2.imshow("Gray Image",img_gray)
cv2.imwrite("./sherlock_kid_gray.png",img_gray)
print(img_gray.shape)
img_resized=cv2.resize(img,(500,500))
cv2.imshow("resized image",img_resized)
#h,w,c=img.shape
#img_cropped=img[:,w/2:]
#cv2.imshow("resized image",img_cropped)
img_cropped=img[:,300:]
cv2.imshow("resized image",img_cropped)

img_shape=img.shape
img_white=np.full(img_shape,255,dtype=np.uint8)
cv2.imshow("white Image",img_white)
img_neg=np.subtract(img_white,img)
cv2.imshow("negative",img_neg)
cv2.waitKey(0)
cv2.destroyAllWindows()
