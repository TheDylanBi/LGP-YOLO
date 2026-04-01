#coding: utf-8
import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
from ultralytics import YOLO
import matplotlib
matplotlib.use('TkAgg')

if __name__ == '__main__':
    model = YOLO('runs/detect/yolov8-l/weights/best.pt')
    model.val(data='Datasets/tt1ook.yaml',
              split='val',
              save_json=True,
              project='RUN/Model',
              name='YOLOv8'
              )
