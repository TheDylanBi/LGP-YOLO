import warnings

warnings.filterwarnings('ignore')
from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO('runs/detect/yolo-bdf2(best)/weights/best.pt')
    #model = YOLO('runs/detect/yolo-ts-200/weights/best.pt')
    model.predict(source='C:/Users/hp-pc/Desktop/test.jpg',
                  imgsz=640,
                  project='C:/Users/hp-pc/Desktop/vs/YOLOv8',
                  name='4',
                  save=True,
                  conf=0.2,
                  iou=0.5,
                  )