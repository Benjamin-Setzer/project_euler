"""
http://projecteuler.net/problem=12
"""
"""
The solution is 76576500.
It took 38 min and 52 seconds on a 2.3 GHz PC...

Switched from pure python to inline c for performance reasons.
The inline c is about 15 -20 times as fast.
Note: Due to the nature of weave, the first call of a c function is slower.
"""

from scipy import weave
from scipy.weave import converters
from math import sqrt

ccode = """
        int factors[600] = {0};
        int factor_idx = 0;
        for(unsigned long int i=1; i <= number; i++){
            if (number % i == 0){
                factors[factor_idx] = i;
                factor_idx++;
            }
            if(factor_idx > 500){break;}
        }
        
        return_val = factor_idx;
        """

def find_tri_num(num_divisors):    
    increment = 1
    triangle_number = 1

    while True:
        count_divisors = get_divisors(triangle_number)
        if count_divisors > num_divisors:
            return triangle_number
        increment += 1
        triangle_number += increment

def get_divisors_c(number):
    i= weave.inline(ccode, ['number'],
                type_converters=converters.blitz,
                compiler = 'gcc')

    return i
            
def get_divisors(num):
    divisors = 0
    for i in xrange(1, int(sqrt(num+1))):
        if num % i == 0:
            divisors += 1
    
    return divisors

if __name__ == '__main__':
    from datetime import datetime
    st = datetime.now()
    print find_tri_num(500)
    end = datetime.now()
    print 'duration: ', end - st
