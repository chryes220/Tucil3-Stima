# puzzle.py
import random

class Puzzle :
    # Setiap ubin pada puzzle ditandai angka [1..16], dengan ubin bernilai 16 adalah ubin kosong

    def __init__(self) :
        self.__buffer = [[-1 for j in range (4)] for i in range (4)]
        self.random()

    def copy(self, puzzle) :
        # __buffer is initialized
        for i in range (4) :
            for j in range (4) :
                self.__buffer[i][j] = puzzle.getByIdx(i,j)

    def setByIdx(self, i, j, val) :
        self.__buffer[i][j] = val

    def getByIdx(self, i, j) :
        return self.__buffer[i][j]

    def isIn(self, num) :
        found = False
        i = 0
        while (i < 4 and not found) :
            j = 0
            while (j < 4 and not found) :
                if (self.__buffer[i][j] == num) :
                    found = True
                else :
                    j += 1
            if (not found) :
                i += 1
        return found

    def random(self) :
        for i in range (4) :
            for j in range (4) :
                num = random.randint(1,16)
                while (self.isIn(num)) :
                    num = random.randint(1,16)
                self.__buffer[i][j] = num

    def print(self) :
        for i in range (4) :
            for j in range (4) :
                print(self.__buffer[i][j], end = " ")
            print()

    def locate(self, no_ubin) :
        # posisi ubin dihitung dengan persamaan 4i + j + 1 (dimulai dari posisi 1)
        # dipastikan ketemu
        found = False
        i = 0
        loc = -1
        while (i < 4 and not found) :
            j = 0
            while (j < 4 and not found) :
                if (self.__buffer[i][j] == no_ubin) :
                    found = True
                    loc = 4*i + j + 1
                else :
                    j += 1
            i += 1
        return loc

    def locIdx(self, no_ubin) :
        # mengembalikan indeks dari ubin dengan nomor no_ubin
        loc = self.locate(no_ubin) - 1
        i = loc // 4
        j = loc % 4
        return (i, j)

    def getByLoc(self, loc) :
        # posisi adalah integer bernilai [1..16]
        i = self.locIdx(self.getByLoc(loc))[0]
        j = self.locIdx(self.getByLoc(loc))[1]
        return self.__buffer[i][j]
