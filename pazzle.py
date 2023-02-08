def column(board: list) -> bool:
    """ """
    rotated = [
        "".join(column) for column in list(zip(*[list(row) for row in board]))
        ]
    return rotated
