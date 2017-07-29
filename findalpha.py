from sympy.solvers import nsolve     # import sympy solver 'nsolve' for numerical solution
from sympy import sin                # import trigonometric function from the sympy library
from sympy.abc import x
import math                          # import math library for using constants

# Class to find the alpha
class AlphaFind:

    # method to calculate pi:
    def picalculate(self, length, n):
        # using math library for formulating as circumfernce = 2 * pi * radius
        radius = float((length) / (math.sqrt(2 - (2 * (math.cos((math.radians(360) / n)))))))
        diameter = 2 * radius
        circumference = (length * n)
        return (float(circumference / diameter))

    # method to calculate the alpha, the angle e the angle with vertex at the center of the left circle
    def alphacalculate(self):
        # the higher the number of segmentation the more accurate pi is. so n = 500 is good
        pi = self.picalculate(1, 500)
        # numericall calculating alpha by using the 'nsolve' function of sympy library
        self.alpha = nsolve(-sin(x) + x - pi/2, 0)
        #print pi
        # returns the value of alpha
        return self.alpha

    # method to print the data calculated in 'alphacalulate' method
    def displayalpha(self):
        print "The value of alpha is: " + str(self.alpha)
        # print self.alpha

alphafind = AlphaFind()               # creating object of the class AlphaFind
alphafind.alphacalculate()            # calling the 'alphacalculate' method
alphafind.displayalpha()              # calling the 'displayalpha' method
