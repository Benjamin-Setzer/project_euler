"""
http://projecteuler.net/problem=12
"""
import math

def find_tri_num(num_divisors):
	lower_bound = math.factorial(10) 
	#since we are looking for 500 unique divisors this is the lower bound
	#
	
	increment = 1
	triangle_number = 1

	while True:
		print lower_bound - triangle_number
		if triangle_number >= lower_bound:
			count_divisors = len(get_divisors(triangle_number))
			print triangle_number, count_divisors
			if count_divisors > num_divisors:
				return triangle_Number
		increment += 1
		triangle_number += increment
		
def get_divisors(num):
	divisors = []
	for i in xrange(1, num+1):
		if num % i == 0:
			divisors.append(i)
	
	return divisors

if __name__ == '__main__':
	print find_tri_num(500)
