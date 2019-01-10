# -*- coding:utf-8 -*-

# import cv2
# #导入库
#
# img = cv2.imread('F://PythonDemo//FaceByOpenCV//venv//imgsource//img2.jpg')
# #加载图片
#
# face = cv2.CascadeClassifier('F://PythonDemo//FaceByOpenCV//venv//xmlsorce//haarcascade_frontalface_default.xml')
# #加载人脸模型
#
# gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
# #调整图片灰度
#
# faces = face.detectMultiScale(gray)
# #检查人脸
#
# for (x,y,w,h) in faces:
#     cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),10)
# #标记人脸
#
# cv2.namedWindow('Face',0)
# #创建窗口
#
# cv2.resizeWindow('Face',500,800)
# #调整窗口大小
#
# cv2.imshow("Face",img)
# #显示图片
#
# cv2.waitKey(0)
# #暂停窗口
#
# cv2.destroyAllWindows()
# #关闭窗口


import cv2
import os

path = os.path.abspath(__file__).split('Face2.py',1)[0]+"\\xmlsorce\\haarcascade_frontalface_default.xml"

if not os.path.isdir(os.path.abspath(__file__).split('\Face2.py',1)[0]):
    os.mkdir(os.path.join(os.path.abspath(__file__).split('\Face2.exe',1)[0],'xmlsource'))

capture = cv2.VideoCapture(0)

cv2.namedWindow("Hello",0)

while True:
    ret,frame = capture.read()

    face = cv2.CascadeClassifier(path)

    gray = cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)

    faces = face.detectMultiScale(gray)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),5)
    cv2.imshow("Hello", frame)

    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

capture.release()

cv2.destroyAllWindows()