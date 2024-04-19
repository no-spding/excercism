def construct_chessboard():
    chessboard = {0: 1}
    squares = range(1, 64)
    for square in squares:
        chessboard[square] = (chessboard[square-1]) * 2
    return chessboard

def square(number):
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    else:
        return construct_chessboard().get(number-1)

def total():
    chessboard = construct_chessboard()
    total_grains = 0
    for square in chessboard:
        total_grains = total_grains + chessboard[square]
    return total_grains
