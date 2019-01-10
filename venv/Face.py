#1.导入库
import cv2
#2.加载图片
img = cv2.imread('F://PythonDemo//FaceByOpenCV//venv//imgsource//img2.jpg')

#3.创建窗口
cv2.namedWindow('Face')
#4.显示图片
cv2.imshow('hello',img)
#5.暂停窗口
cv2.waitKey(0)
#6.关闭窗口
cv2.destroyAllWindows()