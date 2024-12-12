import kagglehub
from pathlib import Path
# Download latest version

path=Path.cwd().joinpath("fatihkgg/affectnet-yolo-format")

path = kagglehub.dataset_download(str(path))



print("Path to dataset files:", path)