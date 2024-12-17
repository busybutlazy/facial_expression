from PIL import Image
from ultralytics import YOLO
from pathlib import Path
# Create your models here.
print("Start loading model.")
model = YOLO(model=Path.cwd().joinpath("runs/detect/train/weights/best.pt"))
print("End loading.")
mood_dict = {
    0:"Anger",
    1:"Contempt",
    2:"Disgust",
    3:"Fear",
    4:"Happy",
    5:"Neutral",
    6:"Sad",
    7:"Surprise",}



def predict_image(image):
    img=image.resize((640,640))
    results=model(img,conf=0.5)
    for r in results:
        if not len(r.boxes.cls):
            return "Does there any human in picture ?"
        elif len(r.boxes.cls):
            return f"You seem {mood_dict[int(r.boxes.cls[0])]}."
        else :
            moods=[mood_dict[int(r.boxes.cls[i])] for i in range(len(r.boxes.cls[0]))]
            s="You seem "
            for i in range(len(moods)):
                s+=moods[i]
                if i == len(moods)-1:
                    s+="."
                else:
                    s+=" or "
            return s
        
    # predict by model