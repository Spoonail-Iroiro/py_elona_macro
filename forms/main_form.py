from PySide2.QtWidgets import QDialog
import PySide2.QtCore as QtCore
from forms.main_forms_ui import Ui_MainForm
from PIL import Image, ImageGrab
from pathlib import Path
from config import Config

path = Path(r"C:\Users\spoon\Pictures\normal_pic.png")
class MainForm(QDialog):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.ui = Ui_MainForm()
        self.ui.setupUi(self)

        #img = Image.open(path)
        cr = Config.config["capture_rect"]
        rect = (cr["x"],cr["y"],cr["width"],cr["height"])
        grab_rect = (rect[0], rect[1], rect[0]+rect[2], rect[1]+rect[3])
        print(grab_rect)
        img = ImageGrab.grab(bbox=grab_rect)
        self._img = img
        self.setFixedSize(img.width,img.height)
        self.ui.mainView.setup_scene(img)
        #scene = CanvasGraphicsScene(img,parent=self)
        #self.scene = scene
        #self.ui.mainView.setScene(scene)
        print(self.frameGeometry())
        print(self.ui.mainView.frameSize())
        print(self.ui.mainView.sizeHint())
        print(self.ui.mainView.rect())
        print(self.ui.mainView.viewport().rect())
        print(self.ui.mainView.scene().sceneRect())

    def keypressed(self):
        self.scene.addText("Hello")


