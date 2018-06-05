# -*- coding:utf-8 -*-

import numpy as np
import cv2
import matplotlib.pyplot as plt


cv2.imread('./girl.jpg')



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