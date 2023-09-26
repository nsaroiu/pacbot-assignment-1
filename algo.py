# You can modify this file to implement your own algorithm

from constants import *

"""
You can use the following values from constants.py to check for the type of cell in the grid:
I = 1 -> Wall 
o = 2 -> Pellet (Small Dot)
e = 3 -> Empty
"""

def get_next_coordinate(grid, location):

    """
    Calculate the next coordinate for 6ix-pac to move to.
    Check if the next coordinate is a valid move.

    Parameters:
    - grid (list of lists): A 2D array representing the game board.
    - location (list): The current location of the 6ix-pac in the form (x, y).

    Returns:
    - list or tuple: 
        - If the next coordinate is valid, return the next coordinate in the form (x, y) or [x,y].
        - If the next coordinate is invalid, return None.
    """

    path_list = bfs(grid, location)

    return path_list.pop(1) if path_list is not None else None


def bfs(grid, location):
    """
    Implement the Breadth First Search algorithm here.
    """

    directions = [(0,1), (0,-1), (1,0), (-1,0)]

    queue = []
    queue.append([location])

    visited = set()

    while queue != []:
        currPath = queue.pop(0)
        curr = currPath[len(currPath) - 1]
        visited.add(curr)

        if grid[curr[0]][curr[1]] == o:
            return currPath

        for direction in directions:
            if (curr[0] + direction[0], curr[1] + direction[1]) not in visited and \
            0 <= curr[0] + direction[0] < len(grid) and \
            0 <= curr[1] + direction[1] < len(grid[0]) and \
            grid[curr[0] + direction[0]][curr[1] + direction[1]] != I:

                queue.append(currPath + [(curr[0] + direction[0], curr[1] + direction[1])])

    return None
