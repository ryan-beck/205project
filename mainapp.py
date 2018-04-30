import sys
from PyQt5.QtWidgets import QApplication, QWidget, QSlider, QDial, QLabel, QVBoxLayout, QHBoxLayout, QPushButton
from PyQt5.QtGui import QIcon, QPixmap, QImage
from PyQt5.QtCore import pyqtSlot, Qt
from PIL.ImageQt import ImageQt
from PIL import Image
import numpy as np
import cv2
from testalgo import AlgoOne
from testalgo2 import AlgoTwo
from transformoperator import TranOp



class ArtEngine(QWidget):
    def __init__(self):
        super().__init__()

        # ...
        # Widget Creation
        # ...

        self.appNameLabel = QLabel("Art Engine v0.01", self)
        self.image = QLabel(self)


        self.tca = AlgoOne(self.imgMan)
        #self.tca = AlgoOne(self.imgMan)

        img = cv2.imread('img.jpg')
        img = cv2.resize(img,None,fx=1/2, fy=1/2, interpolation = cv2.INTER_CUBIC)

        self.gimg = img

        self.image.setPixmap(self.cvToPix(img))


        layout = QVBoxLayout()
        layout.addWidget(self.appNameLabel)
        layout.addWidget(self.image)


        layout.addLayout(self.tca.getModBox())

        self.setLayout(layout)
        self.setGeometry(100, 100, 300, 175)
        self.imgMan()
        self.show()



    # Converts an OpenCV image to PyQt5 image
    def cvToPix(self, img):
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        qImg = QImage(img.data, img.shape[1], img.shape[0], img.strides[0], QImage.Format_RGB888)
        qpix = QPixmap()
        qpix.convertFromImage(qImg)
        return qpix

    @pyqtSlot()
    def imgMan(self):

        for op in self.tca.getOperators():
            op.updateAll()
        self.tca.updateRatios()

        final = self.tca.render(self.gimg)
        self.image.setPixmap(self.cvToPix(final))


app = QApplication(sys.argv)
engine = ArtEngine()
sys.exit(app.exec_())
