# puzzle.py
from asyncio.windows_events import NULL
import random

class Puzzle :
    # Setiap ubin pada puzzle ditandai angka [1..16], dengan ubin bernilai 16 adalah ubin kosong
    def __init__(self) :
        self.__buffer = [[-1 for j in range (4)] for i in range (4)]
        self.__sequence = [] # berisi urutan movement yang menghasilkan kondisi puzzle, relatif dari akar
        # secara default bernilai random
        self.random()
        #self.create_final()
    
    def from_file(self, filename) :
        try :
            f = open(filename, "r")
            for i in range (4) :
                line = f.readline().strip()
                nums = line.split(' ')
                for j in range (4) :
                    self.__buffer[i][j] = int(nums[j])
        except FileNotFoundError:
            print("Wrong file name!")
            print("Generating random puzzle...")
    
    def add_movement(self, move) :
        self.__sequence.append(move)

    def get_movement(self, i) :
        return self.__sequence[i]

    def copy(self, puzzle) :
        # __buffer is initialized
        for i in range (4) :
            for j in range (4) :
                self.__buffer[i][j] = puzzle.getByIdx(i,j)
        for i in range (len(puzzle.getMoves())) :
            self.add_movement(puzzle.get_movement(i))

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
        print("╔═══╦═══╦═══╦═══╗")
        for i in range (4) :
            print("║", end=" ")
            for j in range (4) :
                if (self.__buffer[i][j] != 16) :
                    print(self.__buffer[i][j], end = "")
                else :
                    print(" ", end=" ")
                if (self.__buffer[i][j] < 10) :
                    print(" ", end="")
                print("║", end=" ")
            print()
            if(i != 3):
                print("╠═══╬═══╬═══╬═══╣")
        print("╚═══╩═══╩═══╩═══╝")

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
            if (not found) :
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

    def equals(self, puzzle) :
        eq = True
        for i in range (4) :
            for j in range (4) :
                if (self.__buffer[i][j] != puzzle.getByIdx(i,j)) :
                    eq = False
        return eq
    
    def getMoves(self) :
        return self.__sequence

    def up(self) :
        i = self.locIdx(16)[0]
        j = self.locIdx(16)[1]
        if (i != 0) :
            # ubin kosong tidak berada di baris dengan indeks 0, tukar dengan ubin atas
            above = self.getByIdx(i-1, j)
            self.setByIdx(i,j, above)
            self.setByIdx(i-1, j, 16)
            self.add_movement('u')

    def down(self) :
        i = self.locIdx(16)[0]
        j = self.locIdx(16)[1]
        if (i != 3) :
            # ubin kosong tidak berada di baris dengan indeks 3, tukar dengan ubin bawah
            below = self.getByIdx(i+1, j)
            self.setByIdx(i,j, below)
            self.setByIdx(i+1, j, 16)
            self.add_movement('d')
    
    def left(self) :
        i = self.locIdx(16)[0]
        j = self.locIdx(16)[1]
        if (j != 0) :
            # ubin kosong tidak berada di kolom dengan indeks 0, tukar dengan ubin kiri
            left = self.getByIdx(i, j-1)
            self.setByIdx(i,j, left)
            self.setByIdx(i, j-1, 16)
            self.add_movement('l')

    def right(self) :
        i = self.locIdx(16)[0]
        j = self.locIdx(16)[1]
        if (j != 3) :
            # ubin kosong tidak berada di kolom dengan indeks 3, tukar dengan ubin kanan
            right = self.getByIdx(i, j+1)
            self.setByIdx(i,j, right)
            self.setByIdx(i, j+1, 16)
            self.add_movement('r')