##
#  This module defines 2 classes that share similar methods with different forms 
#


## A specific fish with 3 different methods
#
class Shark:
    def swim(self):
        print("The shark is swimming.")

    def swim_backwards(self):
        print("The shark cannot swim backwards, but can sink backwards.")

    def skeleton(self):
        print("The shark's skeleton is made of cartilage.")

## A specific fish with 3 different methods
#
class Clownfish:
    def swim(self):
        print("The clownfish is swimming.")

    def swim_backwards(self):
        print("The clownfish can swim backwards.")

    def skeleton(self):
        print("The clownfish's skeleton is made of bone.")


## A function that expects a superclass as argument 
#
def in_the_ocean(fish):
    fish.swim()
    fish.swim_backwards()
    fish.skeleton()

##
#  Test program: show how Python can use different class types in the same 
#  way. That is, using their methods in a polymorphic way. 
#
myShark     = Shark()
myClownfish = Clownfish()

in_the_ocean(myShark)
in_the_ocean(myClownfish)
