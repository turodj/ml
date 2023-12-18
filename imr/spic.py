#!/usr/bin/python3
#!/usr/bin/env python3

#自己编写的图片预测库，其他目录的py文件可以通过import导入此程序中的库进行图片分类预测
import os 
import tensorflow as tf
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input
from tensorflow.keras.preprocessing import image
import numpy as np
import cv2

# 加载预训练模型
model = ResNet50(weights='imagenet')

def img_show(title,fname):
    img = cv2.imread(fname)
    cv2.imshow(title,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 加载和预处理图像
def load_and_preprocess_image(image_path):
    img = image.load_img(image_path, target_size=(224, 224))
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img = preprocess_input(img)
    return img

def write_code(image_path,decoded_predictions):
    logpath = '/Users/dongjian/src/python3-src/trainlog/'
    fname = logpath+os.path.basename(image_path)+'.txt'

    if os.path.exists(fname):
        os.remove(fname)

    with open(fname,'a') as f:
        for _, category, probability in decoded_predictions:
            f.write(f'{category} {probability}\n')
    
# 进行图像分类预测
def classify_image(image_path):
    img = load_and_preprocess_image(image_path)
    predictions = model.predict(img)
    print(f'pre type {type(predictions)} shape {predictions.shape}')
    decoded_predictions = tf.keras.applications.imagenet_utils.decode_predictions(predictions, top=10)[0]
    #print(decoded_predictions)
    #write_code(image_path,decoded_predictions)
    return decoded_predictions

# 暴露图片识别函数
def detect_explicit_image(image_path):
    flag = 0
    predictions = classify_image(image_path)
    explicit_categories = ['bikini','brassiere','nudity','pornography','adult','genital exposure','sexual acts','violence and abuse','hentai','explicit text','blasphemy','indecent behavior','inappropriate physical contact','pornographic transactions','provocative attire','nipple','diaper']

    #print(predictions)

    for _, category, probability in predictions:
        if category.lower() in explicit_categories:
            #print(predictions)
            print(category,probability)
            flag =flag +1
    if flag>0:
        #print(predictions[:10])
        write_code(image_path,predictions)
        return True
    else:
        return False

def get_filenames(root_dir):
    image_extensions = ['.jpg', '.jpeg', '.png']  # 可根据需要添加其他图片扩展名
    image_filenames = []

    for dirpath,dirnames,filenames in os.walk(root_dir):
        for dirname in dirnames:
            #print(dirname)
            new_dirpath = os.path.join(dirpath, dirname)
            image_filenames.extend(get_filenames(new_dirpath))

        for filename in filenames:
            #print(filename)
            ext = os.path.splitext(filename)[1].lower()
            if ext in image_extensions:
                image_filenames.append(os.path.join(dirpath, filename))

    return image_filenames


if __name__=='__main__':
    print('begin')
    root_dir = '/Users/dongjian/src/python3-src/traindata/julia'  # 替换为你的根目录路径
	#root_dir = '/Users/dongjian/Movies/2021/10' # 替换为你的根目录路径

    filenames = get_filenames(root_dir)
	#print(filenames)

    for filename in filenames:	
	
        image_path=filename
		#print(filename)
		#image_path = '/Users/dongjian/src/python3-src/data/010.jpg'

        is_explicit = detect_explicit_image(image_path)
        if is_explicit:
            print(f"{filename} 图像包含x内容！")
        #else:
            #print(f"i{filename} 图像未包含x内容。")

