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
    lastnum, curnum = 0, 1
    newlist = [lastnum]
    while curnum < maxint:
        lastnum, curnum = curnum, lastnum+curnum
        newlist.append(lastnum)
    return newlist
