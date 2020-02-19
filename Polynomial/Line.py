from Parabola import Parabola

class Line(Parabola):
    """
    Class representing a line with the form y = m*x + b 

    Attributes
    ----------
    coefficients : A list with the polynomial  coefficients
                   [b, m]  

    """


    def __init__(self, m, b):
        # Line of form y = m*x + b
        super().__init__(0, b, m)