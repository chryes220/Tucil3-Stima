# main.py

from puzzle import Puzzle
from solver import Solver
import random

if __name__ == "__main__" :
    path = "../test/"
    #name = input("Masukkan nama file : ")
    name = "tc_solvable_3.txt"
    u = Puzzle()
    u.from_file(path + name)
    u.displayPuzzle()
    print()

    s = Solver(u)
    if (s.isSolvable()) :
        print("solvable")
    else :
        print("not solvable")
    s.solve()
