import cv2

cap = cv2.VideoCapture(0)#(创建对象cap)启用摄像头,0=笔记本内置摄像头，其他数字可能代表外接摄像头序号

frameWidth = 640
frameHeight = 480
brightness = 100
numPlateCascade= cv2.CascadeClassifier("C:/Users/28151/Desktop/python/practice/opencv/haarcascade_russian_plate_number.xml") #(创建对象)启用现有的XML文件,它定义哪些属于车牌
minArea = 500
count=0

cap.set(3, frameWidth)  # 3=宽度
cap.set(4, frameHeight)  # 4=高度
cap.set(10, brightness)  # 10=亮度

while 1:
    success, img = cap.read()
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #灰色图 cvtColor = conver to color
    Plates = numPlateCascade.detectMultiScale(imgGray,1.1,4) #获得识别目标的参数,是一个4列n行的数组
    for (x, y, w, h) in Plates:
        area = w*h
        if area >minArea: #用面积做第一层判断
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 2) #画矩形圈起来
            cv2.putText(img,"Number Plate",(x,y-5),
                        cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(255,255,255),2) #写字
            imgRoi = img[y:y+h,x:x+w] #截图 Roi=region of interest
            cv2.imshow("ROI", imgRoi)
    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF == ord('S'):  #按下S保存截图
        cv2.imwrite("C:/Users/28151/Desktop/python/practice/opencv/Plate_"+str(count)+".jpg",imgRoi)  #将截图imgRoi写入jpg文件
        cv2.rectangle(img,(0,200),(640,300),(0,255,0),cv2.FILLED)  #画text的底色
        cv2.putText(img,"Scan Saved",(150,265),cv2.FONT_HERSHEY_DUPLEX,
                    2,(0,0,255),2) #写字显示已保存
        cv2.imshow("Result",img)
        cv2.waitKey(500)
        
        count +=1
    elif cv2.waitKey(1) & 0xFF == ord('Q'): #按Q退出
        break