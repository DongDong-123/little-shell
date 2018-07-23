from PIL import Image
import argparse


parser = argparse.ArgumentParser()  # 创建ArgumentParser实例
"""使用add_argument添加参数(位置参数和可选参数)"""
parser.add_argument('file')  # 输入文件
parser.add_argument('-o', '--output')  # 输出文件
parser.add_argument('--width', type=int, default=80)  # 输出字符画宽
parser.add_argument('--height', type=int, default=80)  # 输出字符画高

args = parser.parse_args()  # 获取参数

IMG = args.file
WIDTH = args.width
HEIGHT = args.height
OUTPUT = args.output

# 设置字符
ascii_char = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()/\[]{}+=_~''")


def get_char(r,g,b,alpha=256):
	if alpha == 0:
		return ' '
	length = len(ascii_char)
	gray = int(0.2126*r + 0.7125*g + 0.0722*b)

	unit = (256.0 + 1) / length

	return ascii_char[int(gray/unit)]


if __name__ == '__main__':
	im = Image.open(IMG)
	im=im.resize((WIDTH, HEIGHT),Image.NEAREST)  # Image.NEAREST:低质量;Image.ANTIALIAS:高质量
	# Image.BILINEAE:双线性; Image.BICUBIC:三次样条插值

	txt = ''
	for i in range(HEIGHT):
		for j in range(WIDTH):
			txt += get_char(*im.getpixel((j,i)))
		txt += '\n'

	print(txt)

	# 输出到文件
	if OUTPUT:
		with open(OUTPUT, 'w') as f:
			f.write(txt)
	else:
		with open("output.txt", 'a') as f:  # 使用追加模式,可以写入多个
			f.write(txt)
