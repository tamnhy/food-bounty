import os
import shutil
os.makedirs("/output", exist_ok=True)
shutil.copy("12.jpg", "/output/image.png")
