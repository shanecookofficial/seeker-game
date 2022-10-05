from seeker import Seeker
from hider import Hider
def main():

    #globals
    main_loop = True
    seeker = Seeker()
    hider = Hider()

    while main_loop == True:
        if main_loop == True:
            seeker.set_current_guess(input('Enter a location [1-1000]: '))
            try:
                seeker.set_current_guess(int(seeker.get_current_guess()))
            except:
                pass
            if isinstance(seeker.get_current_guess(),int):
                if seeker.get_current_guess() == hider.get_location():
                    print('(;.;) You found me!')
                    main_loop = False
                else:
                    if seeker.get_guesses() == 0:
                        seeker.set_previous_guess(seeker.get_current_guess())
                    else:
                        previous_difference = max(seeker.get_previous_guess(),hider.get_location()) - min(seeker.get_previous_guess(),hider.get_location())
                        current_difference = max(seeker.get_current_guess(),hider.get_location()) - min(seeker.get_current_guess(),hider.get_location())
                        if previous_difference > current_difference:
                            print('(>.<) Getting warmer!')
                        elif previous_difference < current_difference:
                            print('(^.^) Getting colder!')
                        else:
                            print('(^.^) Getting colder!')
                        seeker.set_previous_guess(seeker.get_current_guess())
                    seeker.add_guess()
            elif seeker.get_current_guess() != int:
                print(f'{seeker.get_current_guess()} is not an integer.')
            elif seeker.get_current_guess() > 1000 or seeker.get_current_guess() < 1:
                print('Please enter an integer between 1 and 1000.')
            else:
                print('Somehow something went wrong...')

if __name__ == '__main__':
    main()