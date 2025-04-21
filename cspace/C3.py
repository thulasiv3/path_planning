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

def C3_func(robot: typing.Dict[str, typing.List[float]], cspace: np.array,q_grid: np.array, q_goal: np.array) -> np.array:
    """Create a new 2D array that shows the distance from each point in the configuration space to the goal configuration.

    Parameters
    ----------
    robot : typing.Dict[str, typing.List[float]]
        A dictionary containing the robot's parameters
    cspace : np.array
        The configuration space of the robot given by C2. The first dimension is q1 and the second dimension is q2. Example: [q1, q2]
    q_grid : np.array
        A R x 1 numpy array representing the grid over the angle-range. R is the resolution.
    q_goal : np.array
        A 2 x 1 numpy array representing the goal configuration of the robot in the format of [q1, q2].

    Returns
    -------
    np.array
       A 2D numpy array representing the distance from each cell in the configuration space to the goal configuration. 
       The first dimension is q1 and the second dimension is q2. Example: [q1, q2]
    """

    ### Insert your code below: ###
    
    goal_q1 = np.argmin(np.abs(q_grid-q_goal[0]))
    goal_q2 = np.argmin(np.abs(q_grid-q_goal[1]))
    distances = cspace
    rows = distances.shape[0]
    cols = distances.shape[1]
    # print(cols)
    distances = np.full((rows, cols), np.inf)

    queue = []
    distances[goal_q1][goal_q2] = 0
    queue.append((goal_q1, goal_q2))

    print(goal_q1, goal_q2)
    
    
    possible_moves = [(-1, 0), (1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1)]


    while queue:
        r, c = queue.pop(0)
        for dr, dc in possible_moves:
            pr, pc = r+dr, c+dc
            if 0 <= pr < rows and 0 <= pc < cols and cspace[pr][pc] == 0:
                if distances[pr][pc] > distances[r][c] + 1:
                    distances[pr][pc] = distances[r][c] + 1
                    queue.append((pr, pc))
            
    return distances