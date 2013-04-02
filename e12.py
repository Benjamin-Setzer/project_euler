"""
http://projecteuler.net/problem=12
"""

from scipy import weave
from scipy.weave import converters

ccode = """
        int factors[600] = {0};
        int factor_idx = 0;
        for(int i=1; i <= number; i++){
            if (number % i == 0){
                factors[factor_idx] = i;
                factor_idx++;
            }
        }
        
        return_val = factor_idx;
        """

def find_tri_num(num_divisors):    
    increment = 1
    triangle_number = 1

    while True:
        count_divisors = get_divisors_c(triangle_number)
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
    divisors = []
    for i in xrange(1, num+1):
        if num % i == 0:
            divisors.append(i)
    
    return divisors

if __name__ == '__main__':
    from datetime import datetime
    st = datetime.now()
    print find_tri_num(500)
    end = datetime.now()
    print 'duration: ', end - st
