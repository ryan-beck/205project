from PyQt5.QtWidgets import QDial, QWidget
class ModDial(QWidget):

    def __init__(self, label):
        super().__init__()
        self.name = label
        self.qw = QDial()

    def getValue(self):
        return self.qw.value()
