# You may need this if you really want to use a recursive solution!
# It raises the cap on how many recursions can happen. Use this at your own risk!

# sys.setrecursionlimit(100000)

import sys
from game import Game
import os
from os import path 
#import game_parser
from game_parser import read_lines 
import game_parser
import player
import grid


def bfs(graph, start, end):
    # maintain a queue of paths
    queue = []
    # push the first path into the queue
    queue.append([start])
    while queue:
        # get the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]
        # path found
        if node == end:
            return path
        # enumerate all adjacent nodes, construct a new path and push it into the queue
        for adjacent in graph.get(node, []):
            new_path = list(path)
            new_path.append(adjacent)
            queue.append(new_path)

def getNeighbors(detNode):
    adj = []
    # check 'a': c-1, r   's': c, r+1   'd': c+1, r   'w': c, r+1
    # 'a': c-1, r
    #detN = {g: graph, n: numBuck, s: start, e: end, m: move}
    digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    moves = ['a', 's', 'd', 'w', 'e']
    for move in moves:
        allow = False
        if move == 'a':
            row = detNode['s']['r']
            col = detNode['s']['c']-1
            if col >= 0:
                allow = True
        elif move == 's':
            row = detNode['s']['r']+1
            col = detNode['s']['c']
            if row < len(detNode['g'][0]):
                allow = True
        elif move == 'd':
            row = detNode['s']['r']
            col = detNode['s']['c']+1
            if col < len(detNode['g'][:][0]):
                allow = True
        elif move == 'w':
            row = detNode['s']['r']-1
            col = detNode['s']['c']
            if row >= 0:
                allow = True
        elif move == 'e':
            if (detNode['g'][detNode['s']['r']][detNode['s']['c']] in digits):
                row = detNode['s']['r']
                col = detNode['s']['c']
                allow = True
        if allow:
            if (detNode['g'][row][col] != '*') & (detNode['g'][row][col] != 'X'):
                detNodeC = copyNode(detNode)
                if (detNodeC['g'][row][col] == 'F'):
                    if detNodeC['n'] > 0:
                        detN = {'g': detNodeC['g'], 'n': detNodeC['n']-1, 's': detNodeC['s'], 'e': detNodeC['e'], 'm': move}
                        detN['g'][row][col] = ' '
                        detN['s']['r'] = row
                        detN['s']['c'] = col
                        if not inExplored(detN):
                            adj.append(detN)
                elif (detNodeC['g'][row][col] == 'W'):
                    detN = {'g': detNodeC['g'], 'n': detNodeC['n']+1, 's': detNodeC['s'], 'e': detNodeC['e'], 'm': move}
                    detN['g'][row][col] = ' '
                    detN['s']['r'] = row
                    detN['s']['c'] = col
                    if not inExplored(detN):
                        adj.append(detN)
                elif (detNodeC['g'][row][col] == ' '):
                    detN = {'g': detNodeC['g'], 'n': detNodeC['n'], 's': detNodeC['s'], 'e': detNodeC['e'], 'm': move}
                    detN['s']['r'] = row
                    detN['s']['c'] = col
                    #print("IT IS HERE :  row, col = ", row, col)
                    if not inExplored(detN):
                        #print("INSIDE EMPTY CELL")
                        adj.append(detN)
                elif (detNodeC['g'][row][col] == 'Y'):
                    detN = {'g': detNodeC['g'], 'n': detNodeC['n'], 's': detNodeC['s'], 'e': detNodeC['e'], 'm': move}
                    detN['s']['r'] = row
                    detN['s']['c'] = col
                    if not inExplored(detN):
                        adj.append(detN)
                elif (detNodeC['g'][row][col] in digits):
                    found = False
                    for i in range(len(detNodeC['g'])):
                        for j in range(len(detNodeC['g'][i])):
                            if detNodeC['g'][i][j] in digits:
                                #print("HERE 2")
                                if (not ((i==row) & (j==col))) & (detNodeC['g'][i][j]==detNodeC['g'][row][col]):
                                    detN = {'g': detNodeC['g'], 'n': detNodeC['n'], 's': detNodeC['s'], 'e': detNodeC['e'], 'm': move}
                                    detN['s']['r'] = i
                                    detN['s']['c'] = j
                                    if not inExplored(detN):
                                        adj.append(detN)
                                    found=True
                                    break
                        if found:
                            break
    return(adj)

Explored = []
def inExplored(newNode):
    # check newNode['g'], ['n'], ['s']
    nodePres = False
    for node1 in Explored:
        if newNode['n'] == node1['n']:
            if (newNode['s']['r'] == node1['s']['r']) & (newNode['s']['c'] == node1['s']['c']):
                graphPres = True
                for i in range(len(newNode['g'])):
                    for j in range(len(newNode['g'][i])-1):
                        if newNode['g'][i][j] != node1['g'][i][j]:
                            graphPres = False
                            break
                    if not graphPres:
                        break
                if graphPres:
                    nodePres = True
                    break
    if not nodePres:
        Explored.append(copyNode(newNode))
    else:
        pass
    
    return(nodePres)

