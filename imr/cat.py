#!/usr/bin/python3
#!/usr/bin/env python3

import tensorflow as tf
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
import numpy as np

# 加载预训练模型
model = tf.keras.applications.ResNet50(weights='imagenet')

# 加载图像并进行预处理
img_path = '/Users/dongjian/src/python3-src/data/cat.jpeg'  # 替换为你的图像路径
img = image.load_img(img_path, target_size=(224, 224))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)

# 进行预测
preds = model.predict(x)

# 解码预测结果
decoded_preds = decode_predictions(preds, top=1)[0]
_, label, confidence = decoded_preds[0]
print(f"预测结果：{label}，置信度：{confidence * 100:.2f}%")
print(decoded_preds)

# 判断猫狗分类
if label in ['cat', 'dog']:
    print("这是一张猫狗图片。")
    if label == 'cat':
        print("这是一张猫的图片。")
    else:
        print("这是一张狗的图片。")
else:
    print("这不是一张猫狗图片。")

