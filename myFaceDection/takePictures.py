#用笔记本摄像头拍照，保存原图
import cv2

cap = cv2.VideoCapture(0)#(创建对象cap)启用摄像头,0=笔记本内置摄像头，其他数字可能代表外接摄像头序号

frameWidth = 640
frameHeight = 480
brightness = 100
count =1

cap.set(3, frameWidth)  # 3=宽度的id
cap.set(4, frameHeight)  # 4=高度的id
cap.set(10, brightness)  # 10=亮度的id

name = input("Input your name : ") #输入名字
count = int(input("Input photo number counted from(1 by default) : "))#输入照片序号，从1开始，再次启动程序必须从输入最后一个序号+1

while 1:
    success, img = cap.read()
    cv2.imshow("Pic", img)
    keyboard = cv2.waitKey(1) & 0xFF
    if  keyboard == ord('S'):  #按下S保存截图
        cv2.imwrite("C:/Users/28151/Desktop/python/practice/opencv/myFaceDection/Faces/"+str(count)+"."+name+".jpg",img)  #将图片保存为jpg文件
        cv2.rectangle(img,(0,200),(640,300),(255,255,255),cv2.FILLED)  #画text的底色
        cv2.putText(img,"Saved",(230,265),cv2.FONT_HERSHEY_DUPLEX,
                    2,(0,0,255),2) #写字显示已保存
        cv2.imshow("Pic",img)
        cv2.waitKey(500)
        count +=1
    elif keyboard == ord('Q'): #按Q退出
        cap.release() #释放摄像头
        cv2.destroyAllWindows() #释放内存
        break