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

def is_square(sudoku):
    for row in sudoku:
        while len(row) != len(sudoku):
            return False
    return True

def valid_numbers(sudoku):
    all_numbers = []
    counted_number = 1
    max_number_count = len(sudoku)    # assuming that is_square is True, the amount of times a singular number appears should EQUAL to the length of the sudoku itself
    for row in sudoku:
        try:
            assert isinstance(row, list)
        except AssertionError:
            print("Please input a list of lists separated by commas ([[x, y, z], [z, x, y], [y, z, x]]).")
            return False
        all_numbers += [column for column in row if isinstance(column, int)]   # iterate all the numbers within the sudoku into a singular list all_numbers
    while counted_number <= max_number_count:
        if all_numbers.count(counted_number) != max_number_count:   # count the times a singular number appears in all_numbers and check if it equals to what is expected
            print("This sudoku is wrong, try again!")
            return False
        else: counted_number += 1
    return True

def check_sudoku(sudoku):
    try:
        assert isinstance(sudoku, list)
    except AssertionError:
        print("Please input a list of lists separated by commas ([[x, y, z], [z, x, y], [y, z, x]]).")
        return False
    
    try:
        assert is_square(sudoku)
    except AssertionError:
        print("Bad sudoku: sudoku isn't square.")
        return False
    
    return valid_numbers(sudoku)

if __name__ == '__main__':
    assert is_square([[1, 2, 3], 
                      [3, 1, 2], 
                      [2, 3, 1]]) == True
        
    assert is_square([[3, 1, 4, 2], 
                      [4, 2, 3, 1], 
                      [2, 3, 1, 4]]) == False
        
    assert is_square([[3, 1, 4, 2], 
                      [4, 2, 3, 1], 
                      [2, 3, 1, 4], 
                      [1, 4, 2, 3]]) == True
        
    assert is_square([[1, 2], 
                      [3, 2, 1]]) == False
    
    assert valid_numbers([[1, 2, 3],
                          [2, 3, 1],
                          [3, 1, 2]]) == True
            
    assert valid_numbers([[1, 2, 2],
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