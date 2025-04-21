import matplotlib.pyplot as plt
import numpy as np
import math
from matplotlib.patches import Polygon
from helper_functions import *
import typing

"""
CS4610/CS5335 - Spring 2025 - Homework 2

Name: Thulasi Varatharajan 
Email: varatharajan.t@northeastern.edu
With Whom you discussed the questions with: N/A
"""

def C4_func(distances: np.array,q_grid: np.array, q_start: np.array) -> typing.List[np.array]:
    """Using the distance array from C3, find the optimal path from the start configuration to the goal configuration (zero value).

    Parameters
    ----------
    distances : np.array
        A 2D numpy array representing the distance from each cell in the configuration space to the goal configuration.
        This is given by C3 
    q_grid : np.array
        A R x 1 numpy array representing the grid over the angle-range. R is the resolution.
    q_start : np.array
        A 2 x 1 numpy array representing the start configuration of the robot in the format of [q1, q2].

    Returns
    -------
    typing.List[np.array]
        A list of 2 x 1 numpy array representing the path from the start configuration to the goal configuration using indices of q_grid.
        Example: [ [q1_0 , q2_0], [q1_1, q2_1], .... ]
    """
    
    ### Insert your code below: ###
    shortest_path = []
    rows = len(distances)
    cols = len(distances[0])
    start_q1 = np.argmin(np.abs(q_grid-q_start[0]))
    start_q2 = np.argmin(np.abs(q_grid-q_start[1]))
    possible_moves = [(0, 1), (1, -1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (-1, 1)]
    visited = set()

    for i in range(rows):
        for j in range(cols):
            if distances[i, j] == 0:
                goal_q1 = i
                goal_q2 = j
    
    # print(goal_q1, goal_q2)

    curr_q1, curr_q2 = start_q1, start_q2
    
    while (curr_q1, curr_q2) != (int(goal_q1), int(goal_q2)):
        # shortest_path.append(np.array([q_grid[curr_q1], q_grid[curr_q2]]))
        shortest_path.append(np.array((curr_q1, curr_q2)))
        visited.add((curr_q1, curr_q2))
    
        valid_neighbors = []
        for dr, dc in possible_moves:
            pr, pc = int(curr_q1)+dr, int(curr_q2)+dc
            if 0 <= pr < rows and 0 <= pc < cols and distances[pr, pc] != np.inf and (pr, pc) not in visited:
                valid_neighbors.append((pr, pc, distances[pr, pc]))
        

        valid_neighbors.sort(key=lambda x: x[2])
        # print(valid_neighbors)
        curr_q1, curr_q2 = valid_neighbors[0][:2]
        # print(curr_q1, curr_q2)
        
        
    # shortest_path.append(np.array([q_grid[goal_q1], q_grid[goal_q2]]))
    shortest_path.append(np.array((goal_q1, goal_q2)))

    
        

    

    return shortest_path
