from algorithm import Algorithm
from bop import DilationOp, MorphoGradientOp, NegateOp, BlurOp, TopHatOp, ChangeColorOp, ErodeOp

class BlueNeg(Algorithm):

    def __init__(self, slotCallback):
        super().__init__(slotCallback)

        blue = ChangeColorOp("Blue Value", self.callback, 0)
        self.addOperator(blue)

        negate = NegateOp("Negate", self.callback)
        self.addOperator(negate)

class RedNeg(Algorithm):

    def __init__(self, slotCallback):
        super().__init__(slotCallback)

        red = ChangeColorOp("Red Value", self.callback, 2)
        self.addOperator(red)

        negate = NegateOp("Negate", self.callback)
        self.addOperator(negate)

class GreenNeg(Algorithm):

    def __init__(self, slotCallback):
        super().__init__(slotCallback)

        green = ChangeColorOp("Green Value", self.callback, 1)
        self.addOperator(green)

        negate = NegateOp("Negate", self.callback)
        self.addOperator(negate)

class ErodeMorph(Algorithm):

    def __init__(self, slotCallback):
        super().__init__(slotCallback)


        erode = ErodeOp("Erode", self.callback)
        self.addOperator(erode)

        morpho = MorphoGradientOp("Morphological Gradient", self.callback)
        self.addOperator(morpho)

class NegateMorph(Algorithm):

    def __init__(self, slotCallback):
        super().__init__(slotCallback)

        negate = NegateOp("Negate", self.callback)
        self.addOperator(negate)

        morpho = MorphoGradientOp("Morphological Gradient", self.callback)
        self.addOperator(morpho)

class DilateTop(Algorithm):

    def __init__(self, slotCallback):
        super().__init__(slotCallback)

        dilate = DilationOp("Dilate", self.callback)
        self.addOperator(dilate)

        topHat = TopHatOp("Top Hat", self.callback)
        self.addOperator(topHat)
