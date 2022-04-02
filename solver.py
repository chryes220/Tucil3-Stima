# solver.py

from asyncio.windows_events import NULL
from puzzle import Puzzle

class PriorityQueue :
    def __init__(self) :
        self.queue = [] # queue of tuple (puzzle, cost, level)

    def len(self) :
        return len(self.queue)

    def enqueue(self, puzzle, val, lv) :
        if (self.len() == 0) :
            self.queue.append((puzzle, val, lv))
        else :
            # cost paling kecil di paling depan antrian
            i = 0
            while (i < self.len() and self.queue[i][1] <= val) :
                i += 1
            self.queue.insert(i, (puzzle, val, lv))
    
    def dequeue(self) :
        val = self.queue.pop(0)
        return val

    def printQueue(self) :
        for el in self.queue :
            el[0].displayPuzzle()
            print("Cost : ", el[1])
            print("Level : ", el[2])
            print()


class Solver :
    # bikin vairabel past states yang isinya state yang udah pernah dilalui
    # jadi setiap iterasi gak bakal balik-balik lagi ke situ
    def __init__(self, puzzle) :
        self.__puzzle = Puzzle()
        self.__puzzle.copy(puzzle) # adalah start state dari puzzle, tidak diubah
        self.__node_count = 1 # jumlah simpul yang dibangkitkan
        self.__queue = PriorityQueue() # antrian dari simpul yang telah dibangkitkan
        self.__past_states = [] # list yang berisi (puzzle, cost)
        self.__sequence = []
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
            self.__sequence = puzzle.getMoves()
        else :
            # urutan pencarian : up, right, down, left
            # bangkitkan semua simpul
            i = puzzle.locIdx(16)[0]
            j = puzzle.locIdx(16)[1]

            if (i != 0) :
                child = Puzzle()
                child.copy(puzzle)
                child.up()
                cost = lv + 1 + child.countCost()
                if (not self.isPast(child, cost)) :
                    self.__queue.enqueue(child, cost, lv + 1)
                    self.__past_states.append((child, cost))
                #print("up")
                #child.displayPuzzle()
            if (j != 3 ) :
                child = Puzzle()
                child.copy(puzzle)
                child.right()
                cost = lv + 1 + child.countCost()
                if (not self.isPast(child, cost)) :
                    self.__queue.enqueue(child, cost, lv + 1)
                    self.__past_states.append((child, cost))
                #print("right")
                #child.displayPuzzle()
            if (i != 3) :
                child = Puzzle()
                child.copy(puzzle)
                child.down()
                cost = lv + 1 + child.countCost()
                if (not self.isPast(child, cost)) :
                    self.__queue.enqueue(child, cost, lv + 1)
                    self.__past_states.append((child, cost))
                #print("down")
                #child.displayPuzzle()
            if (j != 0) :
                child = Puzzle()
                child.copy(puzzle)
                child.left()
                cost = lv + 1 + child.countCost()
                if (not self.isPast(child, cost)) :
                    self.__queue.enqueue(child, cost, lv + 1)
                    self.__past_states.append((child, cost))
                #print("left")
                #child.displayPuzzle()
    

    def solve(self) :
        if (self.isSolvable()) :
            # do something
            # branch and bound
            print("Puzzle dicari dengan metode branch and bound...")
            self.__queue.enqueue(self.__puzzle, self.__puzzle.countCost(), 0)
            self.__past_states.append((self.__puzzle, 0))
            while (not self.__fin and self.__queue.len() > 0) :
                head = self.__queue.dequeue()

                print("Level : ", head[2])
                head[0].displayPuzzle()
                print("Cost : ", head[1])
                print("Moves : ", head[0].getMoves())
                print()
                
                self.branchBound(head[0], head[2])
                
                #self.__fin = True
                if (self.__fin) :
                    print("Final state reached")
            #self.__queue.printQueue()
            self.displayMoves()

        else :
            print("Puzzle tidak dapat diselesaikan")

    

    def isPast(self, puzzle, cost) :
        i = 0
        past = False
        while (i < len(self.__past_states) and not past) :
            if (self.__past_states[i][0].equals(puzzle)) :
                if (self.__past_states[i][1] <= cost) :
                    past = True
                else :
                    self.__past_states.pop(i)
            else :
                i += 1
        return past

    def displayMoves(self) :
        print("Move sequence : ")
        self.__puzzle.displayPuzzle()
        copy_pz = Puzzle()
        copy_pz.copy(self.__puzzle)
        print()
        for move in self.__sequence :
            if (move == 'u') :
                copy_pz.up()
            elif (move == 'r') :
                copy_pz.right()
            elif (move == 'd') :
                copy_pz.down()
            else :
                copy_pz.left()
            copy_pz.displayPuzzle()
            print()