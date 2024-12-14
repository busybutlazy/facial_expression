# Download dataset

import kagglehub
from pathlib import Path
import os

# Download dataset
dataset_path=Path.cwd().joinpath("dataset/")
if not os.path.exists(dataset_path):
    path = kagglehub.dataset_download("fatihkgg/affectnet-yolo-format")
    print("Path to dataset files:", path)
    os.rename(path,dataset_path)
else:
    print("File is already exist.")
# %%

# show img
import cv2
import numpy as np
train_img_path=dataset_path.joinpath("YOLO_format/train/images")
print(train_img_path)
show_img_num=10
if os.path.isdir(train_img_path):
    img=None
    list_of_train_data_filenames=os.listdir(train_img_path)
    for f in list_of_train_data_filenames:
    
        if type(img)!=np.ndarray:
            # First img and show the shape of img.
            img=cv2.imread(os.path.join(train_img_path,f))
            print(f"num of train files: {len(list_of_train_data_filenames)}")
            print(f'Shape of image: {img.shape}')
        else:
            img=np.concatenate((img,cv2.imread(os.path.join(train_img_path,f))),axis=1)
        show_img_num-=1
        if show_img_num<=1:
            cv2.imshow("Img"+str(show_img_num-9), img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            break
# %%
else:
    print("There are no files.")

