import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QDial
from PyQt5.QtGui import QIcon, QPixmap, QImage
from PyQt5.QtCore import pyqtSlot
from PIL.ImageQt import ImageQt
from PIL import Image
import numpy as np
import cv2


class ArtEngine(QWidget):
    def __init__(self):
        super().__init__()

        # ...
        # Widget Creation
        # ...

        self.appNameLabel = QLabel("Art Engine v0.01", self)
        self.image = QLabel(self)
        self.dial = QDial(self)
        self.dial.valueChanged.connect(self.imgMan)

        img = cv2.imread('img.jpg')


        self.image.setPixmap(self.cvToPix(img))

        #self.image.setPixmap(QPixmap('img.jpg'))

        layout = QVBoxLayout()
        layout.addWidget(self.appNameLabel)
        layout.addWidget(self.image)
        layout.addWidget(self.dial)

        self.setLayout(layout)
        self.setGeometry(100, 100, 300, 175)
        self.show()

        for i in range(0, 100):
            if i % 2 == 0:
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            self.image.setPixmap(self.cvToPix(img))

    # Converts an OpenCV image to PyQt5 image
    def cvToPix(self, img):
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        qImg = QImage(img.data, img.shape[1], img.shape[0], img.strides[0], QImage.Format_RGB888)
        qpix = QPixmap()
        qpix.convertFromImage(qImg)
        return qpix

    @pyqtSlot()
    def imgMan():
        True
        #img = cv2.imread('img.jpg')
        #self.image.setPixmap(cvToPix(self, img))







app = QApplication(sys.argv)
engine = ArtEngine()
sys.exit(app.exec_())
