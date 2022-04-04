import cv2

cap = cv2.VideoCapture("C:/Users/28151/Desktop/python/practice/opencv/MXBC.mp4")#读取视频

while 1:
    success, img = cap.read()#读取一帧图片
    if success == 1:
        cv2.imshow("mixue", img)#展示图片
    else:
        break
    if cv2.waitKey(20) & 0xFF == ord('q'): #延时20ms，按q退出
        break