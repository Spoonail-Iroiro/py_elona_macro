from pathlib import Path
from pprint import pprint
import sys,os
import json
from PIL import ImageGrab

if getattr(sys, 'frozen', False):
    app_dir = sys._MEIPASS
else:
    app_dir = os.path.dirname(os.path.abspath(__file__))
app_dir = Path(app_dir)

area_data_path = (app_dir / ".." / "area.json").resolve()
config_path = (app_dir / ".." / "config.json")

class RectImageGrab:
    def __init__(self):
        with open(area_data_path,"r",encoding="utf-8") as f:
            area_info = json.load(f)
            self.rect = area_info["rect"]
            #print(area_info)
            #image = Image.open(r"C:\Users\spoon\Pictures\comment.png")

    def grab(self):
        image = ImageGrab.grab(bbox=self.rect)
        #image.show()
        return image
