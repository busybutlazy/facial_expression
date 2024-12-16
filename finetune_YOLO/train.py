#Load pretrain model
from ultralytics import YOLO
try:
    model = YOLO("yolov8n.pt")
except Exception:
    print("can't load model.")


model.train(data="dataset/YOLO_format/data.yaml",
            imgsz=640,
            batch=32,
            epochs=100,
            device=0)