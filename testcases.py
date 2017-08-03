import unittest
import math
import computelength, projectscratch1                      # import classes to use data from those classes

length = computelength.Computelength()
alpha = projectscratch1.Findalpha()
print "Test the square root function, Insert a number: "
a = float(raw_input())
print "Test the sin function, Insert a number ranged(0 to 90): "
b = float(raw_input())


# No test cases for input as input exceptions has been handled.
class TestLength(unittest.TestCase):

    #checks wether the srt root function genertaes the same value
    def test_sqrt(self):
        self.assertAlmostEqual(alpha.sqrt(a), math.sqrt(a))

    #checks the pi value
    def test_pi(self):
        self.assertAlmostEqual(alpha.picalculate(), math.pi)

    # checks the sin function if mathes with tha mayh library sin function value upto 5 digits
    def test_sin(self):
        x1 = alpha.sin(b)
        y1 = math.sin(math.radians(b))
        x = str(x1)
        y = str(y1)
        self.assertAlmostEqual(x[:5], y[:5])

def main():
    unittest.main()

if __name__ == '__main__':
    main()