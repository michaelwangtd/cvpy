# -*- coding:utf-8 -*-

import cv2
from opencvele import img_aug as ia


"""
    augment_images函数的主要参数：
        flip_fc：翻转方式
        crop_size：裁剪比率
        crop_hw_vari：裁剪宽、高比率 
        rotate_angle：旋转角度
        p_crop：去黑边裁剪比例
        h、s、v：色彩空间
        gamma：Gamma变化的范围
"""
def augment_images(img,flip_fc=1,crop_size=0.8,crop_hw_vari=0.1,rotate_angle=20,p_crop=1,
                   h=10,s=0.1,v=0.1,gamma=2):
    img_cpy = img.copy()
    # 1 图像翻转
    img_cpy = cv2.flip(img_cpy,flip_fc)
    # 2 随机裁剪
    img_cpy = ia.random_crop(img_cpy,crop_size,crop_hw_vari)
    # 3 随机旋转
    img_cpy = ia.random_rotate(img_cpy,rotate_angle,p_crop)
    # 4 随机HSV扰动
    img_cpy = ia.random_hsv_transform(img_cpy,h,s,v)
    # 5 随机Gamma扰动
    img_cpy = ia.random_gamma_transform(img_cpy,gamma)

    return img_cpy



if __name__ == '__main__':
    img = cv2.imread('./pic/girl.jpg')

    # ia.imgshow(img)
    # img = augment_images(img)
    # ia.imgshow(img)

    ia.imgshow(img,t=50000)
    for i in range(300):
        img_cp = img.copy()
        img_cp = augment_images(img_cp)
        fp = './ext/girl_' + str(i) + '.jpg'
        cv2.imwrite(fp,img_cp)
