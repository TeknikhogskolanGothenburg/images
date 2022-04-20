import cv2
import numpy as np

def main():
    img = cv2.imread('./img/cards.jpg')

    width = 323
    height = 461
    points1 = np.float32([[457, 121], [897, 223], [727, 859], [293, 743]])
    points2 = np.float32([[0, 0], [width, 0], [width, height], [0, height]])
    matrix = cv2.getPerspectiveTransform(points1, points2)
    img_warped = cv2.warpPerspective(img, matrix, (width, height))

    cv2.imshow('Card', img_warped)
    cv2.waitKey(0)


if __name__ == '__main__':
    main()
