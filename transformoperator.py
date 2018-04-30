from moddial import ModDial
from modslider import ModSlider
from PyQt5.QtWidgets import QVBoxLayout, QDial, QLabel
from PyQt5.QtCore import Qt


class TranOp():

    def __init__(self, label, slotCallback):
        self.name = label
        self.controls = {}
        self.callback = slotCallback
        self.layout = QVBoxLayout()
        nameLabel = QLabel(label)
        nameLabel.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(nameLabel)

        self.tranParams = {}

    def getControlLayout(self):
        return self.layout

    def getName(self):
        return self.name

    def addKnob(self, name, paramName, default=0):

        self.controls[paramName] = ModDial(name)
        self.controls[paramName].qw.valueChanged.connect(self.callback)
        self.tranParams[paramName] = default
        label = QLabel(name)
        label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(label)
        self.layout.addWidget(self.controls[paramName].qw)

    def transform(self, img):
        return img

    def updateAll(self):
        for param in self.tranParams:
            self.tranParams[param] = self.controls[param].getValue()




    def addSlider(self, name, paramName, default=0):
        self.controls[paramName] = ModSlider(name)
        self.controls[paramName].qw.valueChanged.connect(self.callback)
        self.tranParams[paramName] = default
        label = QLabel(name)
        label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(label)
        self.layout.addWidget(self.controls[paramName].qw)
