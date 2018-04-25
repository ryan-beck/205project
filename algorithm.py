from modslider import ModSlider
from moddial import ModDial
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt
import cv2



class Algorithm():

    def __init__(self, slotCallback):

        self.layout = QVBoxLayout()

        self.ratioLayout = QHBoxLayout()
        self.controlLayout = QHBoxLayout()

        self.layout.addLayout(self.ratioLayout)
        self.layout.addLayout(self.controlLayout)

        self.callback = slotCallback
        self.opList = []

        self.ratioLinks = []
        self.currentLink = 0
        self.ratioDials = []


    # Get the mod box with all widgets inside
    # use mainAppLayout.addLayout(inst.getModBox()) to add widgets to bottom
    def getModBox(self):
        return self.layout

    def getOperators(self):
        return self.opList

    def render(self, img):
        final_img = img

        for i in range(len(self.opList)):
            manipulation = self.opList[i].transform(final_img)
            ratio = self.ratioLinks[i] / 360.0

            final_img = cv2.addWeighted(manipulation, ratio, final_img, (1.0-ratio), 0.0)

        return final_img

    def updateRatios(self):
        for i in range(len(self.ratioLinks)):
            self.ratioLinks[i] = self.ratioDials[i].getValue()




    def addOperator(self, op):
        self.opList += [op]

        ratioControl = QVBoxLayout()
        if len(self.opList) > 1:
            labelText = self.opList[-2].name + " x " + self.opList[-1].name + " Ratio"
        else:
            labelText = "Original x " + self.opList[-1].name + " Ratio"

        ratioLabel = QLabel(labelText)
        ratioLabel.setAlignment(Qt.AlignCenter)
        ratioDial = ModDial(str(self.currentLink))
        ratioDial.qw.valueChanged.connect(self.callback)
        self.ratioLinks += [0]
        self.ratioDials += [ratioDial]
        self.currentLink += 1
        ratioControl.addWidget(ratioLabel)
        ratioControl.addWidget(ratioDial.qw)
        self.ratioLayout.addLayout(ratioControl)

        self.controlLayout.addLayout(op.getControlLayout())
