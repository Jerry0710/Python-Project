# Image Art practice to learn to use the Numpy library
import numpy as np
from PIL import Image

a = np.asarray(Image.open('./IMG_8827.jpg').convert('L')).astype('float')

depth = 10
grad_x, grad_y = np.gradient(a)
grad_x *= depth/100
grad_y *= depth/100

vec_el = np.pi/4
vec_az = np.pi/4
dx = np.cos(vec_el)*np.cos(vec_az)
dy = np.cos(vec_el)*np.sin(vec_az)
dz = np.sin(vec_el)

A = np.sqrt(grad_x**2 + grad_y**2 + 1)
uni_x = grad_x/A
uni_y = grad_y/A
uni_z = 1./A

b = 255*(dx*uni_x + dy*uni_y + dz*uni_z)   	# 光源归一化
# b = 255*(dx*uni_x + dy*uni_y)   	# 光源归一化
b = b.clip(0, 255)

im = Image.fromarray(b.astype('uint8')) 	# 重构图像
im.save('./IMG_HD.jpg')
