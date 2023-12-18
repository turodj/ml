#!/usr/bin/python3
#!/usr/bin/env python3

image_path = '/Users/dongjian/src/python3-src/data/cat.jpeg'  # 替换为你的根目录路径

from nudenet import NudeDetector

detector = NudeDetector(image_path)

image_path = '/Users/dongjian/src/python3-src/data/cat.jpeg'  # 替换为你的根目录路径

# Performing detection
detector.detect(image_path)
# [{'box': [352, 688, 550, 858], 'score': 0.9603578, 'label': 'BELLY'}, {'box': [507, 896, 586, 1055], 'score': 0.94103414, 'label': 'F_GENITALIA'}, {'box': [221, 467, 552, 650], 'score': 0.8011624, 'label': 'F_BREAST'}, {'box': [359, 464, 543, 626], 'score': 0.6324697, 'label': 'F_BREAST'}]

# Censoring an image
detector.censor('path_to_nude_image', out_path='censored_image_path', visualize=False)



