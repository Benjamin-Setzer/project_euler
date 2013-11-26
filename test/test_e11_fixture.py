from project_euler.e11 import GridSolver

import pytest

example_grid = '\n'.join(['1 1 1 2',
                         '1 1 1 3',
                         '1 1 1 1',
                         '1 1 1 1']
                        )

invalid_grid_format1 = ''.join(['2 1 1 1',
                                '1 1 1 1',
                                '3 1 1 1',
                                '1 1 1 1'])
@pytest.fixture()
def gs():
    return GridSolver(example_grid)

def test_solve(gs):
    assert gs.solve() == 6
        
def test_check_horizontal(gs):
    gs._check_horizontal()
    assert gs._max_val == 3
        
def test_check_vertical(gs):
    gs._check_vertical()
    assert gs._max_val == 6
    
def test_check_diagonal(gs):
    gs._check_diagonal()
    assert gs._max_val == 2
        
def test_update_max(gs):
    gs._update_max(5)
    assert gs._max_val == 5
        
def test_update_max_no_change(gs):
    max_val_init = gs._max_val
    gs._update_max(-1)
    assert gs._max_val == max_val_init

def test_valid_init():
    assert isinstance(GridSolver(example_grid), GridSolver)
        
def test_invalid_init():
    pytest.raises(ValueError, GridSolver, invalid_grid_format1)
        
