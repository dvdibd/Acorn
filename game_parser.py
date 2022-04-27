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

def read_lines(filename):
    """Read in a file, process them using parse(),
    and return the contents as a list of list of cells."""
    
    with open(filename) as f:
        content = f.readlines()
    return(parse(content))

def parse(lines):
    """Transform the input into a grid.

    Arguments:
        lines -- list of strings representing the grid

    Returns:
        list -- contains list of lists of Cells
    """
    
    
    i = 0
    
    list1 = ""
    while i < len(lines):
        j = 0
        while j < len(list(lines[i])):
            list1 = list1+list(lines[i])[j]
            
            j = j +1
        i = i+1

    
    list1 = list1[:-1]
    allowed = [' ', 'X', 'Y','*','1','2','3','4','5','6','7','8','9','W','F', '\n']
    k = 0

    while k < len(list1):
        try:
            allowed.index(list1[k])
        except ValueError:
            raise ValueError('Bad letter in configuration file: '+list1[k]+'.')

        k = k+1

    numList = []
    numList.append(1)
    cntX = list1.count('X')
    try:
        numList.index(cntX)
    except ValueError:
        raise ValueError('Expected 1 starting position, got '+str(cntX)+'.')
    cntY = list1.count('Y')
    try:
        numList.index(cntY)
    except ValueError:
        raise ValueError('Expected 1 ending position, got '+str(cntY)+'.')
    
    #teleport
    i=0
    teleport = 0
    while i <10:
        if list1.count(str(i))%2 != 0:
            teleport=i
            break 
        i=i+1
    teleList = [0,2,4,6,8,10]
    try:
        teleList.index(list1.count(str(teleport)))
    except ValueError:
        raise ValueError('Teleport pad '+str(teleport)+' does not have an exclusively matching pad.')
    ListOfList = []
    i = 0
    digits = ['1','2','3','4','5','6','7','8','9']
    while i < (len(lines)-1):
        temp1 = []
        for j in range(len(lines[i])-1):
            if (lines[i][j] == ' '):
                temp1.append(Air())
            elif (lines[i][j] == 'X'):
                temp1.append(Start())
            elif (lines[i][j] == 'Y'):
                temp1.append(End())
            elif (lines[i][j] == '*'):
                temp1.append(Wall())
            elif (lines[i][j] in digits):
                c1 = Teleport()
                c1.display = lines[i][j]
                temp1.append(c1)
            elif (lines[i][j] == 'W'):
                temp1.append(Water())
            elif (lines[i][j] == 'F'):
                temp1.append(Fire())
        ListOfList.append(temp1)
        i = i+1
    temp1 = []
    for j in range(len(lines[i])):
        if (lines[i][j] == ' '):
            temp1.append(Air())
        elif (lines[i][j] == 'X'):
            temp1.append(Start())
        elif (lines[i][j] == 'Y'):
            temp1.append(End())
        elif (lines[i][j] == '*'):
            temp1.append(Wall())
        elif (lines[i][j] in digits):
            c1 = Teleport()
            c1.display = lines[i][j]
            temp1.append(c1)
        elif (lines[i][j] == 'W'):
            temp1.append(Water())
        elif (lines[i][j] == 'F'):
            temp1.append(Fire())


    ListOfList.append(temp1)
    return(ListOfList)
