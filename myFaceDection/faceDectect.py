import cv2
import numpy as np
import os
# coding=utf-8
import urllib
import urllib.request
import hashlib

#加载训练数据集文件
recogizer=cv2.face.LBPHFaceRecognizer_create()
recogizer.read('C:/Users/28151/Desktop/python/practice/opencv/myFaceDection/TrainFile/trainer.yml')
names=[]
warningtime = 0
count = 1
#对密码进行加密
def md5(str):
    import hashlib
    m = hashlib.md5()
    m.update(str.encode("utf8"))
    return m.hexdigest()

statusStr = {
    '0': '短信发送成功',
    '-1': '参数不全',
    '-2': '服务器空间不支持,请确认支持curl或者fsocket,联系您的空间商解决或者更换空间',
    '30': '密码错误',
    '40': '账号不存在',
    '41': '余额不足',
    '42': '账户已过期',
    '43': 'IP地址限制',
    '50': '内容含有敏感词'
}

#报警发送短信(短信宝平台)
def warning():
    global count
    print("警报"+str(count)+"次")
    count +=1
    smsapi = "http://api.smsbao.com/"
    # 短信平台账号
    user = 'Timheng'
    # 短信平台密码
    password = md5('**')#4545645
    # 要发送的短信内容
    content = '【陌生人报警】\n检测到未知人员\n地点：xxx'
    # 要发送短信的手机号码
    phone = '13728300927'

    data = urllib.parse.urlencode({'u': user, 'p': password, 'm': phone, 'c': content})
    send_url = smsapi + 'sms?' + data
    response = urllib.request.urlopen(send_url)
    the_page = response.read().decode('utf-8')
    print(statusStr[the_page])

#准备识别的图片
def face_detect(img):
    imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#转换为灰度图
    face_detector=cv2.CascadeClassifier('C:/Users/28151/Desktop/python/practice/opencv/myFaceDection/Classifier/haarcascade_frontalface_default.xml')#分类器
    face=face_detector.detectMultiScale(imgGray,1.1,7,cv2.CASCADE_SCALE_IMAGE) #获取脸部区域参数（可选最小最大面积）
    #face=face_detector.detectMultiScale(imgGray) #先识别有无人脸
    #若识别到人脸，再分辨是谁
    for x,y,w,h in face:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 2) #画矩形圈起来
        # 人脸识别，获取id和误差
        ids, error = recogizer.predict(imgGray[y:y + h, x:x + w])
        #若误差过大，且超过100帧图片出现此情况，则发出警报
        if error > 80:
            global warningtime
            warningtime += 1
            #print("warning time = " + str(warningtime)) #打印警告次数
            if warningtime > 100:
               warning() #发出警报
               warningtime = 0
            cv2.putText(img, 'Unknow', (x + 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 1) #打印“Unkonw”
        else:
            cv2.putText(img,str(names[ids-1]), (x + 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 1) #打印人名
    cv2.imshow('Result',img)
    #print('bug:',ids)

#从照片目录中获取名字列表
def name():
    path = 'C:/Users/28151/Desktop/python/practice/opencv/myFaceDection/Faces'
    #names = []
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)]
    for imagePath in imagePaths:
       name = str(os.path.split(imagePath)[1].split('.',2)[1]) #把1.Tim根据'.'分成2份取Tim
       names.append(name)



#检测视频
name() #获取名字列表
cap=cv2.VideoCapture('C:/Users/28151/Desktop/python/practice/opencv/myFaceDection/FANDENG.mp4') #加载视频
while True:
    success, img = cap.read() #读取一帧图片
    if success == 1:
        face_detect(img) #识别人脸
        keyboard = cv2.waitKey(1) & 0xFF #检测按键+延迟1ms
    else:
        break
    if keyboard == ord('Q'): #按Q退出
        break
cv2.destroyAllWindows()  #关闭窗口
cap.release() #释放内存

'''#检测图片
name() #获取名字列表
img = cv2.imread('C:/Users/28151/Desktop/python/practice/opencv/myFaceDection/nana.jpg')
face_detect(img)
cv2.waitKey(0)
'''

'''#检测摄像头
name() #获取名字列表
cap=cv2.VideoCapture(0) #启动摄像头
while True:
    success, img = cap.read() #读取一帧图片
    if success == 1:
        face_detect(img) #识别人脸
        keyboard = cv2.waitKey(1) & 0xFF #检测按键+延迟1ms
    else:
        break
    if keyboard == ord('Q'): #按Q退出
        break
cv2.destroyAllWindows()  #关闭窗口
cap.release() #释放内存'''