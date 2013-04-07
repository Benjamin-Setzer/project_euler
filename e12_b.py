"""
http://projecteuler.net/problem=12

This time with a better algorithm instead of brute force. -> Results in much better execution time compared to original approach.
"""

import math
from datetime import datetime

st = datetime.now()

num = 0
inc = 1
while True:
    num += inc
    inc += 1
    f = 0
    for i in xrange(1, int(math.sqrt(num))):
        if num % i == 0:
            f += 2
    if num % int(math.sqrt(num)) == 0:
        f += 1
    if f > 500:
        break

print num
end = datetime.now()
print 'duration: ', end -st        
