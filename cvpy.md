#使用python操作opencv#

>本教程默认读者有一定的计算机视觉和python基础

* 使用python表示一副图像
```python
img = np.array([
    [[255, 0, 0], [0, 255, 0], [0, 0, 255]],
    [[255, 255, 0], [255, 0, 255], [0, 255, 255]],
    [[255, 255, 255], [128, 128, 128], [0, 0, 0]],
], dtype=np.uint8)
plt.imsave('color_pyplot.jpg',img)
cv2.imwrite('color_cv2.jpg',img)
```

* imread imwrite
```python
img = './girl.jpg'
color_img = cv2.imread(img)
print(color_img.shape)
gray_img = cv2.imread(img,cv2.IMREAD_GRAYSCALE)
print(gray_img.shape)
cv2.imwrite('./grayscale.jpg',gray_img)

cv2.imwrite('./girl_jpg.jpg',color_img,(cv2.IMWRITE_JPEG_QUALITY,80))
cv2.imwrite('./girl_png.png',color_img,(cv2.IMWRITE_PNG_COMPRESSION,5))
```