from Polynomial import Polynomial

class Parabola(Polynomial):

    """
    Class representing a parabola  with the form y = ax^2 + bx +c 

    Attributes
    ----------
    coefficients : A list with the polynomial  coefficients
                   [c, b, a]  

    """


    def __init__(self, a,b,c):
        # Polynomial ax^2 + bx +c 
        # Note Polynomial maps constant as first item  
        super().__init__([c,b,a])
