def valid_numbers(sudoku):
# after is_square
    for row in sudoku:
        try:
            assert isinstance(row, list)
        except AssertionError:
            return False, "Please input a list of lists separated by commas ([[x, y, z], [z, x, y], [y, z, x]])."
        try:
            for column in row:
                assert isinstance(column, int)
                numbers = [column for column in row in sudoku]
        except AssertionError:
            return False, "Please input integer values."
        try:
            range_of_valid_numbers = range(len(sudoku) + 1)
            assert column in range_of_valid_numbers    # check if numbers are in range
            for column in range_of_valid_numbers:
                assert numbers.count(column) == len(sudoku)    # check if number count is correct
        except AssertionError:
            return False, "Bad sudoku, try again!"
    return True

if __name__ == '__main_':
    assert valid_numbers([[1, 2, 3],
                          [2, 3, 1],
                          [3, 1, 2]]) == True
        
    assert valid_numbers([[1, 2, 2],
                          [2, 3, 1],
                          [3, 1, 2]]) == False