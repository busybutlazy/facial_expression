from ultralytics import YOLO

model = YOLO("runs/detect/train/weights/best.pt")
metrics=model.val(data="dataset/YOLO_format/data.yaml",conf=0.45)
print(metrics.box.map)