# solver.py

from asyncio.windows_events import NULL
from puzzle import Puzzle

class PriorityQueue :
    def __init__(self) :
        self.queue = [] # queue of tuple (puzzle, cost, level)

    def len(self) :
        return len(self.queue)

    def enqueue(self, puzzle, val, lv) :
        # cost paling kecil di paling depan antrian
        i = 0
        while (i < len(self.queue) and self.queue[i][1] < val) :
            i += 1
        self.queue.insert(i, (puzzle, val, lv))
    
    def dequeue(self) :
        val = self.queue.pop(0)
        return val


class Solver :
    def __init__(self, puzzle) :
        self.__puzzle = Puzzle()
        self.__puzzle.copy(puzzle)
        self.__node_count = 1 # jumlah simpul yang dibangkitkan
        self.__queue = PriorityQueue() # antrian dari simpul yang telah dibangkitkan
        self.__fin = False

    def kurang(self, no_ubin) :
        loc = self.__puzzle.locate(no_ubin)
        jml = 0
        for i in range (loc, 17) :
            if (no_ubin > self.__puzzle.getByLoc(i)) :
                jml += 1
        return jml

    def isSolvable(self) :
        kurang = 0
        for i in range (1, 17) :
            kurang += self.kurang(i)
        # tentukan X, tentukan apakah ubin diarsir atau tidak
        loc_empty = self.__puzzle.locate(16) - 1
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

    def branchBound(self, puzzle, lv) :
        # memeriksa simpul dan membangkitkan anak-anaknya
        if (puzzle.isSolved()) :
            # finished
            self.__fin = True
        else :
            # urutan pencarian : up, right, down, left
            # bangkitkan semua simpul
            i = self.__puzzle.locIdx(16)[0]
            j = self.__puzzle.locIdx(16)[1]
            if (i != 0) :
                child = self.up(i,j)
                if (child != NULL) :
                    cost = lv + 1 + child.countCost()
                    self.__queue.enqueue(child, cost, lv + 1)
            if (j != 3) :
                child = self.right(i,j)
                if (child != NULL) :
                    cost = lv + 1 + child.countCost()
                    self.__queue.enqueue(child, cost, lv + 1)
            if (i != 3) :
                child = self.down(i,j)
                if (child != NULL) :
                    cost = lv + 1 + child.countCost()
                    self.__queue.enqueue(child, cost, lv + 1)
            if (j != 0) :
                child = self.left(i,j)
                if (child != NULL) :
                    cost = lv + 1 + child.countCost()
                    self.__queue.enqueue(child, cost, lv + 1)
        

    def solve(self) :
        level = 0
        if (self.isSolvable()) :
            # do something
            # branch and bound
            print("Puzzle dicari dengan metode branch and bound...")
            self.__queue.enqueue(self.__puzzle, 0, 0)
            while (not self.__fin) :
                head = self.__queue.dequeue()

                head[0].displayPuzzle()
                print("Level : ", head[2])
                print("Cost : " , head[1])
                print()

                
                self.branchBound(head[0], head[2])
                
                #self.__fin = True
                if (self.__fin) :
                    print("This is the final state")

        else :
            print("Puzzle tidak dapat diselesaikan")


    def up(self, i, j) :
        # loc_empty = self.__puzzle.locate(16)
        child = Puzzle()
        child.copy(self.__puzzle)
        if (i != 0) :
            # ubin kosong tidak berada di baris dengan indeks 0, tukar dengan ubin atas
            above = child.getByIdx(i-1, j)
            child.setByIdx(i,j, above)
            child.setByIdx(i-1, j, 16)
            return child
        else :
            return NULL

    def down(self, i, j) :
        child = Puzzle()
        child.copy(self.__puzzle)
        if (i != 3) :
            # ubin kosong tidak berada di baris dengan indeks 3, tukar dengan ubin bawah
            below = child.getByIdx(i+1, j)
            child.setByIdx(i,j, below)
            child.setByIdx(i+1, j, 16)
            return child
        else :
            return NULL
    
    def left(self, i, j) :
        child = Puzzle()
        child.copy(self.__puzzle)
        if (j != 0) :
            # ubin kosong tidak berada di kolom dengan indeks 0, tukar dengan ubin kiri
            left = child.getByIdx(i, j-1)
            child.setByIdx(i,j, left)
            child.setByIdx(i, j-1, 16)
            return child
        else :
            return NULL

    def right(self, i, j) :
        child = Puzzle()
        child.copy(self.__puzzle)
        if (j != 3) :
            # ubin kosong tidak berada di kolom dengan indeks 3, tukar dengan ubin kanan
            right = child.getByIdx(i, j+1)
            child.setByIdx(i,j, right)
            child.setByIdx(i, j+1, 16)
            return child
        else :
            return NULL
