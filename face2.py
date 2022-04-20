import cv2
from join_images import stack_images


def main():
    cap = cv2.VideoCapture(1)
    face_cascade = cv2.CascadeClassifier('./haarcascades/haarcascade_frontalface_default.xml')

    while True:
        _, img = cap.read()
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img_canny = cv2.Canny(img_gray, 150, 200)

        faces = face_cascade.detectMultiScale(img_gray, 1.15, 6)
        for x, y, w, h in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

        stack = stack_images(0.5, ([img, img_gray, img_canny]))
        cv2.imshow('Video', stack)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


if __name__ == '__main__':
    main()
