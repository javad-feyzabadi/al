def buy_sell_stock(prices):
    """
    buy_sell_stock([7,1,5,3,6,4])
    >>> 5
    buy_sell_stock([9,7,6,4,3,1])
    >>> 0
    """
    cur_max, max_so_far = 0 , 0
    for i in range(1,len(prices)):
        cur_max = max(0, cur_max+prices[i] - prices[i-1])
        max_so_far = max(max_so_far,cur_max)
    return max_so_far
