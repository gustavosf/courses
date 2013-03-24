def numPens(n):
    """
    n is a non-negative integer

    Returns True if some non-negative integer combination of 5, 8 and 24 equals n
    Otherwise returns False.
    """
    if (n == 0): return True
    if (n < 0): return False
    for x in [8, 5]:
    	if (numPens(n - x)): return True
    return False

if __name__ == '__main__':
	assert numPens(0) is True
	assert numPens(5) is True
	assert numPens(8) is True
	assert numPens(24) is True
	assert numPens(5+8) is True
	assert numPens(5+24) is True
	assert numPens(8+24) is True
	assert numPens(5+8+24) is True
	assert numPens(5*3+8*7) is True
	assert numPens(5*5+8*3) is True
	assert numPens(8*7) is True
	assert numPens(8*3) is True
	assert numPens(1) is False
	assert numPens(6) is False
	assert numPens(11) is False
	assert numPens(-1) is False