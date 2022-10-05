import random
class Hider():

    def __init__(self):
        self.__location = random.randint(1,1000)

    def get_location(self):
        return self.__location