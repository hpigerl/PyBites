WHITE, BLACK = " ", "#"


def create_chessboard(size=8):
    """Create a chessboard with of the size passed in.
    Don't return anything, print the output to stdout"""
    if size % 2 > 0:
        raise ValueError("Size must be an even number")
    row_a = "".join([WHITE + BLACK for i in range(int(size / 2))])
    row_b = "".join([BLACK + WHITE for i in range(int(size / 2))])
    for i in range(size):
        print(row_a if i % 2 == 0 else row_b)
    return None
