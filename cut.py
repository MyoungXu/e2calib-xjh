import cv2
from PIL import Image
import os

# 指定文件夹路径
folder_path = "./output/036n"
outpath = './outputcut'

after_crop = (320, 576, 700, 956)
# 获取文件夹中所有图片文件
image_files = [f for f in os.listdir(folder_path) if f.endswith('.bmp') or f.endswith('.png')]

# 遍历每张图片并裁剪后保存
for image_file_name in image_files:
    # 构建图片文件的完整路径
    image_file_path = os.path.join(folder_path, image_file_name)

    # 打开图片
    img = cv2.imread(image_file_path)
    # 裁剪图片
    cropped_img = img[after_crop[0]:after_crop[1], after_crop[2]:after_crop[3]]
    # 构建保存的文件路径
    cropped_image_file_path = os.path.join(outpath, image_file_name)

    # 保存裁剪后的图片
    cv2.imwrite(cropped_image_file_path, cropped_img)

print("所有图片裁剪并保存成功。")