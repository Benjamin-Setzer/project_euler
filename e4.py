"""
http://projecteuler.net/problem=4
"""

def is_pal(nmb):
	nmb = str(nmb)
	for i in range(len(nmb)/2):
		if not nmb[i] == nmb[-1-i]:
			return False
	
	return True
	
def find_largest_pal_product(low_bound, up_bound):
	"""
	    Return the largest product which is a palindrome in a given range. 
	    Factors are restricted in following way:
			low_bound <= factor < up_bound
	"""
	largest_pal = 0
	for i in xrange(low_bound, up_bound):
		for j in xrange(low_bound, up_bound):
			if is_pal(i*j):
				largest_pal = i*j
	return largest_pal
	
if __name__ == '__main__':
	print find_largest_pal_product(100, 1000)
