# Load finetuned model.
from ultralytics import YOLO
from pathlib import Path
import os

model = YOLO(model=Path.cwd().joinpath("runs/detect/train/weights/best.pt"))

dataset_path=Path.cwd().joinpath("dataset/")
test_img_path=dataset_path.joinpath("YOLO_format/test/images")
label_path=dataset_path.joinpath("YOLO_format/test/labels")

results=None

list_of_train_data_filenames=os.listdir(test_img_path)

imgs=[os.path.join(test_img_path,f) for f in list_of_train_data_filenames]
labels=[os.path.join(label_path,Path(f).stem)+".txt" for f in list_of_train_data_filenames]

print(f"nums of test:{len(imgs)}")

id=0
batch=50
correct=0

for i in range(len(imgs)//batch+1):
    if id+batch<len(imgs):
        results=model(imgs[id:id+batch],conf=0.6,stream=True)
    else:
        results=model(imgs[id:-1],conf=0.6,stream=True)

    for result in results:
        f=open(labels[id],"r")
        label=f.read()[0]
        f.close()
        id+=1
        
        if not len(result.boxes.cls):
            continue
        if int(label) in result.boxes.cls:
            correct+=1        

print(f"acc:{correct/(len(imgs))}")
