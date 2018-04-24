from modslider import ModSlider
from moddial import ModDial
from PyQt5.QtWidgets import QHBoxLayout



class Algorithm():

    def __init__(self, slotCallback):
        self.layout = QHBoxLayout()
        self.callback = slotCallback
        self.opList = []


    # Get the mod box with all widgets inside
    # use mainAppLayout.addLayout(inst.getModBox()) to add widgets to bottom
    def getModBox(self):
        return self.layout

    def getOperators(self):
        return self.opList

    def render(self, img):
        final_img = img
        for op in self.opList:
            final_img = op.transform(final_img)

        return final_img


    def addOperator(self, op):
        self.opList += [op]
        self.layout.addLayout(op.getControlLayout())
