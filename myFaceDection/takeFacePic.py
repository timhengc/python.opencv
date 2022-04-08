#用笔记本摄像头拍照，保存原图和人脸截图

import cv2

cap = cv2.VideoCapture(0)#(创建对象cap)启用摄像头,0=笔记本内置摄像头，其他数字可能代表外接摄像头序号

frameWidth = 640
frameHeight = 480
brightness = 100
faceCascade= cv2.CascadeClassifier("C:/Users/28151/Desktop/python/practice/opencv/myFaceDection/Classifier/haarcascade_frontalface_default.xml") #分类器。启用现有的XML文件,它定义哪些属于face哪些不属于face
minArea = 15000 #人脸最小面积
count=1

cap.set(3, frameWidth)  # 3=宽度的id
cap.set(4, frameHeight)  # 4=高度的id
cap.set(10, brightness)  # 10=亮度的id

name = input("Input your name : ") #输入名字

while 1:
    success, img = cap.read()
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #灰色图 cvtColor = conver to color
    faces = faceCascade.detectMultiScale(imgGray,1.1,8) #获得识别目标的参数,是一个4列n行的数组(灰度图，缩放scale，检测到n次才确定是人脸)
    for (x, y, w, h) in faces:
        area = w*h
        #print(area)
        if area >minArea: #用面积做第一层判断
            imgCopy = img.copy()
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 2) #画矩形圈起来
            cv2.putText(img,name,(x,y-5),
                        cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(255,255,255),2) #写字
            imgRoi = img[y:y+h,x:x+w] #截图 Roi=region of interest
            cv2.imshow("ROI", imgRoi)
    cv2.imshow("Result", img)
    keyboard = cv2.waitKey(1) & 0xFF
    if keyboard == ord('S'):  #按下S保存截图
        cv2.imwrite("C:/Users/28151/Desktop/python/practice/opencv/myFaceDection/Faces/"+str(count)+"."+name+".jpg",imgRoi)  #将截图imgRoi写入jpg文件
        cv2.imwrite("C:/Users/28151/Desktop/python/practice/opencv/myFaceDection/Faces/Img."+str(count)+"."+name+".jpg",imgCopy)  #将完整的img写入jpg文件
        cv2.rectangle(img,(0,200),(640,300),(255,255,255),cv2.FILLED)  #画text的底色
        cv2.putText(img,"Saved",(230,265),cv2.FONT_HERSHEY_DUPLEX,
                    2,(0,0,255),2) #写字显示已保存
        cv2.imshow("Result",img)
        cv2.waitKey(500)
        count +=1
        
    elif keyboard == ord('Q'): #按Q退出
        cap.release() #释放摄像头
        cv2.destroyAllWindows() #释放内存
        break