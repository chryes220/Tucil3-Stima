# solver.py

from puzzle import Puzzle

class Solver :

    def __init__(self, puzzle) :
        self.__puzzle = Puzzle()
        self.__puzzle.copy(puzzle)

    def kurang(self, no_ubin) :
        loc = self.locate(no_ubin)
        jml = 0
        for i in range (loc, 17) :
            if (no_ubin > self.getByLoc(i)) :
                jml += 1
        return jml

    def isSolvable(self) :
        kurang = 0
        for i in range (1, 17) :
            kurang += self.kurang(i)
        # tentukan X, tentukan apakah ubin diarsir atau tidak
        loc_empty = self.locate(16) - 1
        i = loc_empty // 4
        j = loc_empty % 4
        x = 0
        if (i % 2 == 0 and j % 2 == 1) :
            x = 1 # diarsir
        elif (i % 2 == 1 and j % 2 == 0) :
            x = 1 # diarsir
        
        if ((kurang + x) % 2 == 0) :
            return True
        else :
            return False

    def isSolved(self) :
        solved = True
        for i in range (16) :
            if (i != self.getByLoc(i)) :
                solved = False
        return solved

    def solve(self) :
        if (self.isSolvable()) :
            # do something
            # branch and bound
            print("Puzzle dicari dengan metode branch and bound...")
        else :
            print("Puzzle tidak dapat diselesaikan")