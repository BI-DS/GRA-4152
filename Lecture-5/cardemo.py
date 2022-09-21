##
#  This program provides a simple test of the Car class.
#

from car import Car

def main() :
   aPlainCar = Car() 
   printInfo(aPlainCar) 

   aLimo = Car() 
   aLimo.setLicensePlateNumber("W00H00") 
   aLimo.setNumberOfTires(8)
   printInfo(aLimo)
   
def printInfo(car) :
   print(car.getDescription())
   print("Tires:", car.getNumberOfTires())

# Start the program.
main()

