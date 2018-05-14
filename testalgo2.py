from algorithm import Algorithm
from bop import DilationOp, MorphoGradientOp, NegateOp, BlurOp, TopHatOp, ChangeColorOp

# CST 205, Sandbox for testing algorithms,
# Ryan Beck & Daniel Kharlamov, 5/2018

class AlgoTwo(Algorithm):

    def __init__(self, slotCallback):
        super().__init__(slotCallback)

        blue = ChangeColorOp("Blue Value", self.callback, 0)
        self.addOperator(blue)

        # green = ChangeColorOp("Green Value", self.callback, 1)
        # self.addOperator(green)

        # red = ChangeColorOp("Red Value", self.callback, 2)
        # self.addOperator(red)

        negate = NegateOp("Negate", self.callback)
        self.addOperator(negate)
        # #
        # topHat = TopHatOp("Top Hat", self.callback)
        # self.addOperator(topHat)
        # #
        # blur = BlurOp("Blur", self.callback)
        # self.addOperator(blur)
        #
        # dilate = DilationOp("Dilate", self.callback)
        # self.addOperator(dilate)
        #
        # morpho = MorphoGradientOp("Morphological Gradient", self.callback)
        # self.addOperator(morpho)

        # green = ChangeColorOp("Green Value", self.callback, 0)
        # self.addOperator(green)
