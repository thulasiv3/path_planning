import matplotlib.pyplot as plt
import numpy as np
import math
from matplotlib.patches import Polygon
from matplotlib.figure import Figure
from helper_functions import *
from q2poly import q2poly
import shapely
from shapely.geometry import Polygon as Polygon_shapely
from shapely import MultiPoint
import typing

"""
CS4610/CS5335 - Spring 2025 - Homework 2

Name: Thulasi Varatharajan 
Email: varatharajan.t@northeastern.edu
With Whom you discussed the questions with: Alston Liu
"""

def C6_func(robot: typing.Dict[str, typing.List[float]], 
            q_path: typing.List[np.array], 
            obstacles: typing.List[Polygon]) -> typing.Tuple[int, Figure]:
    """Calculate the number of collisions that occur along the path, and generate a visualization.
    The visualization should be passed as a matplotlib figure to the outer hw2_cspace.py function.
    
    Parameters
    ----------
    robot : typing.Dict[str, typing.List[float]]
        A dictionary containing the robot's parameters.
    q_path : typing.List[np.array]
       A list of 2 x 1 numpy array representing the path from the start configuration to the goal 
       configuration using actual angle values.
    obstacles : typing.List[Polygon]
        A list of polygons representing the obstacles.

    Returns
    -------
    num_collisions : int
        The number of collisions that occur along the path.
    figure : matplotlib.figure.Figure
        Figure showing swept volume collisions

    """

    ### Insert your code below: ###
    def add_patch(ax, sh, facecolor='purple', edgecolor='blue', alpha=0.5):

        if sh.is_empty:
            return
        if sh.geom_type == 'Polygon':
            x, y = sh.exterior.xy
            patch = plt.Polygon(np.array([x, y]).T, facecolor=facecolor, edgecolor=edgecolor, alpha=alpha)
            ax.add_patch(patch)
        elif sh.geom_type == 'MultiPolygon':
            for poly in sh.geoms:
                x, y = poly.exterior.xy
                patch = plt.Polygon(np.array([x, y]).T, facecolor=facecolor, edgecolor=edgecolor, alpha=alpha)
                ax.add_patch(patch)

        


    num_collisions: int = 0
    fig, ax = plt.subplots()
    plt.xlim([0,12])
    plt.ylim([0,12])
    plt.axis('square')

    for i in range(len(obstacles)):
            coord = obstacles[i]
            p = Polygon(coord, facecolor = 'k')
            plt.gca().add_patch(p)

    ax.set_title("Swept Volume Collisions")
    unions = []

    for i in range(1, len(q_path)):
        shape1, shape2, piv1, piv2 = q2poly(robot, q_path[i-1])
        shape1_1, shape2_1, p1, p2 = q2poly(robot, q_path[i])

        sh1 = Polygon_shapely(shape1)
        sh2 = Polygon_shapely(shape2)
        sh1_1 = Polygon_shapely(shape1_1)
        sh2_1 = Polygon_shapely(shape2_1)

    
        shape1_convex = shapely.union_all([sh1, sh1_1]).convex_hull
        shape2_convex = shapely.union_all([sh2, sh2_1]).convex_hull

       


        for obs in obstacles:
            obs_poly = Polygon_shapely(obs)
            if shape1_convex.intersects(obs_poly) or shape2_convex.intersects(obs_poly):
                num_collisions += 1
                add_patch(ax, shape1_convex, facecolor='red', edgecolor='red')
                add_patch(ax, shape2_convex, facecolor='blue', edgecolor='blue')
 
        # DO NOT CALL plt.show() inside this function. It is called in hw2_cspace.py
    

    return num_collisions, fig