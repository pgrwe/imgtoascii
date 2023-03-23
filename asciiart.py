import cv2
import numpy

image = cv2.imread("smash4logo.jpg")
image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
image = cv2.resize(image,(116,120))
cv2.imshow("smash",image)
cv2.waitKey(0)
# 17 chars for shading
charlist = [' ', '.', "'", ',', ':', ';', 'c', 'l', 'x', 'o', 'k', 'X', 'd', 'O', '0', 'K', 'N']
for y in range(image.shape[0]):
    for x in range(image.shape[1]):
        pixelColor = image[y][x].astype(float)
        pixelNum = round(pixelColor/17)
        print(charlist[pixelNum],end="")
    print()
