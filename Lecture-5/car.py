## A specific type of vehicle - car.
#
from vehicle import Vehicle

class Car(Vehicle) :
   ## Constructs a car object.
   #
   def __init__(self) :
      # Call the superclass constructor to define its instance variables.
      super().__init__(4)
      
      # This instance variable is set by the subclass.
      self._plateNumber = "??????"

   ## Sets the license plate number of the car.
   #  @param newValue a string containing the number
   #
   def setLicensePlateNumber(self, newValue) :
      self._plateNumber = newValue

   ## Gets a description of the car.
   #  @return a string containing the description
   #
   def getDescription(self) : 
      return "A car with license plate " + self._plateNumber

