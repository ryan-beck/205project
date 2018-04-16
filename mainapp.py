import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton
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
        self.image = QLabel(self);

        #img = cv2.imread('img.jpg', 0)

        layout = QVBoxLayout()
        layout.addWidget(self.appNameLabel)
        layout.addWidget(self.image)

        self.setLayout(layout)
        self.setGeometry(100, 100, 300, 175)
        self.show()

    # Converts an OpenCV image to PyQt5 image
    def cvToPix(img):
        False



app = QApplication(sys.argv)
engine = ArtEngine()
sys.exit(app.exec_())
