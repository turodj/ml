#!/usr/bin/python3
#!/usr/bin/env python3

#去除马赛克
import cv2
import numpy as np
import matplotlib.pyplot as plt

# 读取彩色图像
img = cv2.imread("/Users/dongjian/src/python3-src/data/dr.jpeg")

# 调整GaussianBlur函数的参数，使用更大的内核和sigma值来获得更好的平滑效果
blur_img = cv2.GaussianBlur(img, (3, 3), 0)

# 将图像缩小一倍，以便更快地处理它
small_img = cv2.resize(blur_img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

# 将图像转换为Lab色彩空间，并应用bilateralFilter以平滑图像并保留边缘
lab_img = cv2.cvtColor(small_img, cv2.COLOR_BGR2LAB)
bilat_img = cv2.bilateralFilter(lab_img, 100, 100, 75)
bilat_img = cv2.cvtColor(bilat_img, cv2.COLOR_LAB2BGR)

# 将图像放大回原始大小
large_img = cv2.resize(bilat_img, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)

# 显示原始图像和去马赛克效果
plt.subplot(121), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(cv2.cvtColor(large_img, cv2.COLOR_BGR2RGB))
plt.title('De-Mosaic Image'), plt.xticks([]), plt.yticks([])
plt.show()


