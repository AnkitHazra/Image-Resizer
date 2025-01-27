import cv2

# Configurable Parameter
source = "D:/Image Resizer/mountain.jpg"
destination = 'newImage.png'
scale_percent = 50


src = cv2.imread(source, cv2.IMREAD_UNCHANGED)

width = int(src.shape[1] * scale_percent / 100)
height = int(src.shape[0] * scale_percent / 100)
dsize = (width, height)


output = cv2.resize(src, dsize)

cv2.imwrite(destination,output)
cv2.waitKey(0)

