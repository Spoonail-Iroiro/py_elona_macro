from PySide2.QtWidgets import QApplication, QMainWindow, QDialog, QGraphicsScene, QGraphicsView, QGraphicsRectItem, QGraphicsPixmapItem
from PySide2.QtCore import QRectF
import PySide2.QtCore as QtCore
from PySide2.QtGui import QPixmap,QCursor
from PIL.ImageQt import ImageQt
from PIL import Image
from pathlib import Path


class CanvasGraphicsScene(QGraphicsScene):
    def __init__(self,parent=None):
        super().__init__(parent)


