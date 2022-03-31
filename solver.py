# solver.py

from puzzle import Puzzle

class Solver :

    def __init__(self, puzzle) :
        self.__puzzle = Puzzle()
        self.__puzzle.copy(puzzle)
        self.__node_count = 1 # jumlah simpul yang dibangkitkan

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

    def up(self) :
        # loc_empty = self.__puzzle.locate(16)
        i = self.__puzzle.locIdx(16)[0]
        j = self.__puzzle.locIdx(16)[1]
        if (i != 0) :
            # ubin kosong tidak berada di baris dengan indeks 0, tukar dengan ubin atas
            above = self.__puzzle.getByIdx(i-1, j)
            self.__puzzle.setByIdx(i,j, above)
            self.__puzzle.setByIdx(i-1, j, 16)

    def down(self) :
        i = self.__puzzle.locIdx(16)[0]
        j = self.__puzzle.locIdx(16)[1]
        if (i != 3) :
            # ubin kosong tidak berada di baris dengan indeks 3, tukar dengan ubin bawah
            below = self.__puzzle.getByIdx(i+1, j)
            self.__puzzle.setByIdx(i,j, below)
            self.__puzzle.setByIdx(i+1, j, 16)
    
    def left(self) :
        i = self.__puzzle.locIdx(16)[0]
        j = self.__puzzle.locIdx(16)[1]
        if (j != 0) :
            # ubin kosong tidak berada di kolom dengan indeks 0, tukar dengan ubin kiri
            left = self.__puzzle.getByIdx(i, j-1)
            self.__puzzle.setByIdx(i,j, left)
            self.__puzzle.setByIdx(i, j-1, 16)

    def right(self) :
        i = self.__puzzle.locIdx(16)[0]
        j = self.__puzzle.locIdx(16)[1]
        if (j != 3) :
            # ubin kosong tidak berada di kolom dengan indeks 3, tukar dengan ubin kanan
            right = self.__puzzle.getByIdx(i, j+1)
            self.__puzzle.setByIdx(i,j, right)
            self.__puzzle.setByIdx(i, j+1, 16)