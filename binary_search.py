def binary_search(array,element):
    """
    >>> (binary_search([2,3,4,6,12,19,20,21],4))
    2
    """
    low = 0
    high = len(array)-1

    while low <= high :
        mid = (high + low) // 2
        val = array[mid]
        if val == element :
            return mid
        elif val < element :
            low = mid + 1
        else:
            high = mid - 1
    return -1

print(binary_search([2,3,4,6,12,19,20,21,25,26,59,98,122,125,135,168],125))