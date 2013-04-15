#import sys
#sys.path.append('../.')
import unittest
from projecteuler.e4 import is_pal, find_largest_pal_product

class Test_is_pal(unittest.TestCase):
	def test_true(self):
		for i in [9, 11, 121, 4004, 333, 805508]:
			self.assertTrue(is_pal(i), msg="function returned False, but %d is pal" %i)
	
	def test_false(self):
		for i in [12, 13, 42, 69, 5505]:
			self.assertFalse(is_pal(i), msg="function returned True, but %d is not pal" %i)
	
class Test_find_largest_pal_product(unittest.TestCase):
	def test_example1(self):
		self.assertEqual(find_largest_pal_product(0, 10), 9)
		
	def test_example2(self):
		self.assertEqual(find_largest_pal_product(0,12), 121)
