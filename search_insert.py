def search_insert(arr,val):
    """
    arr = [1,3,5,6]
    val = 3
    >>> 1
    arr = [1,3,5,6]
    val = 7
    >>> 4
    arr = [1,3,5,6]
    val = 0
    >>> 0
    """

    low = 0
    high = len(arr)-1
    mid = high // 2
  
    while low <= high :
        if val > arr[mid]:
            mid += 1
            low = mid
        else:
            mid -= 1
            high = mid
    return low


