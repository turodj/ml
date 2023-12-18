#!/usr/bin/python3
#!/usr/bin/env python3

from opennsfw2 import make_open_nsfw_model
import cv2
import numpy as np
import os
import tensorflow as tf
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input
from tensorflow.keras.preprocessing import image

# 创建 NSFW 模型实例
nsfw_model = make_open_nsfw_model()

# 定义待分类的图像路径
image_path = '/Users/dongjian/src/python3-src/data/012.jpg'  # 替换为你的根目录路径

# 读取图像
image = cv2.imread(image_path)

# 调整图像形状为 (224, 224, 3)
resized_image = cv2.resize(image, (224, 224))

# 将图像扩展为批量大小为 32
batch_image = np.expand_dims(resized_image, axis=0)
batch_image = np.repeat(batch_image, 32, axis=0)

# 将图像输入模型进行分类
predictions = nsfw_model.predict(batch_image)
print(f'{image_path} {predictions.shape} {predictions[0]}')

#predictions = nsfw_model.predict_image(batch_image)
#print(f'{image_path} {predictions}')


# 打印分类结果
'''
for label, probability in predictions:
   print(f'Label: {label}, Probability: {probability}')
   '''



