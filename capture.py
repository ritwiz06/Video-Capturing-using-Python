import cv2, time

video = cv2.VideoCapture(0)  #0 for webcam, 1, 2, 3- for external camera, video file path for pre made Video, DSHOW-port of camera

c=0

while True:
    c= c+1
    check, frame = video.read() #first frame capturing

    print(check)
    print(frame)


    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Capturing", gray)
    key = cv2.waitKey(1)
    if key==ord('q'):
        break
print(c)
video.release()
cv2.destroyAllWindows()
