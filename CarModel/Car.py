class Car:

#Constructor
#The self is like a bubble that caches the variables

    def __init__(self, Brand, Doors, colour, Price):
        self.Brand = Brand
        self.Doors = Doors
        self.Price = Price
        self.Colour = colour;
        self.MilesDriven = 0


#Auto generated toString
    def __repr__(self):
        return str(self.__dict__)

#Methods below

    def changeCarColour(self, colourToChangeTo):
        self.Colour = colourToChangeTo
        print("Your colour is changed to ", colourToChangeTo)


    def driveCar(self):
        currentMiles = self.MilesDriven
        currentMiles += 10
        self.MilesDriven = currentMiles
        print("You have driven 10 miles. Total:" + str(self.MilesDriven))

#getters and setters in python

    def getPrice(self):
        print(self.Price)

    def setPrice(self, newPrice):
        self.Price = newPrice
        print("New Price is ", newPrice)

#We can remove items from the self or the fake cache
    def removePrice(self):
        del self.Price
        print("Price has been deleted!")
