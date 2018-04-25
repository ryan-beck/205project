from transformoperator import TranOp
import cv2
import numpy as np

class MorphoGradientOp(TranOp):

    def __init__(self, label, slotCallback):
        super().__init__(label, slotCallback)
        self.addKnob("X", 'x')
        self.addKnob("Y", 'y')


    def transform(self, img):
        kernel = np.ones((self.tranParams['x'], self.tranParams['y']),np.uint8)
        return cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

class ErodeOp(TranOp):

    def __init__(self, label, slotCallback):
        super().__init__(label, slotCallback)
        self.addKnob("X", 'x')
        self.addKnob("Y", 'y')
        self.addKnob("Iterations", 'i')


    def transform(self, img):
        kernel = np.ones((self.tranParams['x'], self.tranParams['y']),np.uint8)
        return cv2.erode(img, kernel, iterations = (self.tranParams['i'] // 30))

# def invert(self, img):
#     img = cv2.bitwise_not(img)
#     return img
#
# def opBlur(self, img, kern):
#     return cv2.blur(img, kern)
#
# def opDialation(self, img, kern=(5,5)):
#     kernel = np.ones((kern[0],kern[1]),np.uint8)
#     return cv2.dilate(img,kernel,iterations=1)

class DialationOp(TranOp):

    def __init__(self, label, slotCallback):
        super().__init__(label, slotCallback)
        self.addKnob("X", 'x')
        self.addKnob("Y", 'x')
        self.addKnob("Iterations", 'i')

    def transform(self, img):
        kernel = np.ones((self.tranParams['x'], sefl.tranParams['y']), np.uint8)
        return cv2.erode(img, kernel, iterations = (self.tranParams['i'] // 30))
