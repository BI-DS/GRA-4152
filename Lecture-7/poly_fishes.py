class Fish:
    def __init__(self, fishType):
        self._type = fishType
    
    def swim(self):
        print('The {} is swimming'.format(self._type))

    def swim_backwards(self):
        raise NotImplementedError
    
    def skeleton(self):
        raise NotImplementedError

    def summarizeMyfish(self):
        self.swim()
        self.swim_backwards()
        self.skeleton()

class Shark(Fish):
    def __init__(self, fishType):
        super().__init__(fishType)

    def swim_backwards(self):
        print("The shark cannot swim backwards, but can sink backwards.")

    def skeleton(self):
        print("The shark's skeleton is made of cartilage.")


class ClownFish(Fish):
    def __init__(self, fishType):
        super().__init__(fishType)

    def swim_backwards(self):
        print("The clownfish can swim backwards.")

    def skeleton(self):
        print("The clownfish's skeleton is made of bone.")


myShark     = Shark(fishType = 'shark')
myClownfish = ClownFish(fishType = 'clownfish')

myShark.summarizeMyfish()
myClownfish.summarizeMyfish()
