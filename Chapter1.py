import cv2

# read the image with color in 1, gray scale 0
img = cv2.imread("/Users/kailiu/Documents/Dataset/Images/lena_256.jpg", 1)

print("Shape of the image:", img.shape)

# show image
cv2.imshow("Original Lena", img)
cv2.waitKey(0)

b = img.copy()
# set green and red channels to 0
b[:, :, 1] = 0
b[:, :, 2] = 0
# RGB - Blue
cv2.imshow('B-RGB', b)
cv2.waitKey(0)

g = img.copy()
# set blue and red channels to 0
g[:, :, 0] = 0
g[:, :, 2] = 0
# RGB - Green
cv2.imshow('G-RGB', g)
cv2.waitKey(0)

r = img.copy()
# set blue and green channels to 0
r[:, :, 0] = 0
r[:, :, 1] = 0
# RGB - Red
cv2.imshow('R-RGB', r)
cv2.waitKey(0)

# scaling
height, width = img.shape[:2]
# nearest neighbor
res1 = cv2.resize(img,(50*width, 50*height), interpolation=cv2.INTER_NEAREST)
cv2.imshow("Enlarged image by nearest neighbor", res1)
cv2.waitKey(0)
height1, width1 = res1.shape[:2]
rres1 = cv2.resize(res1, (int(width1/50), int(height1/50)), interpolation=cv2.INTER_NEAREST)
cv2.imshow("restored image by nearest neighbor", rres1)
cv2.waitKey(0)

# Bilinear
res2 = cv2.resize(img,(2*width, 2*height), interpolation=cv2.INTER_LINEAR)
cv2.imshow("Enlarged image by bilinear", res2)
cv2.waitKey(0)
height2, width2 = res2.shape[:2]
rres2 = cv2.resize(res1, (int(width2/2), int(height2/2)), interpolation=cv2.INTER_LINEAR)
cv2.imshow("restored image by bilinear", rres2)
cv2.waitKey(0)

# bicubic
res3 = cv2.resize(img,(2*width, 2*height), interpolation=cv2.INTER_CUBIC)
cv2.imshow("Enlarged image by bicubic", res3)
cv2.waitKey(0)
height3, width3 = res1.shape[:2]
rres3 = cv2.resize(res1, (int(width3/2), int(height3/2)), interpolation=cv2.INTER_CUBIC)
cv2.imshow("restored image by bicubic", rres3)
cv2.waitKey(0)

