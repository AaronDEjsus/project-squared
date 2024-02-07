#ignore
import os

# import your functions here (example):

#    #folder  #file name        #function name
from programs.utilities.calculator import calculator
from programs.misc.hello import hello
from programs.games.rpg import rpg
from programs.games.quizGame import quizGame

#Catagories for programs:
catagories = ["Miscellaneous",
              "Utilities",
              "Games"]

#add your imported function here:
misc = [hello]

utilities = [calculator]

games = [rpg, quizGame]

def main():
    #clear screen
    while (True):
        # Choose Catagory
        os.system('cls' if os.name == 'nt' else 'clear')

        print("Choose a catagory: \n")

        #show all catagory options
        for i, option in enumerate(catagories):
            print(f'{i+1}. {option}\n')

        #validate input is in range
        catagory = get_input(catagories, False)
        
        # Choose Program
        clear_screen()
        
        print("Choose a program: \n")

        programs = None
        match (catagory):
            case 0:              
                programs = misc
            case 1:
                programs = utilities
            case 2:
                programs = games

        #show all programs options in catagory
        for i, option in enumerate(programs):
            print(f'{i+1}. {option.__name__}.py\n')

        print(f'{len(programs)+1}. Back\n')
        
        #validate input is in range
        program = get_input(programs, True)

        if (program == len(programs)-1):
            continue

        clear_screen()

        programs[program]()

        return

def get_input(options, back):
    choice = -1
    while choice > len(options) or choice < 0:
        try:
            if back:
                choice = int(input(f'(1-{len(options)+1}): ')) - 1
                if choice == len(options):
                    return choice-1
            else:
                choice = int(input(f'(1-{len(options)}): ')) - 1

        except ValueError:
            continue

    return choice
        
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == "__main__":
    main()