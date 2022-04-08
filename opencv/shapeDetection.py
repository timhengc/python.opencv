import cv2
import numpy as np
import stackImg

#通过拐点数目（角的数目）识别形状

# 获得轮廓
def getContours(img):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE) #（图片，查找方法，近似）
    for cnt in contours:
        area = cv2.contourArea(cnt) #轮廓区域面积
        #print(area) #打印区域面积
        if area>5000: #由面积判定哪些图形，哪些是图片
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)  #为每个图形画矩形框（-1 = 选择所有轮廓，（颜色），粗细）
            peri = cv2.arcLength(cnt,True) #弧长，True = 确定是封闭图形
            #print(peri) #打印弧长
            approx = cv2.approxPolyDP(cnt,0.02*peri,True) #拐点坐标list[] （轮廓，分辨率，True同上）
            print(len(approx)) #打印拐点数，例：3=三角形，4=四边形
            objCor = len(approx) #拐点数
            x, y, w, h = cv2.boundingRect(approx) #获得矩形框的起始坐标，宽度和高度

            #根据实际情况填写判断条件及形状名 
            if objCor ==3: objectType ="Tri" #判断是否三角形
            elif objCor == 4:
                aspRatio = w/float(h)  #计算aspect ratio长宽比，判断是正方形还是长方形
                if aspRatio >0.98 and aspRatio <1.03: objectType= "Square"
                else:objectType="Rectangle"
            elif objCor == 5: objectType= "Pentagon" #判断是否多边形或弯曲图形
            elif objCor == 8: 
                aspRatio = w/float(h)  #计算aspect ratio长宽比，判断是圆形还是椭圆形
                if aspRatio >0.98 and aspRatio <1.03: objectType= "Circle"
                else:objectType="Oval"
            else:objectType="None"



            cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),2) #画出矩形框
            cv2.putText(imgContour,objectType,
                        (x+(w//2)-50,y+(h//2)-10),cv2.FONT_HERSHEY_COMPLEX,0.7,
                        (0,0,0),2) #打印形状名字


img = cv2.imread("C:/Users/28151/Desktop/python/practice/opencv/shape.jpg")  # 读取图片
img = cv2.resize(img,(600,600)) #调整大小（宽度，高度），非矢量变化
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #灰色图 cvtColor = conver to color
imgBlur = cv2.GaussianBlur(imgGray,(7,7),1)  #模糊
imgCanny = cv2.Canny(imgBlur,10,20)   #勾勒图 （两个数字不分顺序大小，最小值越小越敏感，最大值越大越迟钝越难识别复杂图形）
imgContour = img.copy() #复制img
getContours(imgCanny) #必须输入勾勒图才能进行识别
imgStack = stackImg.stackImages(0.7,([img,imgGray,imgBlur],[imgCanny,imgContour,imgCanny]))



cv2.imshow("123", imgStack)


cv2.waitKey(0) #延时n ms（0=无限）