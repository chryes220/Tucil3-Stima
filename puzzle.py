# puzzle.py
import random

class Puzzle :
    # Setiap ubin pada puzzle ditandai angka [1..16], dengan ubin bernilai 16 adalah ubin kosong
    def __init__(self) :
        self.__buffer = [[-1 for j in range (4)] for i in range (4)]
        # secara default bernilai random
        self.random()
        #self.create_final()
    
    def from_file(self, filename) :
        f = open(filename, "r")
        for i in range (4) :
            line = f.readline().strip()
            nums = line.split(' ')
            for j in range (4) :
                self.__buffer[i][j] = int(nums[j])

    def copy(self, puzzle) :
        # __buffer is initialized
        for i in range (4) :
            for j in range (4) :
                self.__buffer[i][j] = puzzle.getByIdx(i,j)

    def create_final(self) :
        for i in range (4) :
            for j in range (4) :
                self.setByIdx(i,j, 4*i + j + 1)
        self.setByIdx(3,2,16)
        self.setByIdx(3,3,15)

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

    def displayPuzzle(self) :
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

    def locToIdx(self, loc) :
        pos = loc - 1
        i = pos // 4
        j = pos % 4
        return ((i, j))

    def locIdx(self, no_ubin) :
        # mengembalikan indeks dari ubin dengan nomor no_ubin
        i = 0
        found = False
        while (i < 4 and not found) :
            j = 0
            while (j < 4 and not found) :
                if (self.__buffer[i][j] == no_ubin) :
                    found = True
                else :
                    j += 1
            if (not found) :
                i += 1
        return ((i, j))

    def getByLoc(self, loc) :
        # posisi adalah integer bernilai [1..16]
        i = self.locToIdx(loc)[0]
        j = self.locToIdx(loc)[1]
        return self.__buffer[i][j]

    def isSolved(self) :
        solved = True
        for i in range (16) :
            if (i+1 != self.getByLoc(i+1)) :
                solved = False
        return solved

    def countCost(self) :
        # menghitung ongkos untuk mencapai simpul tujuan dari simpul i
        count = 0
        for i in range (1,17) :
            if (i != self.getByLoc(i) and self.getByLoc(i) != 16) :
                count += 1
        return count