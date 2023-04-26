def move_zero(seq):
    """
    >>> move_zero([False,1,0,1,2,0,1,3,'a'])
    [False, 1, 1, 2, 1, 3, 'a', 0, 0]
    """
    result = []
    zeros = 0
    for i in seq:
        if i == 0 and type(i) != bool:
            zeros += 1
        else:
            result.append(i)
    result.extend([0]*zeros)
    return result

print(move_zero([False,1,0,1,2,0,1,3,'a']))