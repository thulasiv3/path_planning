import numpy as np
import typing
import pdb

"""
CS4610/CS5335 - Spring 2025 - Homework 2

Name: Thulasi Varatharajan
Email: varatharajan.t@northeastern.edu
With Whom you discussed the questions with: N/A
"""

def q2poly(robot: typing.Dict[str, typing.List[float]], q: typing.List[float]) -> typing.Tuple[np.array, np.array, np.array, np.array]:
    """ A function that takes in the robot's parameters and a configuration and 
    returns the vertices of the robot's links after transformation and the pivot points of the links after transformation

    Parameters
    ----------
    robot : typing.dict[str, typing.List[float]]
        A dictionary containing the robot's parameters
    q : typing.List[float]
        A 2-element list representing the configuration of the robot

    Returns
    -------
    typing.Tuple[np.array, np.array, np.array, np.array]
        np.array: 
            a numpy array representing the vertices of the first link of the robot after transformation
        np.array: 
            a numpy array representing the vertices of the second link of the robot after transformation
        np.array: 
            a numpy array representing the pivot point of the first link of the robot after transformation
        np.array: 
            a numpy array representing the pivot point of the second link of the robot after transformation
    """


    ### Insert your code below: ###
    # def rotate(angle):
    #     return np.array([[np.cos(angle), -np.sin(angle)], 
    #           [np.sin(angle), np.cos(angle)]])



    shape1 = np.array(robot["link1"])
    shape2 = np.array(robot["link2"])
    pivot1 = np.array(robot["pivot1"])
    pivot2 = np.array(robot["pivot2"])
    angle1 = q[0]
    angle2 = q[1]



# Construct the combined transformation matrix
# Translation that takes the pivot into account
   

    zeroTone = np.array([
    [np.cos(angle1), -np.sin(angle1)], 
    [np.sin(angle1),  np.cos(angle1)],
])
    
    oneTtwo = np.array([
    [np.cos(angle2), -np.sin(angle2)], 
    [np.sin(angle2),  np.cos(angle2)],
])
    

    tm2_multiplied = np.dot(zeroTone, oneTtwo)

    pivot2 = np.dot(zeroTone, robot["pivot2"]) + pivot1

    tm1 = np.dot(zeroTone, shape1.T).T +  pivot1
    tm2 = np.dot(tm2_multiplied, shape2.T).T + pivot2

    return tm1, tm2, pivot1, pivot2