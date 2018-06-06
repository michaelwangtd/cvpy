# -*- coding:utf-8 -*-

import numpy as np
import cv2
import matplotlib.pyplot as plt

def imgshow(img):
    cv2.imshow('img',img)
    cv2.waitKey(5000)











# # 仿射变换
# img = cv2.imread('./pic/girl.jpg')
# # 仿射变换核
# core1 = np.array([[1.6, 0, -150],
#     [0, 1.6, -240]],dtype=np.float32)
# theta = 15 * np.pi / 180
# core2 = np.array([[1, np.tan(theta), 0],
#     [0, 1, 0]],dtype=np.float32)
# core3 = np.array([[np.cos(theta), -np.sin(theta), 0],
#     [np.sin(theta), np.cos(theta), 0]],dtype=np.float32)
#
# imgd1 = cv2.warpAffine(img,core1,(300,300))
# imgd2 = cv2.warpAffine(img,core2,(300,300))
# imgd3 = cv2.warpAffine(img,core3,(300,300))
# cv2.imwrite('./pic/affine1.jpg',imgd1)
# cv2.imwrite('./pic/affine2.jpg',imgd2)
# cv2.imwrite('./pic/affine3.jpg',imgd3)




# # 直方图
# img = cv2.imread('./pic/girl.jpg')
# b,g,r = cv2.split(img)
# hist_b = cv2.calcHist([b],[0],None,[256],[0.0,255.0])
# print(type(hist_b),hist_b.shape)    # <class 'numpy.ndarray'> (256, 1)


# # hsv空间
# img = cv2.imread('./pic/girl.jpg')
# img_hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
# hsv_cpy = img_hsv.copy()
# # hsv H域变换
# # hsv_cpy[:,:,0] = (hsv_cpy[:,:,0]+20)%180
# # img_cpy = cv2.cvtColor(hsv_cpy,cv2.COLOR_HSV2BGR)
# # cv2.imwrite('./pic/girl_color1.jpg',hsv_cpy)
# # hsv S域变换
# # hsv_cpy[:,:,1] = (hsv_cpy[:,:,1]+20)%180
# # img_cpy = cv2.cvtColor(hsv_cpy,cv2.COLOR_HSV2BGR)
# # cv2.imwrite('./pic/girl_hsv_s.jpg',hsv_cpy)
# # hsv V域变换
# hsv_cpy[:,:,2] = (hsv_cpy[:,:,2]+10)%180
# img_cpy = cv2.cvtColor(hsv_cpy,cv2.COLOR_HSV2BGR)
# cv2.imwrite('./pic/girl_hsv_v.jpg',hsv_cpy)
# imgshow(img_cpy)




# img = cv2.imread('./pic/girl.jpg')
# img_hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
# cv2.imshow('img_hsv',img_hsv)
# cv2.waitKey(5000)






# img = cv2.imread('./pic/boy.jpg')
# img22 = cv2.resize(img,(200,200))
# img05 = cv2.resize(img,(0,0),fx=0.5,fy=0.5,interpolation=cv2.INTER_NEAREST)
# img33 = cv2.copyMakeBorder(img,50,50,50,50,cv2.BORDER_CONSTANT,value=(0,0,0))
# cv2.imshow('gril',img)
# cv2.imshow('gril22',img22)
# cv2.imshow('girl05',img05)
# cv2.imshow('img33',img33)
# cv2.waitKey(5000)



# # img = './color_cv2.jpg'
# img = './girl.jpg'
# color_img = cv2.imread(img)
# print(color_img.shape)
# # print(color_img)
# gray_img = cv2.imread(img,cv2.IMREAD_GRAYSCALE)
# print(gray_img.shape)
# # print(gray_img)
# cv2.imwrite('./grayscale.jpg',gray_img)
# re_grayimg = cv2.imread('./grayscale.jpg')
# print(re_grayimg.shape)
#
# cv2.imwrite('./girl_jpg.jpg',color_img,(cv2.IMWRITE_JPEG_QUALITY,80))
# cv2.imwrite('./girl_png.png',color_img,(cv2.IMWRITE_PNG_COMPRESSION,5))





# img = np.array([
#     [[255, 0, 0], [0, 255, 0], [0, 0, 255]],
#     [[255, 255, 0], [255, 0, 255], [0, 255, 255]],
#     [[255, 255, 255], [128, 128, 128], [0, 0, 0]],
# ], dtype=np.uint8)
# plt.imsave('color_pyplot.jpg',img)
# cv2.imwrite('color_cv2.jpg',img)