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

def check_color(board):
    """
    Function for checking every color in puzzle
    >>> check_color(["**** ****", "***1 ****", "**  3****", "* 4 1****", "     9 5 ",\
 " 6 183  *", "3   1  **", "  8  2***", "  2  ****"])
    False
    >>> check_color(["**** ****", "***1 ****", "**  3****", "* 4 1****", "     9 5 ",\
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


def column(board: list) -> bool:
    """ """
    rotated = [
        "".join(column) for column in list(zip(*[list(row) for row in board]))
        ]
    return validate_row(rotated)

