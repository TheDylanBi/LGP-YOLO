from ultralytics import YOLO
import os


os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
if __name__ == '__main__':

    # Load a model
    model = YOLO('LGP-YOLO.yaml')

    # Train the model
    model.train(data='Datasets/cctsdb2021.yaml', epochs=200, batch=8, imgsz=640, device=0)

    # Evaluate model performance on the validation set
    metrics = model.val(data='Datasets/cctsdb2021.yaml', imgsz=640, batch=1, device=0)

    # Export the model to ONNX format
    # path = model.export(format="engine", device='0', half=True, opset=12)