class Seeker():

    def __init__(self):
        self.__previous_guess = None
        self.__current_guess = None
        self.__total_guesses = 0

    def set_current_guess(self, current_guess):
        self.__current_guess = current_guess
    
    def get_current_guess(self):
        return self.__current_guess

    def set_previous_guess(self, previous_guess):
        self.__previous_guess = previous_guess
    
    def get_previous_guess(self):
        return self.__previous_guess

    def add_guess(self):
        self.__total_guesses += 1

    def get_guesses(self):
        return self.__total_guesses