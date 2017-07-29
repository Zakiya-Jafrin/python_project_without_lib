import lxml.builder
import pdb
import projectscratch1, userinput1

# Creted object of the two other classes that were required
alpha = projectscratch1.Findalpha()
radius = userinput1.Input()
E = lxml.builder.ElementMaker()

# class to compute the degree of overlap
class Computelength:

    # function to calculate the degree of overlap, that is the length
    def lengthcalculate(self):
           # calculates length taking into account the user input and alpha that was calculated in class Findalpha
           self.length= 2 * radius.inputradius() * (1 - alpha.cos(alpha.computeAlpha() / (alpha.picalculate()/180) / 2))
           # debugger
           # pdb.set_trace()
           print "The length of the overlap is: " + str(self.length)
           # returns the value of length
           return self.length

# creating object of the class Computelength
Length = Computelength()
Length.lengthcalculate()
