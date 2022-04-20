import cv2
import numpy as np
from join_images import stack_images


def get_contours(img, img_contour):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for contour in contours:
        area = cv2.contourArea(contour)
        cv2.drawContours(img_contour, contour, -1, (255, 0, 0), 3)
        arc_length = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, arc_length * 0.02, True)
        obj_corners = len(approx)
        x, y, w, h = cv2.boundingRect(approx)
        cv2.rectangle(img_contour, (x, y), (x+w, y+h), (0, 255, 0), 2)

        if obj_corners == 3:
            object_type = 'Triangle'
        elif obj_corners == 4:
            asp_ratio = w / float(h)
            if 0.98 < asp_ratio < 1.03:
                object_type = 'Square'
            else:
                object_type = 'Rectangle'
        else:
            print(obj_corners)
            object_type = 'Circle'

        cv2.putText(img_contour, object_type, (x + (w // 2) - len(object_type)*4, y-10), cv2.FONT_HERSHEY_COMPLEX, 0.5,
                    (0, 0, 0), 1)


def main():
    img = cv2.imread('./img/shapes2.png')
    img_blank = np.zeros_like(img)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_blur = cv2.GaussianBlur(img_gray, (7, 7), 0.5)
    img_canny = cv2.Canny(img_blur, 50, 50)

    img_contour = img.copy()

    get_contours(img_canny, img_contour)

    img_stack = stack_images(0.5, ([img, img_gray, img_blur],
                                   [img_canny, img_contour, img_blank]))

    cv2.imshow('images', img_stack)

    cv2.waitKey(0)

if __name__ == '__main__':
    main()
