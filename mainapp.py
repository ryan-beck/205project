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

        img = cv2.imread('img.jpg')

        self.gimg = img

        self.image.setPixmap(self.cvToPix(img))


        layout = QVBoxLayout()
        layout.addWidget(self.appNameLabel)
        layout.addWidget(self.image)


        layout.addLayout(self.tca.getModBox())

        self.setLayout(layout)
        self.setGeometry(100, 100, 300, 175)
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

        final = self.tca.render(self.gimg)

        self.image.setPixmap(self.cvToPix(final))


    def testAlgo(self, img, a_kern, a_iter, b_kern, a_ratio, b_ratio):
        a = self.opErode(img, a_kern, a_iter)
        sum = cv2.addWeighted(a, a_ratio, self.gimg, (1.0-a_ratio), 0.0)
        b = self.opMorphoGradient(sum, b_kern)
        return cv2.addWeighted(b, a_ratio, self.gimg, (1.0-b_ratio), 0.0)

    # Erosion Operator
    def opErode(self, img, kern=(5,5), iter=1):
        kernel = np.ones((kern[0],kern[1]),np.uint8)
        return cv2.erode(img, kernel, iterations = iter)

    # Morphological Gradient Operator
    def opMorphoGradient(self, img, kern=(5,5)):
        kernel = np.ones((kern[0],kern[1]),np.uint8)
        return cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

app = QApplication(sys.argv)
engine = ArtEngine()
sys.exit(app.exec_())
