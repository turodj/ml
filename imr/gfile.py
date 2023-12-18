#!/usr/bin/python3
#!/usr/bin/env python3

import os
import opennsfw2 as n2

def get_filenames(root_dir):
    image_extensions = ['.jpg', '.jpeg', '.png']  # 可根据需要添加其他图片扩展名
    image_filenames = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for dirname in dirnames:
            print(dirname)
            new_dirpath = os.path.join(dirpath, dirname)
            image_filenames.extend(get_filenames(new_dirpath))

        for filename in filenames:
            ext = os.path.splitext(filename)[1].lower()
            if ext in image_extensions:
                image_filenames.append(os.path.join(dirpath, filename))
    return image_filenames


if __name__=='__main__':

	root_dir = '/Users/dongjian/src/python3-src/data/010.jpg'  # 替换为你的根目录路径
	nsfw_probability = n2.predict_image(root_dir)
	print(nsfw_probability)

	#image_filenames = get_filenames(root_dir)

#	for filename in image_filenames:
	# 	print(filename)




	#nsfw_probabilities = n2.predict_images(image_paths)
