import os
import shutil
os.makedirs("/output", exist_ok=True)
shutil.copy("food.png", "/output/image.png")
