# main.py

from puzzle import Puzzle
from solver import Solver
import random

if __name__ == "__main__" :
    quit = False
    while (not quit) :
        path = "test/"
        u = Puzzle()

        print("Type 'quit' to quit program anytime")
        choice = input("Use randomized puzzle? [y/n] ")
        if (choice == 'quit') :
            quit = True
        else :
            if (choice == 'n') :
                name = input("Input file name : ")
                if (name == 'quit') :
                    quit = True
                else :
                    u.from_file(path + name)
            
            if (not quit) :
                print()
                
                print("Initial state")
                u.displayPuzzle()
                print()

                s = Solver(u)
                s.solve()
