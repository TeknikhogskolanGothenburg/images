import cv2
import numpy as np


def main():
    # Read original image
    img = cv2.imread('./img/house.jpg')
    # Convert image to gray scale
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Blur image
    img_blur = cv2.GaussianBlur(img, (7, 7), 2)
    # Edge detection
    img_canny1 = cv2.Canny(img_gray, 100, 200)

    # Dialate and erode
    kernel = np.ones((5, 5), np.uint8)
    img_dia = cv2.dilate(img_canny1, kernel, iterations=1)
    img_eroded = cv2.erode(img_dia, kernel, iterations=1)


    # print(img_gray.shape)

    # Show images
    cv2.imshow('Image', img)
    cv2.imshow('Gray Scale', img_gray)
    cv2.imshow('Blured Image', img_blur)
    cv2.imshow('Canny Image 1', img_canny1)
    cv2.imshow('Dialate Image', img_dia)
    cv2.imshow('Eroded Image', img_eroded)

    cv2.waitKey(0)


if __name__ == '__main__':
    main()
