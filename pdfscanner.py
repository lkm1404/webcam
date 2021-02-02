import cv2
import os
from fpdf import FPDF

url = 'http://192.168.43.1:8080/video'
cap = cv2.VideoCapture(url)
ret = True
f1 = 0
i = 0
while ret:
    ret, frame = cap.read()
    if f1 == 0:
        print("press s to scan the document")
        f1 = f1 + 1
    cv2.imshow('frame', frame)
    k = cv2.waitKey(1)
    if k == ord('s'):
        cv2.destroyWindow('frame')
        cv2.imshow("scanned photo", frame)
        print('Press u of the image is unreadable')
        print('Press b to convert the image into black and white ')
        print('Press c to obtain the cannied image of the scanned photo')
        print('If you want the section of the image to be excluded in pdf press y')
        k1 = cv2.waitKey(0)
        if k1 == ord('b'):
            cv2.destroyWindow("scanned photo")
            gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
            cv2.imwrite("D//pdf//scanned%d.jpg" % i, gray)
            i = i + 1
            continue
        elif k1 == ord('u'):
            cv2.destroyWindow('scanned photo')
            gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
            new = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 15)
            cv2.imwrite("D//pdf//scanned%d.jpg" % i, new)
            i = i + 1
            continue
        elif k1 == ord('c'):
            cv2.destroyWindow("scanned photo")
            cannied = cv2.Canny(frame, 200, 250)
            cv2.imwrite("D://pdf//scanned%d.jpg" % i, cannied)
            i = i + 1
            continue
        elif k1 == ord('y'):
            cv2.destroyWindow("scanned photo")
            print("Enter the pixel value of the image that tou dont want them to be included in the pdf  ")
            print('The area of the image bounded by the entered pixel values will be excluded')
            x = input('Enter the x co ordinate of the initial pixel value : ')
            y = input('Enter the y co ordinate of the initial pixel value : ')
            x1 = input('Enter the  x co ordinate of the final pixel value : ')
            y1 = input('Enter the y co ordinate of the final pixel value : ')
            frame[int(x), int(y):int(x1), int(y1)] = [255, 255, 255]
            cv2.imwrite("E://pdf//scanned%d.jpg" % i, frame)
            i = i + 1
            continue
        print('press q to exit')
    elif k == ord('q'):
        ret = False
        break
    else:
        print('invalid input')
cv2.destroyAllWindows()
cap.release()
imagelist = os.listdir("D://pdf")
pdf = FPDF()
for image in imagelist:
    image = "D://pdf//" + image
    pdf.add_page()
    pdf.image(image)
pdf.output("D://my1pdf")
