# main.py

from puzzle import Puzzle
from solver import Solver
import random

if __name__ == "__main__" :
    path = "test/"
    name = input("Masukkan nama file : ")
    print()

    u = Puzzle()
    u.from_file(path + name)
    print("Initial state")
    u.displayPuzzle()
    print()

    s = Solver(u)
    s.solve()
