import cv2

cap = cv2.VideoCapture(0)#(创建对象cap)启用摄像头,0=笔记本内置摄像头，其他数字可能代表外接摄像头序号

cap.set(3, 640)  # 3=宽度
cap.set(4, 480)  # 4=高度
cap.set(10, 100)  # 10=亮度

while 1:
    success, img = cap.read()
    if success == 1:
        cv2.imshow("mixue", img)
    else:
        break
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
