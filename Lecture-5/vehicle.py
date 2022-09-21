##
#  This module defines classes that model vehicle classes.
#

## A generic vehicle superclass.
#
class Vehicle :
   ## Constructs a vehicle object with a given number of tires.
   #  @param numberOfTires the number of tires on the vehicle
   #
   def __init__(self, numberOfTires) :
      self._numberOfTires = numberOfTires
      
   ## Gets the number of tires on the vehicle.
   #  @return number of tires
   #
   def getNumberOfTires(self) : 
      return self._numberOfTires 

   ## Changes the number of tires on the vehicle.
   #  @param newValue the number of tires
   #
   def setNumberOfTires(self, newValue) :
      self._numberOfTires = newValue
      
   ## Gets a description of the vehicle.
   #  @return a string containing the description
   #
   def getDescription(self) :
      return "A vehicle with " + self._numberOfTires + " tires"


