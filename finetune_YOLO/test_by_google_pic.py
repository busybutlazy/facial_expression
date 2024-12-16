from ultralytics import YOLO
from pathlib import Path
import os

model = YOLO(model=Path.cwd().joinpath("runs/detect/train/weights/best.pt"))
pics_path=Path.cwd().joinpath("dataset/YOLO_format/picture_from_google")
list_of_train_data_filenames=os.listdir(pics_path)
imgs=[os.path.join(pics_path,f) for f in list_of_train_data_filenames]

results= model(imgs,conf=0.5,save=True)
for result in results:
    print(result.boxes)