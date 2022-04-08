import os
import cv2
import sys
from PIL import Image
import numpy as np

path = "C:/Users/28151/Desktop/python/practice/opencv/myFaceDection/Faces"
'''imagePaths=[os.path.join(path,f) for f in os.listdir(path)] #获得path目录中每一个文件的完整路径，join用于合并path和f，for in listdir用于遍历path中所有文件
print(imagePaths)

for imagePath in imagePaths:
     id = int(os.path.split(imagePath)[1].split('.')[2]) #os.path.split(imagePath)将文件路径和文件名分开，[1]取文件名；.split('.')[1]将文件名根据'.'分开，取第2项id（int）
     print(id)'''



facesSamples=[]
ids=[]
imagePaths=[os.path.join(path,f) for f in os.listdir(path)] #获得path目录中每一个文件的完整路径，join用于合并path和f，for in listdir用于遍历path中所有文件
#检测人脸
face_detector = cv2.CascadeClassifier('C:/Users/28151/Desktop/python/practice/opencv/haarcascade_frontalface_default.xml')
#打印路径数组imagePaths
print('数据排列：',imagePaths)
#遍历列表中的图片
for imagePath in imagePaths:
    #打开图片,黑白化
    PIL_img=Image.open(imagePath).convert('L')
    #将图像转换为数组，以黑白深浅
    # PIL_img = cv2.resize(PIL_img, dsize=(400, 400))
    img_numpy=np.array(PIL_img,'uint8')
    print(img_numpy)
    #获取图片人脸特征
    faces = face_detector.detectMultiScale(img_numpy)
    #获取每张图片的id和姓名
    id = int(os.path.split(imagePath)[1].split('.')[2]) #os.path.split(imagePath)将文件路径和文件名分开，[1]取文件名；.split('.')[0]将文件名根据'.'分开，取第0项id（int）
    #预防无面容照片
    for x,y,w,h in faces:
        ids.append(id)
        facesSamples.append(img_numpy[y:y+h,x:x+w]) 
        print("w="+str(w)+" h="+str(h))
    #打印脸部特征和id
    #print('fs:', facesSamples)
    print('id:', id)
    #print('fs:', facesSamples[id])
print('fs:', facesSamples)

print(np.array(ids))
