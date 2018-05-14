from transformoperator import TranOp
import cv2
import numpy as np

class MorphoGradientOp(TranOp):

    def __init__(self, label, slotCallback):
        super().__init__(label, slotCallback)
        self.addKnob("X", 'x')
        self.addKnob("Y", 'y')

    def transform(self, img):
        kernel = np.ones((self.tranParams['x']//5, self.tranParams['y']//5),np.uint8)
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

class DilationOp(TranOp):

    def __init__(self, label, slotCallback):
        super().__init__(label, slotCallback)
        self.addKnob("X", 'x')
        self.addKnob("Y", 'y')
        self.addKnob("Iterations", 'i')

    def transform(self, img):
        kernel = np.ones((self.tranParams['x'], self.tranParams['y']), np.uint8)
        return cv2.dilate(img, kernel, iterations = (self.tranParams['i'] // 50))

class NegateOp(TranOp):

    def __init__(self, label, slotCallback):
        super().__init__(label, slotCallback)
        self.addKnob("Scale", 's')

    def transform(self, img):
        img = (self.tranParams['s']-img)
        return img

class ChangeColorOp(TranOp):
    def __init__(self, label, slotCallback, color): # Color: Blue = 0, Green = 1, Red = 2
        super().__init__(label, slotCallback)
        self.color = color
        self.addKnob("Scale", 's')

    def transform(self, img):
        timg = img
        timg[:,:,self.color] += (self.tranParams['s']//20)
        return timg



class BlurOp(TranOp):
    def __init__(self, label, slotCallback):
        super().__init__(label, slotCallback)
        self.addKnob("Iterations", 'i')

    def transform(self, img):
        kernel = np.ones((5,5), np.float32)/self.tranParams['i']
        return cv2.filter2D(img, -1, kernel)


class TopHatOp(TranOp):
    def __init__(self, label, slotCallback):
        super().__init__(label, slotCallback)
        self.addKnob("X", 'x')
        self.addKnob("Y", 'y')

    def transform(self, img):
        kernel = np.ones((self.tranParams['x'], self.tranParams['y']), np.uint8)
        return cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
