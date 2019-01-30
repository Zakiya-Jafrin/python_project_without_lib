#kamptan august 2017
class Input:

    # creating a method to take the radius of the circle as an input provided by the user
    def inputradius(self):
        while True:
            n = raw_input("Enter the radius: R = ")  # takes the radius as an input form the user
            try:
                # The user input is tried to convert into float
                self.radius= float(n)
                # if input is negative or zero raise an exception
                if self.radius<=0:
                    raise Exception
            # if the user input not valid to convert into float then give the error message
            except ValueError:
                print('You must put an interger, not a charecter! Try again...')
            except Exception:
                print('Invalid input! Radius can not be negative or zero. Please put a postive value. Try again...')
            else:
                break
        # returns the value of the radius
        return self.radius

radius = Input()
# radius.inputradius()
