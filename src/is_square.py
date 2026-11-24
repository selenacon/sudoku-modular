def is_square(sudoku):
    for row in sudoku:
        while len(row) != len(sudoku):
            return False
    return True

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