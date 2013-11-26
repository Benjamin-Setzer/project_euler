import pytest
from project_euler.e4 import is_pal, find_largest_pal_product

class Test_is_pal():
	def test_true(self):
		for i in [9, 11, 121, 4004, 333, 805508]:
			assert is_pal(i) == True
	
	def test_false(self):
		for i in [12, 13, 42, 69, 5505]:
			assert is_pal(i) == False 
	
class Test_find_largest_pal_product():
	def test_example1(self):
		assert find_largest_pal_product(0, 10) == 9
		
	def test_example2(self):
		assert find_largest_pal_product(0,12) == 121
