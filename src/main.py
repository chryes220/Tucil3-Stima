# main.py

from puzzle import Puzzle
from solver import Solver
import random

if __name__ == "__main__" :
    path = "test/"
    u = Puzzle()

    choice = input("Use randomized puzzle? [y/n] ")
    if (choice == 'n') :
        name = input("Input file name : ")
        u.from_file(path + name)
    print()
    
    print("Initial state")
    u.displayPuzzle()
    print()

    s = Solver(u)
    s.solve()
