"""
A file for executing math functions.
"""

import random
import numpy as np
from typing import Union  # gives ability to define types in python

def euler(n=10, maxitr=1000):

    """
    This function computes :math:`e` via a Taylor series.

    .. math::

        e = 1 + \\sum_n^\\infty \\frac{1}{n!}

    Parameters
    ----------
    n : int
        Level of precision.

    Returns
    -------
    e_value : float
        The computed value of Euler's number.
    """

    if n < 0:
        raise ValueError("Only positive integers are allowed")

    euler_tmp = 0
    euler = 0
    for i in range(maxitr):
        denominator = 1
        for j in range(1, i + 1):
            denominator = denominator * j
        euler_tmp += 1 / denominator

        if i == 0:
            euler = round(euler_tmp, n)
        else:
            if euler == round(euler_tmp, n):
                break
            else:
                euler = round(euler_tmp, n)
    print("Euler's number up to %g digits is: %f" % (n, euler))
    return euler


def find_pi(maxitr=1e+20):

    """
    This function computes :math:`\\pi` heuristically.

    Parameters
    ----------
    maxitr : int
        Number of random coordinates used in calculation.

    Returns
    -------
    pi_value : float
        The computed value of pi according to the number of points requested.
    """

    ncircle, ntotal = [0, 0]
    for i in range(int(maxitr)):

        # Generate coordinates
        coord = np.array([random.random() for x in range(2)])
        # Determine if it is within circle and add to counts
        ntotal += 1
        if np.sqrt(np.sum(coord**2)) < 1:
            ncircle += 1
        # Calculate pi
        pi_tmp = ncircle / ntotal * 4

    print("Pi is: %f" % (pi_tmp))
    return pi_tmp

