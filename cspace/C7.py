import matplotlib.pyplot as plt
import numpy as np
import math
from matplotlib.patches import Polygon
from helper_functions import *

"""
CS4610/CS5335 - Spring 2025 - Homework 2

Name: Thulasi Varatharajan 
Email: varatharajan.t@northeastern.edu
With Whom you discussed the questions with: Alston Liu
"""

def C7_func(cspace: np.array) -> np.array:
    """Pad the configuration space by one grid cell.

    Parameters
    ----------
    cspace : np.array
        The origianl configuration space of the robot.

    Returns
    -------
    np.array
        The padded configuration space of the robot.
    """

    ### Insert your code below: ###
    padded_cspace = cspace.copy()
    possible_moves = [(-1, 0), (1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    rows = cspace.shape[0]
    cols = cspace.shape[1]
    already_padded = set()

    for i in range(rows):
        for j in range(cols):
            if cspace[i, j] == 1:
                for dr, dc in possible_moves:
                    pr, pc = i+dr, j+dc
                    if (0 <= pr < rows and 0 <= pc < cols and (pr, pc) not in already_padded and cspace[pr][pc] == 0):
                         padded_cspace[pr][pc] = 1
                         already_padded.add((pr, pc))
    
    return padded_cspace