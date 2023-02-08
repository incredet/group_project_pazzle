def check_col(board):
    """
    Function for checking every color in puzzle
    >>> check_col(["**** ****", "***1 ****", "**  3****", "* 4 1****", "     9 5 ",\
 " 6 183  *", "3   1  **", "  8  2***", "  2  ****"])
    False
    >>> check_col(["**** ****", "***1 ****", "**  3****", "* 4 1****", "     9 5 ",\
 " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    True
    """
    number = 4
    j = 0
    while number >= 0:
        angle = []
        for i in range(number, number+5):
            angle.append(board[i][j])
        angle.append(board[number+4][j+1:number+1])
        for elements in angle:
            if elements.isnumeric():
                if angle.count(elements) > 1:
                    return False
        j += 1
        number -= 1
    return True
