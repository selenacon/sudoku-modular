# Sudoku [http://en.wikipedia.org/wiki/Sudoku]
# is a logic puzzle where a game
# is defined by a partially filled
# 9 x 9 square of digits where each square
# contains one of the digits 1,2,3,4,5,6,7,8,9.
# For this question we will generalize
# and simplify the game.

# Define a procedure, check_sudoku,
# that takes as input a square list
# of lists representing an n x n
# sudoku puzzle solution and returns the boolean
# True if the input is a valid
# sudoku square and returns the boolean False
# otherwise.

# A valid sudoku square satisfies these
# two properties:

#   1. Each column of the square contains
#       each of the whole numbers from 1 to n exactly once.

#   2. Each row of the square contains each
#       of the whole numbers from 1 to n exactly once.

# You may assume the the input is square and contains at
# least one row and column.
def check_rows(sudoku):
    for row in sudoku:
        for column in row:
            try: assert column in range(len(sudoku) + 1)
            except AssertionError:
                return False
            try:
                assert sudoku.count(column) == len(sudoku) +1
            except AssertionError:
                return False
    return True

def check_sudoku(sudoku):
    try: assert isinstance(sudoku, list)
    except AssertionError:
        sudoku = list(sudoku)
    finally: assert isinstance(sudoku, list)

if __name__ == '__main__':
    assert check_rows([[1, 2, 3],
                       [2, 3, 1],
                       [3, 1, 2]]) == True
    
    assert check_rows([[1, 2, 2],
                           [2, 3, 1],
                           [3, 1, 2]]) == False
    
    assert check_sudoku([[1, 2, 3],
                         [2, 3, 1],
                         [3, 1, 2]]) == True

    assert check_sudoku([[1, 2, 3, 4],
                         [2, 3, 1, 3],
                         [3, 1, 2, 3],
                         [4, 4, 4, 4]]) == False

    assert check_sudoku([[1, 2, 3, 4],
                         [2, 3, 1, 4],
                         [4, 1, 2, 3],
                         [3, 4, 1, 2]]) == False

    assert check_sudoku([[1, 2, 3, 4, 5],
                         [2, 3, 1, 5, 6],
                         [4, 5, 2, 1, 3],
                         [3, 4, 5, 2, 1],
                         [5, 6, 4, 3, 2]]) == False

    assert check_sudoku([['a', 'b', 'c'],
                         ['b', 'c', 'a'],
                         ['c', 'a', 'b']]) == False

    assert check_sudoku([[1, 1.5],
                         [1.5, 1]]) == False

    assert check_sudoku([[1, 0, 0, 0],
                         [0, 1, 0],
                         [0, 0, 0, 1]]) == False