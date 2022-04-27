import game_parser

def grid_to_string(grid, player):
    """Turns a grid and player into a string

    Arguments:
        grid -- list of list of Cells
        player -- a Player with water buckets

    Returns:
        string: A string representation of the grid and player.
    """
    
    str1 = ""
    for i in range(len(grid)-1):
        for j in range(len(grid[i])):
            if (i==player.row) & (j==player.col):
                str1 = str1 + player.display   
            else:
                str1 = str1 + str(grid[i][j].display)
        str1 = str1 +'\n'
    i=len(grid)-1
    for j in range(len(grid[i])):
        if (i==player.row) & (j==player.col):
            str1 = str1 + player.display   
        else:
            str1 = str1 + str(grid[i][j].display)
    if((player.num_water_buckets>0)&(player.num_water_buckets<2)): 
        str1 = str1 + "\n\nYou have " + str(player.num_water_buckets)+ " water bucket."
    else:
        str1 = str1 + "\n\nYou have " + str(player.num_water_buckets)+ " water buckets."
    return(str1)
    
