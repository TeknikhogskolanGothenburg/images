import cv2
import numpy as np


def change_some_pixels():
    img = np.zeros((500, 600, 3), np.uint8)
    for i in range(10, 501, 20):
        img[i:i+10] = 157, 168, 0
    cv2.imshow('Image', img)

    cv2.waitKey(0)


def draw_lines():
    img = np.zeros((500, 600, 3), np.uint8)
    height, width, _ = img.shape
    cv2.line(img, (0, 0), (width, height), (255, 0, 0), 3)

    cv2.imshow('Image', img)
    cv2.waitKey(0)


def draw_rectangles():
    img = np.zeros((500, 600, 3), np.uint8)
    cv2.rectangle(img, (200, 200), (400, 450), (255, 0, 0), cv2.FILLED)
    cv2.rectangle(img, (100, 100), (300, 300), (0, 0, 255), 3)

    cv2.imshow('Image', img)
    cv2.waitKey(0)


def draw_circles():
    img = np.zeros((500, 600, 3), np.uint8)
    cv2.circle(img, (100, 150), 30, (0, 0, 255), 3)
    cv2.circle(img, (200, 250), 50, (255, 0, 0), cv2.FILLED)

    cv2.imshow('Image', img)
    cv2.waitKey(0)


def draw_text():
    img = np.zeros((500, 600, 3), np.uint8)
    cv2.putText(img, 'This is my text', (200, 200), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)

    cv2.imshow('Image', img)
    cv2.waitKey(0)


def main():
    draw_text()


if __name__ == '__main__':
    main()
