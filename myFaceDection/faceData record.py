import os
import cv2
import sys 
from PIL import Image
import numpy as np


def getFaceAndId(path):
    facesSamples=[]
    ids=[]
    #names=[]
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)] #获得path目录中每一个文件的完整路径，join用于合并path和f，for in listdir用于遍历path中所有文件
    #检测人脸
    face_detector = cv2.CascadeClassifier('C:/Users/28151/Desktop/python/practice/opencv/myFaceDection/Classifier/haarcascade_frontalface_default.xml')
    #打印路径数组imagePaths
    print('数据排列：',imagePaths)
    #遍历列表中的图片
    for imagePath in imagePaths:
        #打开图片,灰度化（L表示黑白）
        PIL_img=Image.open(imagePath).convert('L')
        # PIL_img = cv2.resize(PIL_img, dsize=(400, 400))
        #将图像转换为数组
        img_numpy=np.array(PIL_img,'uint8')
        #获取图片人脸特征（若无面容，则faces为空tuple）
        faces = face_detector.detectMultiScale(img_numpy)
        #获取每张图片的id和姓名
        id = int(os.path.split(imagePath)[1].split('.')[0]) #os.path.split(imagePath)将文件路径和文件名分开，[1]取文件名；.split('.')[1]将文件名根据'.'分开，取第1项id（int）
        name = (os.path.split(imagePath)[1].split('.')[1])
        #预防无面容照片(若检测不到面容，此for循环不会运行)
        for x,y,w,h in faces:
            ids.append(id)
            #names.append(name)
            facesSamples.append(img_numpy[y:y+h,x:x+w]) 
            print("w="+str(w)+" h="+str(h))
            print('name',name,'id:', id)
        #打印脸部特征和id
        #print('fs:', facesSamples)
        #print('fs:', facesSamples[id])
    print('fs:', facesSamples)
    print('ids:',ids)
    #print(np.array(ids))
    return facesSamples,ids

if __name__ == '__main__':
    #图片路径（图片所在文件夹）
    path = "C:/Users/28151/Desktop/python/practice/opencv/myFaceDection/Faces"
    #获取脸部图像数组和id数组
    faces,ids=getFaceAndId(path)
    #获取训练对象
    recognizer=cv2.face.LBPHFaceRecognizer_create()
    #recognizer.train(faces,names)#np.array(ids)
    recognizer.train(faces,np.array(ids))
    #保存文件
    recognizer.write('C:/Users/28151/Desktop/python/practice/opencv/myFaceDection/TrainFile/trainer.yml')
    #save_to_file('names.txt',names)

#测试train时缺少一个id会不会出错，或者id错位会不会出错。！！！！！！