# main.py

from puzzle import Puzzle
from solver import Solver
import random

if __name__ == "__main__" :
    #name = input("Masukkan nama file : ")
    name = "tc1.txt"
    u = Puzzle()
    u.from_file(name)
    u.displayPuzzle()
    print()

    s = Solver(u)
    if (s.isSolvable()) :
        print("solvable")
    else :
        print("not solvable")
    s.solve()
