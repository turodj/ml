#!/usr/bin/python3
#!/usr/bin/env python3

import imageio.v2 as imageio
import matplotlib.pyplot as plt

import os  
import numpy as np

def get_dir_name(fname):#根据文件名获取它的上级目录名
    parent_dir = os.path.dirname(fname)
    last_path = get_last_dir(parent_dir)
    return last_path

def get_last_dir(path): #根据路径返回最后一个目录名或文件名(带后缀)
    return os.path.basename(os.path.normpath(path))

#把指定目录下的文件转换为gif  
def combine_images_to_GIF(input_dir, output_file, duration = 300):  
    images = [img for img in os.listdir(input_dir) if (img.endswith(".jpg") or img.endswith('jpeg'))]  # 假设只有jpg图片  
    images.sort()  # 按照文件名排序，确保图片顺序  
  
    with imageio.get_writer(output_file, mode='I',duration = duration) as writer:    
        for image in images:  
            writer.append_data(imageio.imread(os.path.join(input_dir, image)))  
  
if __name__=='__main__':
    # 使用函数  
    img_path = '/Users/dongjian/src/python3-src/traindata/jays/'
    fname = get_last_dir(img_path)     
    output_file = img_path+fname+'.gif'  # 修改为你想要的输出文件名  
    combine_images_to_GIF(img_path, output_file)
    print(f'img2gif: [{output_file}] finish!---')
    
    # 播放 GIF
    #show_gif(output_file)
