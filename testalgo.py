from algorithm import Algorithm
from bop import MorphoGradientOp, ErodeOp

# CST 205, Sandbox for testing algorithms,
# Ryan Beck & Daniel Kharlamov, 5/2018

class AlgoOne(Algorithm):

    def __init__(self, slotCallback):
        super().__init__(slotCallback)


        erode = ErodeOp("Erode", self.callback)
        self.addOperator(erode)

        morpho = MorphoGradientOp("Morphological Gradient", self.callback)
        self.addOperator(morpho)

        erode2 = ErodeOp("Erode Post", self.callback)
        self.addOperator(erode2)

        erode3 = ErodeOp("Erode Post Post", self.callback)
        self.addOperator(erode3)
