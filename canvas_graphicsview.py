from canvas_graphics_scene import CanvasGraphicsScene
from PySide2.QtWidgets import QGraphicsRectItem, QGraphicsPixmapItem
from PySide2.QtGui import QPixmap,QCursor,QPen,QImage
from PIL.ImageQt import ImageQt
from PIL import Image
from util import *

from PySide2 import QtCore, QtWidgets


class CanvasGraphicsView(QtWidgets.QGraphicsView):
    capture_complete = QtCore.Signal()
    def __init__(self,parent=None):
        super().__init__(parent)

        self.image = None
        self.rect_item = None
        self.start_pos = None


    def setup_scene(self,img:Image):
        #if img.mode != "RGB":
            #img = img.convert("RGB")
        self.image = img
        scene = CanvasGraphicsScene()
        self.setScene(scene)

        #scene固有の初期化
        qtimg = ImageQt(self.image)
        pixmap = QPixmap.fromImage(qtimg).copy()
        pixmap_item = QGraphicsPixmapItem(pixmap)
        self.scene().addItem(pixmap_item)
        pixmap_item.setPos(0,0)
        self.rect_item = QGraphicsRectItem(0,0,200,200)
        self.rect_item.setPen(QPen(QtCore.Qt.blue, 3))
        self.rect_item.hide()
        self.scene().addItem(self.rect_item)
        self.frame_rect_item = QGraphicsRectItem(0,0,self.image.width-3,self.image.height-3)
        self.frame_rect_item.setPen(QPen(QtCore.Qt.red,5))
        self.scene().addItem(self.frame_rect_item)


        self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        img = self.image
        self.setSceneRect(0,0,img.width,img.height)
        self.setFixedSize(img.width,img.height)

        self._dragging = False
        pass

    def mousePressEvent(self, event):
        event.accept()
        if event.button() == QtCore.Qt.MouseButton.RightButton:
            #self._parent_window.accepted()
            self.capture_complete.emit()
            return
        else:
            self._dragging = True
            orig_pos = self.mapFromGlobal(QCursor.pos())
            scene_pos = self.mapToScene(orig_pos)
            #self.rect_item.show()
            self.start_pos = scene_pos
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            self.capture_complete.emit()

    def mouseMoveEvent(self, event):
        event.accept()
        if self._dragging:
            orig_pos = self.mapFromGlobal(QCursor.pos())
            now_pos = self.mapToScene(orig_pos)

            s_x = self.start_pos.x()
            s_y = self.start_pos.y()
            n_x = now_pos.x()
            n_y = now_pos.y()

            self.rect_item.setRect(s_x, s_y, max(0,n_x - s_x), n_y - s_y)

            self.rect_item.show()

    def mouseReleaseEvent(self, event):
        event.accept()
        orig_pos = self.mapFromGlobal(QCursor.pos())
        now_pos = self.mapToScene(orig_pos)

        s_x = self.start_pos.x()
        s_y = self.start_pos.y()
        n_x = now_pos.x()
        n_y = now_pos.y()
        data = { "rect":(s_x,s_y,n_x,n_y)}
        res = QtWidgets.QMessageBox.information(None,"確認","この領域を保存しますか？",
                                          QtWidgets.QMessageBox.Yes,
                                          QtWidgets.QMessageBox.No)
        if res == QtWidgets.QMessageBox.Yes:
            import json
            with open(area_data_path,"w",encoding="utf-8") as f:
                json.dump(data, f)
            self.capture_complete.emit()

        self._dragging = False
        self.rect_item.hide()