def printGraph(LoL, st1):
    for i in range(len(LoL)):
        list1 = LoL[i]
        for j in range(len(LoL[i])):
            if (i==st1['r']) & (j==st1['c']):
                list1[j] = 'A'
        print(''.join(list1))

def solveBFS(graph, numBuck, start, end):
    solvedPaths = []
    # maintain a queue of paths
    queue = []
    # push the first path into the queue
    detN = {'g': graph, 'n': numBuck, 's': start, 'e': end, 'm': ''}
    queue.append([detN])
    while queue:
        # get the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        detNode = path[-1]
        #printGraph(detNode['g'], detNode['s'])
        #x = input("ENTER something: ")
        # path found
        if detNode['s'] == end:
            #return path
            
        
            sol1 = []
            for i in range(1, len(path)):
                sol1.append(path[i]['m'])
            solvedPaths.append(sol1)
        else:
            # enumerate all adjacent nodes, construct a new path and push it into the queue
            list1 = getNeighbors(detNode)
            #print("No. of adj nodes: = ", len(list1))
            #x = input("ENTER something: ")
            for adjacent in list1:
                new_path = list(path)
                new_path.append(adjacent)
                queue.append(new_path)
    min1 = 10000000
    shortestPath = []
    foundPath = False
    for i in range(len(solvedPaths)):
        path1 = solvedPaths[i]
        if (len(path1) < min1):
            foundPath = True
            min1 = len(path1)
            shortestPath = path1
    return(foundPath, shortestPath)       
    
            
def solveDFS(graph, numBuck, start, end):
    solvedPaths = []
    # maintain a queue of paths
    queue = []
    # push the first path into the queue
    detN = {'g': graph, 'n': numBuck, 's': start, 'e': end, 'm': ''}
    queue.append([detN])
    while queue:
        #print('QUEUE length = ', len(queue))
        # get the first path from the queue
        path = queue.pop()
        # get the last node from the path
        detNode = path[-1]
        #printGraph(detNode['g'], detNode['s'])
        # path found
        if detNode['s'] == end:
            #return path
            sol1 = []
            for i in range(1, len(path)):
                sol1.append(path[i]['m'])
            solvedPaths.append(sol1)
        else:
            # enumerate all adjacent nodes, construct a new path and push it into the queue
            list1 = getNeighbors(detNode)
            #x = input("ENTER something: ")
            for adjacent in list1:
                new_path = list(path)
                new_path.append(adjacent)
                queue.append(new_path)
    min1 = 10000000
    shortestPath = []
    foundPath = False
    for i in range(len(solvedPaths)):
        path1 = solvedPaths[i]
        if (len(path1) < min1):
            foundPath = True
            min1 = len(path1)
            shortestPath = path1
    return(foundPath, shortestPath)       

def solve(mode, graph, numBuck, start, end):
    if mode == 'BFS':
        return(solveBFS(graph, numBuck, start, end))
    elif mode == 'DFS':
        return(solveDFS(graph, numBuck, start, end))
 
def copyNode(dNode):
    #detN = {g: graph, n: numBuck, s: start, e: end, m: move}
    grid2 = []
    start2 = {'r': 0, 'c': 0}
    end2 = {'r': 0, 'c': 0}
    for i in range(len(dNode['g'])):
        temp1 = []
        for j in range(len(dNode['g'][i])):
            temp1.append(dNode['g'][i][j])
        grid2.append(temp1)
    
    start2['r'] = dNode['s']['r']
    start2['c'] = dNode['s']['c']
    end2['r'] = dNode['e']['r']
    end2['c'] = dNode['e']['c']
    int1 = 0
    ch1 = ''
    int1 = dNode['n']
    ch1 = dNode['m']
    tempNode = {'g': grid2, 'n': int1, 's': start2, 'e': end2, 'm': ch1}
    return(tempNode)
            
def read_lines(filename):
    """Read in a file, process them using parse(),
    and return the contents as a list of list of cells."""
    
    with open(filename) as f:
        lines = f.readlines()
    ListOfList = []
    start = {'r': 0, 'c': 0}
    end = {'r': 0, 'c': 0}
    i=0
    while i < (len(lines)-1):
        temp1 = []
        for j in range(len(lines[i])-1):
            temp1.append(lines[i][j])
            if lines[i][j]=='X':
                start['r'] = i
                start['c'] = j
            elif lines[i][j]=='Y':
                end['r'] = i
                end['c'] = j
        ListOfList.append(temp1)
        i = i+1
    temp1 = []
    for j in range(len(lines[i])):
        temp1.append(lines[i][j])
        if lines[i][j]=='X':
            start['r'] = i
            start['c'] = j
        elif lines[i][j]=='Y':
            end['r'] = i
            end['c'] = j
    ListOfList.append(temp1)
    return ListOfList, start, end
    


if __name__ == "__main__":
    if len(sys.argv) <3:
        print("Usage: python3 solver.py <filename> <mode>")
    else:
        graph, start, end = read_lines(sys.argv[1])
        solution_found = False
        solution_found, shortestPath = solve(sys.argv[2], graph, 0, start, end)
        if solution_found:
            print("Path has " + str(len(shortestPath))+" moves.")
            print("Path: "+', '.join(shortestPath))
        else:
            print("There is no possible path.")
