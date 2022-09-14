from msilib.schema import TextStyle
from pickle import FALSE
from paddleocr import PaddleOCR
 
import cv2
 
import numpy as np
 
from PIL import Image, ImageDraw, ImageFont
 
from paddleocr import PaddleOCR, draw_ocr
import os
import xlwings as xw
 
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

# b=[txts[i:i] for i in range(0,len(txts),1)]
# print(b)

app = xw.App(visible=True, add_book=FALSE) # 程序可见，只打开不新建工作薄
app.display_alerts = True # 警告关闭
app.screen_updating = True # 屏幕更新关闭

path = r"D:\vscode-cuda\cudaocr-master"
wb = app.books.open(path + r'\txx.xlsx')


sheet=wb.sheets.active

# sheet.range('A1').value=txts
sheet.range('A1').options(transpose=True).value=txts

wb.save()