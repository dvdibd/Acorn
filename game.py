from game_parser import read_lines
from grid import grid_to_string
from player import Player

from cells import (
    Start,
    End,
    Air,
    Wall,
    Fire,
    Water,
    Teleport
)
from player import Player

class Game:
    def __init__(self, filename):
        self.filename = filename
        self.moves = []
        self.totMoves = 0
        self.pROW =0
        self.pCOL =0
        self.grid1 = read_lines(self.filename)
        
    def gameMove(self, move):
        pass

    def initParser(self):
        for i in range(len(self.grid1)):
            for j in range(len(self.grid1[i])):
                if type(self.grid1[i][j])==Start:
                    self.pROW = i
                    self.pCOL = j
                    self.p1=Player()
                    self.p1.display = 'A'
                    self.p1.row=i
                    self.p1.col=j
                    self.p1.num_water_buckets = 0
    
    def displayGrid(self):
        print(grid_to_string(self.grid1, self.p1))
    
    def setGrid(self, prevR, prevC, r1, c1):
        if type(self.grid1[r1][c1])==Air:
            self.p1.row=r1
            self.p1.col=c1
            return('', False)
        if type(self.grid1[r1][c1])==Start:
            self.p1.row=r1
            self.p1.col=c1
            return('', False)
        elif type(self.grid1[r1][c1])==End:
            self.p1.row=r1
            self.p1.col=c1
            mess1 = "\n\nYou conquer the treacherous maze set up by the Fire Nation and reclaim the Honourable Furious Forest Throne, restoring your hometown back to its former glory of rainbow and sunshine! Peace reigns over the lands.\n"
            str1 = ', '.join(self.moves)
            if self.totMoves<2:
                mess1 = mess1 + "\n" + "You made " + str(self.totMoves) + " move." + "\n" + "Your move: " + str1 + "\n\n=====================\n====== YOU WIN! =====\n====================="
            else:    
                mess1 = mess1 + "\n" + "You made " + str(self.totMoves) + " moves." + "\n" + "Your moves: " + str1 + "\n\n=====================\n====== YOU WIN! =====\n====================="
            return(mess1, True)
        elif type(self.grid1[r1][c1])==Wall:
            self.p1.row=prevR
            self.p1.col=prevC  
            self.moves.pop() 
            self.totMoves -= 1         
            return("\nYou walked into a wall. Oof!", False)
        elif type(self.grid1[r1][c1])==Teleport:
            #search for other teleport
            self.found = False
            for self.i in range(len(self.grid1)):
                for self.j in range(len(self.grid1[self.i])):
                    if type(self.grid1[self.i][self.j])==Teleport:
                        if (not ((self.i==r1) & (self.j==c1))) & (self.grid1[self.i][self.j].display==self.grid1[r1][c1].display):
                            self.p1.row = self.i
                            self.p1.col = self.j
                            self.found=True
                            break
                if self.found:
                    break
            return("\nWhoosh! The magical gates break Physics as we know it and opens a wormhole through space and time.", False)
        
        elif type(self.grid1[r1][c1])==Water:
            self.p1.row = r1
            self.p1.col = c1
            self.p1.num_water_buckets += 1
            self.grid1[r1][c1] = Air()
            return("\nThank the Honourable Furious Forest, you've found a bucket of water!", False)
        
        elif type(self.grid1[r1][c1])==Fire:
            if self.p1.num_water_buckets>0:
                self.p1.num_water_buckets -= 1
                self.grid1[r1][c1] = Air()
                self.p1.row = r1
                self.p1.col = c1
                return("\nWith your strong acorn arms, you throw a water bucket at the fire. You acorn roll your way through the extinguished flames!", False)
        
            else:
                self.p1.row = r1
                self.p1.col = c1
                str2 = ', '.join(self.moves)
                str1 = "\n\nYou step into the fires and watch your dreams disappear :(.\n\nThe Fire Nation triumphs! The Honourable Furious Forest is reduced to a pile of ash and is scattered to the winds by the next storm... You have been roasted.\n\nYou made " + str(self.totMoves) + " moves.\nYour moves: " + str2 + "\n\n=====================\n===== GAME OVER =====\n====================="
                return(str1, True)

    def playGame(self, ch):
        ch1 = ch.lower()
        validMoves = ['w', 'a', 's', 'd', 'e', 'q']
        if ch1 not in validMoves:
            self.displayGrid()
            print('\nPlease enter a valid move (w, a, s, d, e, q).')
            return(False)
        self.moves.append(ch1)
        self.totMoves += 1
        mess1 = ''
        flag1 = False
        if ch1 == 'w':
            mess1, flag1 = self.setGrid(self.p1.row, self.p1.col, self.p1.row - 1, self.p1.col)
            self.displayGrid()
        elif ch1 == 'a':
            mess1, flag1 = self.setGrid(self.p1.row, self.p1.col, self.p1.row, self.p1.col -1)
            self.displayGrid()
        elif ch1 == 's':
            mess1, flag1 = self.setGrid(self.p1.row, self.p1.col, self.p1.row+1, self.p1.col)
            self.displayGrid()
        elif ch1 == 'd':
            mess1, flag1 = self.setGrid(self.p1.row, self.p1.col, self.p1.row, self.p1.col+1)
            self.displayGrid()
        elif ch1 == 'e':
            mess1, flag1 = self.setGrid(self.p1.row, self.p1.col, self.p1.row, self.p1.col)
            self.displayGrid()
        elif ch1 == 'q':
            mess1 = '\nBye!'
            flag1 = True
        if mess1 != '':
            print(mess1)
        return(flag1)
