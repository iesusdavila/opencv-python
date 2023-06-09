import cv2 as cv
import numpy as np

img = cv.imread('../Resources/Photos/park.jpg')
cv.imshow('Parque', img)


# Traslacion
def translate(img, x, y):
    transMat = np.float32([[1, 0.5, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

translated = translate(img, -100, -100)
cv.imshow('Translated', translated)

# Rotacion
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width // 2, height // 2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, -45)
cv.imshow('Rotacion', rotated)

rotated_rotated = rotate(img, -90)
cv.imshow('Doble Rotacion', rotated_rotated)

# Redimensionamiento
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
print(resized.shape)
cv.imshow('Resized', resized)

# Voltear
flip = cv.flip(img, -1)
cv.imshow('Flip', flip)

# Recortar
cropped = img[200:400, 300:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)