#!/usr/bin/python3
#!/usr/bin/env python3

#检测单张图片的分类
import os 
import tensorflow as tf
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input
from tensorflow.keras.preprocessing import image
import numpy as np
import cv2
import spic #导入当前ml下的spic.py,可以引起它里面的类、函数

# 加载预训练模型
model = ResNet50(weights='imagenet')

def img_show(title,fname): 
    img = cv2.imread(fname)
    cv2.imshow(title,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()    



if __name__=='__main__':
    print('begin')


	
    fname = '/Users/dongjian/src/python3-src/data/012.jpg'
    img = cv2.imread(fname)
    

    is_explicit = spic.detect_explicit_image(fname)
    if is_explicit:
        print(f"{fname} 图像包含SEX内容！")
    else:
       print(f"i{fname} 图像未包含SEX内容。")

    #cv2.imshow('orign', img)
    img_show('test',fname)
    ''' 
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    '''

