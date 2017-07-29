# calculate the angle with vertex at the center of the left circle
class Findalpha:

    # The square root function to calculate the square root
    def sqrt(self, x=2.0):
        x0= x/2.0
        while True:
            sqrtofthenumber = (x0 + x/x0)/2
            if abs(sqrtofthenumber - x0) < .000001: # example threshold
                return sqrtofthenumber
            x0 = sqrtofthenumber

    # def sqrtdisplay(self):
    #     print "The square root of the number is: " + str(self.sqrt(2))

    # Function for calculating pi,
    def picalculate(self):
        # Brent-Salamin formula to calculate pi
        initialval1 = 1.0
        initialval2 = 1.0 / self.sqrt(2)
        fixdval = 1.0 / 4.0
        m = 1.0
        n = 10

        for i in range(n):
            initvaln1 = (initialval1 + initialval2) / 2
            initvaln2 = self.sqrt(initialval1 * initialval2)
            value = fixdval - m * (initialval1 - initvaln1) ** 2
            o = 2 * m
            initialval1, initialval2, fixdval, m = initvaln1, initvaln2, value, o

        #pi value calculated
        self.pi = float((initialval1 + initialval2) ** 2 / (4 * fixdval))
        self.pi_180 = self.pi/ 180
        self.pi_2 = self.pi / 2

        # returns the value of Pi
        return self.pi

    # function for calculating sin
    def sin(self, angle):
        # sin value table
        sinTable = [
            0.0,  # sin(0)
            0.17364817766693034885171662676931,  # sin(10)
            0.34202014332566873304409961468226,  # sin(20)
            0.5,  # sin(30)
            0.64278760968653932632264340990726,  # sin(40)
            0.76604444311897803520239265055542,  # sin(50)
            0.86602540378443864676372317075294,  # sin(60)
            0.93969262078590838405410927732473,  # sin(70)
            0.98480775301220805936674302458952,  # sin(80)
            1.0  # sin(90)
        ]

        # cos value table
        cosTable = [
            1.0,  # cos(0)
            0.99984769515639123915701155881391,  # cos(1)
            0.99939082701909573000624344004393,  # cos(2)
            0.99862953475457387378449205843944,  # cos(3)
            0.99756405025982424761316268064426,  # cos(4)
            0.99619469809174553229501040247389,  # cos(5)
            0.99452189536827333692269194498057,  # cos(6)
            0.99254615164132203498006158933058,  # cos(7)
            0.99026806874157031508377486734485,  # cos(8)
            0.98768834059513772619004024769344  # cos(9)
        ]
        if angle >= 0 and angle <= 90:
            a = int(angle * 0.1)
            b = angle - 10 * a
            # calculating sin using sin(A+B) formula
            return sinTable[int(a)] * cosTable[int(b)] + b * self.pi_180 * sinTable[9 - int(a)]
        elif angle > 90 and angle <= 180:
            return self.sin(180 - angle)
        else:
            print "this angle is wrong"
            exit(-1)

    # function for calculating cosine
    def cos(self, angle):
        if angle >= 0 and angle <= 90:
            return self.sin(90 - angle)
        # cosine calculated shifting the angle by 90 degrees
        else:
            print("Error. We can only calculate an angle between 0 and 90")
            exit(-1)

    # function for calculating alpha, the angle
    def computeAlpha(self):
        self.pi_180 = self.picalculate() / 180
        self.pi_2 = self.picalculate() / 2
        var = 0.1
        for i in range(20):
            alpha = self.pi_2 + self.sin(var / self.pi_180)
            var = alpha
        # returns the value of alpha
        return var

    # print the value of alpha
    def displayalpha(self):
        print "The value of alpha is: " + str(self.computeAlpha())

# creating object of the class Findalpha
alpha = Findalpha()
# calling the functions
alpha.picalculate()
alpha.computeAlpha()
alpha.displayalpha()
