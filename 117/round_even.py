def round_even(number: float):
    """Takes a number and returns it rounded even"""

    int_num = int(number)
    if number - int_num == 0.5:
        if int_num % 2 == 0:
            rounded = int_num
        else:
            rounded = int_num + 1
    else:
        rounded = round(number)
    return rounded
