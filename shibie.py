from msilib.schema import TextStyle
from paddleocr import PaddleOCR
 
import cv2
 
import numpy as np
 
from PIL import Image, ImageDraw, ImageFont
 
from paddleocr import PaddleOCR, draw_ocr
import os
import openpyxl
 
font=cv2.FONT_HERSHEY_SIMPLEX
 
 
 
#Paddleocr目前支持中英文、英文、法语、德语、韩语、日语，可以通过修改lang参数进行切换
 
#参数依次为`ch`, `en`, `french`, `german`, `korean`, `japan`。
 
ocr = PaddleOCR(use_angle_cls=True, lang="ch",use_gpu=False,
 
                rec_model_dir='D:/vscode-python/python/PaddleOCR/models/ch_PP-OCRv3_rec_infer/',
 
                cls_model_dir='D:/vscode-python/python/PaddleOCR/models/ch_ppocr_mobile_v2.0_cls_infer/',
 
                det_model_dir='D:/vscode-python/python/PaddleOCR/models/ch_PP-OCRv3_det_infer/') # need to run only once to download and load model into memory
 
 
 
img_path = r'D:\vscode-python\python\lianxi\tupian\jietu.png'
 
result = ocr.ocr(img_path, cls=True)
 
 
 
# 显示结果
 
from PIL import Image
 
image = Image.open(img_path).convert('RGB')
 
boxes = [line[0] for line in result]
 
txts = [line[1][0] for line in result]
 
scores = [line[1][1] for line in result]
 
im_show = draw_ocr(image, boxes, txts, scores, font_path='simfang.ttf')
 
im_show = Image.fromarray(im_show)
 
 
 
im_show.save(r'result.png')

# wb = openpyxl.load_workbook('abc.xlsx')
baconFile = open('abc.txt', 'w')
# i=name=txts
# for i in '12':
baconFile.write(str(txts))
#     for i in name:
#        baconFile.write(str(i))
baconFile.close()
print(txts)