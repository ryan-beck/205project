from algorithm import Algorithm
from bop import MorphoGradientOp, ErodeOp

class AlgoOne(Algorithm):

    def __init__(self, slotCallback):
        super().__init__(slotCallback)


        morpho = MorphoGradientOp("Morphological Gradient", self.callback)
        self.addOperator(morpho)

        erode = ErodeOp("ErodeOp", self.callback)
        self.addOperator(erode)
