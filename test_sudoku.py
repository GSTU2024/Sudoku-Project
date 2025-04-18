import pytest
import time
from GUI import Grid, find_empty, valid

@pytest.fixture
def sample_grid():
    """Create a sample Grid instance for testing."""
    return Grid(9, 9, 540, 540, None)  # No window needed for testing

@pytest.mark.benchmark
def test_solve_performance(sample_grid, benchmark):
    """Benchmark Sudoku solving time."""
    benchmark(sample_grid.solve)

def test_valid_move():
    """Test valid number placement in Sudoku."""
    board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    assert valid(board, 2, (0, 2)) == True  # Valid placement
    assert valid(board, 3, (0, 2)) == False  # Invalid placement

def test_find_empty():
    """Test finding an empty position in the Sudoku grid."""
    board = [
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 0]  # Empty cell
    ]

    assert find_empty(board) == (8, 8)
    board[8][8] = 9  # Fill it
    assert find_empty(board) == None  # Now it's solved