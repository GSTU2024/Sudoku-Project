from behave import given, when, then
from sudoku import solve  # Import the solve function from your Sudoku app

# Given: The Sudoku board is partially filled
@given('the Sudoku board is partially filled')
def step_given_board(context):
    context.board = [
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

# Given: The Sudoku board is unsolvable
@given('the Sudoku board is unsolvable')
def step_given_unsolvable_board(context):
    context.board = [
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
    context.board[0][0] = 9  # Making the board unsolvable

# When: I solve the puzzle
@when('I solve the puzzle')
def step_when_solve(context):
    context.solved = solve(context.board)

# Then: The puzzle should be solved
@then('the puzzle should be solved')
def step_then_solved(context):
    assert context.solved == True

# Then: The puzzle should not be solved
@then('the puzzle should not be solved')
def step_then_unsolved(context):
    assert context.solved == False
