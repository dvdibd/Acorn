from game import Game
import os
from os import path 
import sys
import game_parser
import player
import grid

if len(sys.argv) < 2:
    print("Usage: python3 run.py <filename> [play]")
 
else:
    if os.path.isfile(sys.argv[1]):
        game1 = Game(sys.argv[1])
        game1.initParser()
        game1.displayGrid()
        quitFlag = False 
        while not quitFlag:
            m1 = input("\nInput a move: ")
            quitFlag = game1.playGame(m1)
    else:
        print(sys.argv[1] + ' does not exist!')
