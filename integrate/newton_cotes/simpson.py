"""
This file contains the implementation of the Simpson rule
"""

import numpy as np


def evaluate(bounds, func):
    """
    
    Evaluates simpson's rule on an array of values and a function pointer.

    .. math::
    
        \int_{a}^{b} = \sum_{i} 

    Parameters
    ----------
    bounds : array_like
        An array with a dimension of two that contains the starting and ending
        points of the integrand. 
    func : function
        Function to be integrated. 

    Returns
    ------
    integral : float
        The integral of the function between the bounds. 

    """

    if len(bounds) != 2:
        raise ValueError("Bounds should have length two, found %d." %
                len(bounds))

    a = bounds[0]
    b = bounds[1]
    ya = func(a)
    yb = func((a + b) / 2.)
    yc = func(b)
    I = (b - a) * (ya + 4 * yb + yc) / 6.
    return I
