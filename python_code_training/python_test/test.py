
import imageio
import numpy as np

# 读取图像
img = imageio.imread("i9.jpg")

# RGB转BGR
bgr_img = img[:,:,::-1]

# 保存结果
imageio.imsave("bgr_img9.jpg", bgr_img)



