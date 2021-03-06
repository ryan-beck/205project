from PyQt5.QtWidgets import QSlider, QWidget
from PyQt5.QtCore import Qt

# CST 205, Wrapper for QSlider that makes our lives easier,
# Daniel Kharlamov, 5/2018

class ModSlider(QWidget):

    def __init__(self, label):
        super().__init__()
        self.name = label
        self.qw = QSlider(Qt.Horizontal)
        self.qw.setFocusPolicy(Qt.StrongFocus)
        self.qw.setTickPosition(QSlider.TicksBothSides)
        self.qw.setTickInterval(10)
        self.qw.setSingleStep(1)

    def getValue(self):
        return self.qw.value()
