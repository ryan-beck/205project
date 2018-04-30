from algorithm import Algorithm
from bop import DilationOp, MorphoGradientOp, NegateOp

class AlgoTwo(Algorithm):

    def __init__(self, slotCallback):
        super().__init__(slotCallback)

        negate = NegateOp("Negate", self.callback)
        self.addOperator(negate)

        dilate = DilationOp("Dilate", self.callback)
        self.addOperator(dilate)

        morpho = MorphoGradientOp("Morphological Gradient", self.callback)
        self.addOperator(morpho)
