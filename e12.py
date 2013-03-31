"""
http://projecteuler.net/problem=12
"""

def find_tri_num(num_divisors):
	increment = 1
	triangle_number = 1

	while True:
		if len(get_divisors(triangle_number)) > num_divisors:
			return triangleNumber
		increment += 1
		triangle_number += increment
		print triangle_number
		
def get_divisors(num):
	divisors = set()
	for i in range(1, num+1):
		if num % i == 0:
			divisors.add(num)
	
	return divisors

if __name__ == '__main__':
	print find_tri_num(500)
