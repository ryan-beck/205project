from PyQt5.QtWidgets import QDial, QWidget

# CST 205, Wrapper for QDials that makes our lives easier,
# Daniel Kharlamov, 5/2018

class ModDial(QWidget):

    def __init__(self, label):
        super().__init__()
        self.name = label
        self.qw = QDial()

    def getValue(self):
        return self.qw.value()
