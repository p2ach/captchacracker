import CaptchaCracker as cc
import os
import argparse
import cv2
import numpy as np
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--input',default="/app/captcha/assets/ex_0.png")
args = parser.parse_args()

# Target image data size
img_width = 200
img_height = 50
# Target image label length
max_length = 6
# Target image label component
characters = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}

# Model weight file path
weights_path = "model/weights.h5"
# Creating a model application instance
AM = cc.ApplyModel(weights_path, img_width, img_height, max_length, characters)

# Target image path
target_img_path = args.input

list_ex = os.listdir("assets/")

# Predicted value

for ex_png in list_ex:
    path2ex=os.path.join("assets",ex_png)
    if os.path.isfile(path2ex):
        temp_png = cv2.imread(path2ex)
        # print("path2ex",path2ex)
        # print("temp_png 1 :", temp_png.shape)
        temp_png= np.pad(temp_png, ((0,0),(0,50),(0,0)), 'constant', constant_values=255)
        # print("temp_png 2 :",temp_png.shape)

            # cv2.resize(temp_png,(250,50))
        cv2.imwrite(os.path.join("assets/test/",ex_png),temp_png)

        path2ex_target=os.path.join("assets/test/", ex_png)
        pred = AM.predict(path2ex_target)
        print(ex_png + " : " + pred)