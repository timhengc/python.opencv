import cv2

faceCascade= cv2.CascadeClassifier("C:/Users/28151/Desktop/python/practice/opencv/haarcascade_frontalface_default.xml") #分类器。启用现有的XML文件,它定义哪些属于face哪些不属于face

img = cv2.imread('C:/Users/28151/Desktop/python/practice/opencv/nana.jpg')
#img = cv2.imread('C:/Users/28151/Desktop/python/practice/opencv/myFaceDection/Faces/1.noface.jpg')
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(imgGray,1.1,4) #定义faces (图片,scale,min neighbour=至少检测出n次才算确定是人脸，flags直接设为0，minSize=人脸最小尺寸，如（100，100），maxSize) 一般后面的限制参数不设置，让它自己适应可能效果更好 。

for (x,y,w,h) in faces: 
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2) #画矩形圈出人脸

cv2.imshow("Result",img)
cv2.waitKey(0)
