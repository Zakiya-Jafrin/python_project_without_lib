import unittest
import findlength, findalpha                      # import classes to use data from those classes

length = findlength.Length()
alpha = findalpha.AlphaFind()

# No test cases for input as input exceptions has been handled.
class TestLength(unittest.TestCase):

    #checks the pi value
    def test_pi(self):
        self.assertAlmostEqual(alpha.picalculate(1, 500), 3.14157198278)

    # checks that the calculation gives a result
    def test_lengthcalculate2(self):
        self.assertTrue(length.lengthcalculate())

    # cheks that the user is non zero positive
    def test_lengthcalculate(self):
        self.assertGreater(length.lengthcalculate(), 0)


def main():
    unittest.main()

if __name__ == '__main__':
    main()