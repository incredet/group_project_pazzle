def validate_row(board):
    """
    Return True if there are no equal numbers in a row else False.
    >>> validate_row(board = ["****1****", "***12****", "**123****",\
 "*1234****", "123456789", "12345678*", "1234567**", "123456***", "12345****"])
    True
    >>> validate_row(board = ["****1*1**", "***12****", "**123****",\
 "*1234****", "123456789", "12345678*", "1234567**", "123456***", "12345****"])
    False
    >>> validate_row(board = ["****1****", "***11****", "**123****",\
 "*1234****", "123456789", "12345678*", "1234567**", "123456***", "12345****"])
    False
    >>> validate_row(board = ["**** ****", "***1 ****", "**  3****",\
 "* 4 1****", "     9 5 ", " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    False
    """
    for row in board:
        for element in row:
            if element != '*' and element != ' ' and row.count(element) > 1:
                return False
    return True
