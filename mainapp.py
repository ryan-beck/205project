import sys
from PyQt5.QtWidgets import QApplication, QWidget, QSlider, QDial, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QFileDialog, QComboBox, QStackedLayout
from PyQt5.QtGui import QIcon, QPixmap, QImage
from PyQt5.QtCore import pyqtSlot, Qt
from PIL.ImageQt import ImageQt
from PIL import Image
import numpy as np
import cv2
from testalgo import AlgoOne
from testalgo2 import AlgoTwo
from finalAlgos import RedNeg, BlueNeg, GreenNeg
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
        options = QFileDialog.Options()
        options|= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"Select Image", "","Image Files (*.png *.jpg)", options=options)

        img = cv2.imread(fileName)
        print("before", img.shape)
        while(img.shape[0] > 300 or img.shape[1] > 1000):
            img = cv2.resize(img,None,fx=9/10, fy=9/10, interpolation = cv2.INTER_CUBIC)
        print("after", img.shape)

        self.gimg = img

        self.image.setPixmap(self.cvToPix(img))


        layout = QVBoxLayout()

        #Creating Buttons

        filterNames = ["Select Filter", "Red x Negative", "Blue x Negative", "Green x Negative"]
        buttonsLayout = QHBoxLayout()
        self.openButton = QPushButton('Open', self)
        self.saveButton = QPushButton('Save', self)
        self.shareButton = QPushButton('Share With Email', self)

        self.openButton.clicked.connect(self.openButtonClicked)
        self.saveButton.clicked.connect(self.saveButtonClicked)
        self.shareButton.clicked.connect(self.shareButtonClicked)
        self.comboBox = QComboBox()
        self.comboBox.addItems(filterNames)

        self.comboBox.currentIndexChanged.connect(self.applyFilterClicked)

        buttonsLayout.addWidget(self.openButton)
        buttonsLayout.addWidget(self.saveButton)
        buttonsLayout.addWidget(self.shareButton)
        buttonsLayout.addWidget(self.comboBox)

        layout.addLayout(buttonsLayout)
        layout.addWidget(self.appNameLabel)
        layout.addWidget(self.image)

        self.firstLabel = QLabel("Choose Your Filter")

        self.stacked_layout = QStackedLayout() # Creates stacked layout to hold the dial layouts for algos
        self.stacked_layout.addWidget(self.firstLabel)
        layout.addLayout(self.stacked_layout)

        self.setLayout(layout)
        self.setGeometry(100, 100, 300, 175)
        self.imgMan()
        self.show()

    def createAlgoLayout(self):
        self.newLayout = self.tca.getModBox()
        self.newWidget = QWidget()
        self.newWidget.setLayout(self.newLayout)
        self.stacked_layout.addWidget(self.newWidget)

    def applyFilterClicked(self, value):
        print(self.stacked_layout.count())
        if value == 1:
            self.tca = RedNeg(self.imgMan)
        elif value == 2:
            self.tca = BlueNeg(self.imgMan)
        elif value == 3:
            self.tca = GreenNeg(self.imgMan)
        self.createAlgoLayout()
        self.stacked_layout.setCurrentIndex(self.stacked_layout.count()-1)


    def openButtonClicked(self):
        options = QFileDialog.Options()
        options|= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"Select Image", "","Image Files (*.png *.jpg)", options=options)

        img = cv2.imread(fileName)
        while(img.shape[0] > 300 or img.shape[1] > 1000):
            img = cv2.resize(img,None,fx=9/10, fy=9/10, interpolation = cv2.INTER_CUBIC)

        self.gimg = img

        self.image.setPixmap(self.cvToPix(img))

    def saveButtonClicked(self):

        w = len(self.final)
        h = len(self.final[0])

        cv2.imwrite("Images/lol.png", self.final)
        print('Save Button Clicked')

    def shareButtonClicked(self):

        email = 'student@csumb.edu'
        server = smtplib.SMTP(email, 587)
        server.starttls()
        server.login(email, 'Password')

        msg = "Hello"

        server.sendmail(email, email, msg)
        server.quit()

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

        self.final = self.tca.render(self.gimg)
        self.image.setPixmap(self.cvToPix(self.final))


app = QApplication(sys.argv)
engine = ArtEngine()
sys.exit(app.exec_())
