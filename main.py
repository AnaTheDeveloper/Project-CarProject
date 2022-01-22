from CarModel.Car import Car

if __name__ == '__main__':

#Created a new object called Luke that follows the car model
    LukesCar = Car("BMW", 4, "Red", 1000)


    print(LukesCar.__repr__())
    LukesCar.changeCarColour("Blue")
    print(LukesCar.__repr__())
    LukesCar.driveCar()
    print(LukesCar.__repr__())
    LukesCar.getPrice()
    LukesCar.setPrice(2000)
    print(LukesCar.__repr__())
    LukesCar.removePrice()
    print(LukesCar.__repr__())

    AnsCar = Car("Toyota", 3, "Pink", 5000)

    print(AnsCar.__repr__())
    print(LukesCar.__repr__())
