# main.py

from puzzle import Puzzle
from solver import Solver

f = input("Masukkan nama file : ")

p = Puzzle()
p.displayPuzzle()
if (p.isSolved()) :
    print("solved")
'''
for i in range (1, 17) :
    kurang = p.kurang(i)
    print("ubin ", i, " kurang : ", kurang)
'''
s = Solver(p)
if (s.isSolvable()) :
    print("solvable")
else :
    print("not solvable")
s.solve()
