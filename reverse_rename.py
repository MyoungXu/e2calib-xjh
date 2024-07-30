import os
from PIL import Image

# 定义输入和输出文件夹路径
input_folder = 'output/0718'
output_folder = 'output/event'

# 确保输出文件夹存在，如果不存在则创建
os.makedirs(output_folder, exist_ok=True)

# 遍历输入文件夹中的所有文件
file_list = os.listdir(input_folder)
for i, filename in enumerate(file_list):
    if filename.endswith('.png'):
        # 构造输入文件的完整路径
        input_path = os.path.join(input_folder, filename)

        # 打开图像文件
        img = Image.open(input_path)

        # 左右翻转图像
        flipped_img = img.transpose(Image.FLIP_LEFT_RIGHT)

        # 构造输出文件的完整路径，并按照指定格式重命名
        output_filename = '{:06d}.bmp'.format(i + 1)
        output_path = os.path.join(output_folder, output_filename)

        # 保存翻转后的图像
        flipped_img.save(output_path)

        # 关闭图像文件
        img.close()

print("处理完成！")