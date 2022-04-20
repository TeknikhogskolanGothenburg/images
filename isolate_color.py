import cv2
import numpy as np

from join_images import stack_images


def main():
    img = cv2.imread('./img/house.jpg')
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    cv2.namedWindow('Trackbars')
    cv2.resizeWindow('Trackbars', 640, 240)
    cv2.createTrackbar('Hue Min', 'Trackbars', 83, 179, lambda x: 0)
    cv2.createTrackbar('Hue Max', 'Trackbars', 142, 179, lambda x: 0)
    cv2.createTrackbar('Sat Min', 'Trackbars', 73, 255, lambda x: 0)
    cv2.createTrackbar('Sat Max', 'Trackbars', 255, 255, lambda x: 0)
    cv2.createTrackbar('Val Min', 'Trackbars', 162, 255, lambda x: 0)
    cv2.createTrackbar('Val Max', 'Trackbars', 255, 255, lambda x: 0)

    while True:
        hue_min = cv2.getTrackbarPos('Hue Min', 'Trackbars')
        hue_max = cv2.getTrackbarPos('Hue Max', 'Trackbars')
        sat_min = cv2.getTrackbarPos('Sat Min', 'Trackbars')
        sat_max = cv2.getTrackbarPos('Sat Max', 'Trackbars')
        val_min = cv2.getTrackbarPos('Val Min', 'Trackbars')
        val_max = cv2.getTrackbarPos('Val Max', 'Trackbars')

        lower_limit = np.array([hue_min, sat_min, val_min])
        upper_limit = np.array([hue_max, sat_max, val_max])
        mask = cv2.inRange(img_hsv, lower_limit, upper_limit)

        masked_img = cv2.bitwise_and(img, img, mask=mask)
        image_stack = stack_images(0.5, ([img_hsv], [mask], [masked_img]))
        cv2.imshow('images', image_stack)
        # cv2.imshow('Image', img_hsv)
        # cv2.imshow('Masked', mask)
        # cv2.imshow('Masked Original', masked_img)

        cv2.waitKey(1)


if __name__ == '__main__':
    main()
