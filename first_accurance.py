def first_accurance(array,element):
    """
    >>> first_accurance([2,2,2,3,3,4,4,5,5,5],5)
    7
    """
    low, high = 0 , len(array)-1

    while low <= high :
        mid = (low + high) // 2
        if low == high:
            break
        if array[mid] < element:
            low = mid +1
        else:
            high = mid
    if array[low] == element :
        return low
    
print(first_accurance([2,2,2,3,3,4,4,5,5,5],5))