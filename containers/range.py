def range(a, b=None, c=None):
    '''
    This function should behave exactly like the built-in range function.
    For example:

    >>> list(range(5))
    [0, 1, 2, 3, 4]
    >>> list(range(1, 5))
    [1, 2, 3, 4]
    >>> list(range(1, 5, 2))
    [1, 3]
    '''
    if b is None:
        beg = 0
        end = a
    else:
        beg = a
        end = b

    if c is None:
        right = 1
    else:
        right = c

    if right < 0:
        while beg > end:
            f0 = beg
            beg += right
    else:
        while beg < end:
            f0 = beg
            beg += right
            yield f0
