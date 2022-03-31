# main.py

from puzzle import Puzzle

p = Puzzle()
p.print()
'''
for i in range (1, 17) :
    kurang = p.kurang(i)
    print("ubin ", i, " kurang : ", kurang)
'''

print("is solveable?", end = " ")
if (p.isSolvable()) :
    print("Y")
else :
    print("N")