import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon
from shapely.geometry import Polygon as Polygon_shapely # type: ignore
# from shapely.geometry import Polygon as Polygon_shapely
from helper_functions import *
from q2poly import q2poly
import typing

"""
CS4610/CS5335 - Spring 2025 - Homework 2

Name: Thulasi Varatharajan 
Email: varatharajan.t@northeastern.edu
With Whom you discussed the questions with: N/A
"""

def C2_func(robot: typing.Dict[str, typing.List[float]], cspace: np.array, obstacles: typing.List[Polygon],q_grid: np.array) -> np.array:
    """Create the configuration space for the robot with the given obstacles in the given empty cspace array.

    Parameters
    ----------
    robot : typing.Dict[str, typing.List[float]]
        A dictionary containing the robot's parameters
    cspace : np.array
        An empty 2D numpy array
    obstacles : typing.List[Polygon]
        A list of polygons representing the obstacles
    q_grid : np.array
        A R x 1 numpy array representing the grid over the angle-range. R is the resolution.

    Returns
    -------
    np.array
        A 2D numpy array representing the updated configuration space. The first dimension is q1 and the second dimension is q2. Example: [q1, q2]
    """

    ### Insert your code below: ###

    # poly1 = Polygon_shapely(shape1_tuple)
    # obs1 = Polygon_shapely(obstable_tuple)

    # print(q_grid[1])
    # s_obs = [Polygon_shapely(obs) for obs in obstacles]
    cspace = np.zeros((len(q_grid), len(q_grid)))

    for i, q1 in enumerate(q_grid):
        for j, q2 in enumerate(q_grid):

            shape1, shape2, piv1, piv2 = q2poly(robot=robot, q=[q1, q2])


            # print(piv1)
            # print(piv2)
            
            sh1 = Polygon_shapely(shape1)
            # print(shape1)
            sh2 = Polygon_shapely(shape2)
            # print(shape2)
            

            for obs in obstacles:
                obs_shape = Polygon_shapely(obs)
                if sh1.intersects(obs_shape) or sh2.intersects(obs_shape):
                    cspace[i, j] = 1
                    break

    

    return cspace