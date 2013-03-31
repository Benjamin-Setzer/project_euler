"""
http://projecteuler.net/problem=7
"""

def get_primes(amount):
	if amount <  1:
		raise ValueError('amount must be >= 1')
	primes = [2] #we start with the prime 2, so that only uneven numbers have to be checked
	i = 3  
	while len(primes) < amount:
		is_prime = True
		for prime in primes:
			if i % prime == 0:
				is_prime = False
		if is_prime:
			primes.append(i)
		i += 2
			
	return primes

if __name__ == '__main__':
	print get_primes(10001)[-1]
