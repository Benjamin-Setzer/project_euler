import pytest
from project_euler.e4 import is_pal, find_largest_pal_product

@pytest.fixture(params=[9, 11, 121, 4004, 333, 805508])
def success(request):
    return request.param

def test_is_pal_true(success):
    assert is_pal(success) == True

@pytest.fixture(params=[12, 13, 42, 69, 5505])
def failure(request):
    return request.param
	
def test_is_pal_false(failure):
    assert is_pal(failure) == False 
	
def test_find_largest_pal_product1():
    assert find_largest_pal_product(0, 10) == 9
		
def test_find_largest_pal_product2():
    assert find_largest_pal_product(0,12) == 121
