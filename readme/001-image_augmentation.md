
##图像扩增##


>图像扩增是构建具有较强泛化能力模型的常用手段，也是为了防止模型过拟合。

扩增的方法采用翻转、裁剪、旋转、HSV空间变换、gamma变换5种。
```python
'''
裁剪函数：
x0：左上角横坐标
y0：左上角纵坐标
w：裁剪宽度
h：裁剪高度
'''
crop_image = lambda img, x0, y0, w, h: img[y0:y0+h, x0:x0+w]

'''
随机裁剪
area_ratio：裁剪比率
hw_vari：裁剪宽、高比率
'''
def random_crop(img, area_ratio, hw_vari):
    h, w = img.shape[:2]
    hw_delta = np.random.uniform(-hw_vari, hw_vari)
    hw_mult = 1 + hw_delta

    w_crop = int(round(w*np.sqrt(area_ratio*hw_mult)))

    if w_crop > w:
        w_crop = w

    h_crop = int(round(h*np.sqrt(area_ratio/hw_mult)))
    if h_crop > h:
        h_crop = h

    x0 = np.random.randint(0, w-w_crop+1)
    y0 = np.random.randint(0, h-h_crop+1)

    return crop_image(img, x0, y0, w_crop, h_crop)

'''
随机旋转
angle_vari：旋转角度
p_crop：去黑边裁剪比例
'''
def random_rotate(img, angle_vari, p_crop):
    angle = np.random.uniform(-angle_vari, angle_vari)
    crop = False if np.random.random() > p_crop else True
    return rotate_image(img, angle, crop)

'''
随机hsv变换：
h、s、v：色彩空间
'''
def random_hsv_transform(img, hue_vari, sat_vari, val_vari):
    hue_delta = np.random.randint(-hue_vari, hue_vari)
    sat_mult = 1 + np.random.uniform(-sat_vari, sat_vari)
    val_mult = 1 + np.random.uniform(-val_vari, val_vari)
    return hsv_transform(img, hue_delta, sat_mult, val_mult)

'''
随机gamma变换
gamma_vari：gamma变化范围
'''
def random_gamma_transform(img, gamma_vari):
    log_gamma_vari = np.log(gamma_vari)
    alpha = np.random.uniform(-log_gamma_vari, log_gamma_vari)
    gamma = np.exp(alpha)
    return gamma_transform(img, gamma)
```

外层使用函数封装上面的方法，得到一个单核图片处理方法。数据量较大情况下可以使用多进程同时处理数据。

```python
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

```

这里使用经典的莱娜·瑟德贝里图片，进行随机增强实验，生成50张图片的结果。

<div align="center"><img src="http://p9wapwreo.bkt.clouddn.com/image/jpg/python/cv/aug1.png" height="100%" width="60%"/></div>

进一步生成300张图片的结果

<div align="center"><img src="http://p9wapwreo.bkt.clouddn.com/image/jpg/python/cv/aug2.png" height="100%" width="60%"/></div>

图像变换相关结果

<div align="center"><img src="http://p9wapwreo.bkt.clouddn.com/image/jpg/python/cv/aug3.png" height="100%" width="60%"/></div>