import time

import cv2


def image_processing():
    img = cv2.imread('img_test.jpg')
    #cv2.imshow('image', img)
    w, h = img.shape[:2]
    #(cX, cY) = (w // 2, h // 2)
    #M = cv2.getRotationMatrix2D((cX, cY), 45, 1.0)
    #rotated = cv2.warpAffine(img, M, (w, h))
    #cv2.imshow('rotated', rotated)

    #cat = img[250:580, 20:280]
    #cv2.imshow('image', cat)

    #r = cv2.selectROI(img)
    #image_cropped = img[int(r[1]):int(r[1] + r[3]), int(r[0]):int(r[0] + r[2])]
    #cv2.imshow('cropped', image_cropped)

    cv2.line(img, (0, 0), (580, 600), (255, 0, 0), 5)
    cv2.rectangle(img, (384, 10), (580, 128), (0, 252, 0), 3)
    cv2.putText(img, 'Lab. No 8', (10, 500), cv2.FONT_HERSHEY_SIMPLEX, 3,
                (0, 0, 255), 2, cv2.LINE_AA)
    cv2.imshow('img', img)


def video_processing():
    cap = cv2.VideoCapture(1)
    down_points = (640, 480)
    i = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.resize(frame, down_points, interpolation=cv2.INTER_LINEAR)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)
        ret, thresh = cv2.threshold(gray, 110, 255, cv2.THRESH_BINARY_INV)

        contours, hierarchy = cv2.findContours(thresh,
                            cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        if len(contours) > 0:
            c = max(contours, key=cv2.contourArea)
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            if i % 5 == 0:
                a = x + (w // 2)
                b = y + (h // 2)
                print(a, b)

        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        time.sleep(0.1)
        i += 1

    cap.release()


if __name__ == '__main__':
    #image_processing()
    video_processing()

cv2.waitKey(0)
cv2.destroyAllWindows()