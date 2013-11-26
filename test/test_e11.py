import pytest
from project_euler.e11 import GridSolver

example_grid = '\n'.join(['1 1 1 2',
                        '1 1 1 3',
                        '1 1 1 1',
                        '1 1 1 1']
                        )

invalid_grid_format1 = ''.join(['2 1 1 1',
                        '1 1 1 1',
                        '3 1 1 1',
                        '1 1 1 1']
                        )

class Test_e11_functions():                        
    def setup_method(self, method):
        self.gs = GridSolver(example_grid)
    
    def test_solve(self):
        assert self.gs.solve() == 6
        
    def test_check_horizontal(self):
        self.gs._check_horizontal()
        assert self.gs._max_val == 3
        
    def test_check_vertical(self):
        self.gs._check_vertical()
        assert self.gs._max_val == 6
        
    def test_check_diagonal(self):
        self.gs._check_diagonal()
        assert self.gs._max_val == 2
        
    def test_update_max(self):
        self.gs._update_max(5)
        assert self.gs._max_val == 5
        
    def test_update_max_no_change(self):
        max_val_init = self.gs._max_val
        self.gs._update_max(-1)
        assert self.gs._max_val == max_val_init
        
        
class Test_e11_initilization():
    
    def test_valid_init(self):
        assert isinstance(GridSolver(example_grid), GridSolver)
        
    def test_invalid_init(self):
        pytest.raises(ValueError, GridSolver, invalid_grid_format1)
        
