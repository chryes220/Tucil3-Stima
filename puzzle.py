# puzzle.py
import random

class Puzzle :
    # Setiap ubin pada puzzle ditandai angka [1..16], dengan ubin bernilai 16 adalah ubin kosong

    def __init__(self) :
        self.buffer = [[-1 for j in range (4)] for i in range (4)]
        self.random()

    def isIn(self, num) :
        found = False
        i = 0
        while (i < 4 and not found) :
            j = 0
            while (j < 4 and not found) :
                if (self.buffer[i][j] == num) :
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
                self.buffer[i][j] = num

    def print(self) :
        for i in range (4) :
            for j in range (4) :
                print(self.buffer[i][j], end = " ")
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
                if (self.buffer[i][j] == no_ubin) :
                    found = True
                    loc = 4*i + j + 1
                else :
                    j += 1
            i += 1
        return loc

    def getByLoc(self, loc) :
        # posisi adalah integer bernilai [1..16]
        pos = loc - 1
        i = pos // 4
        j = pos % 4
        return self.buffer[i][j]

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