#! usr/bin/env python
# *-* coding: utf-8 *-*
"""A Fibonacci sequence generator function with loops."""


def fibonacci(maxint):
    """This is a docstring.

    Arg:
        maxint(int): an integer that will serve as the upper bound of the loop

    Return:
        A new generated sequence as a list

    Example:
        >>>import task_01
        >>>task_01.fibonacci(10)
        [0,1,1,2,3,5,8]
            
    """
    a, b = 1, 3
    while b < 10:
        print(b)
        a, b = b, a+b
