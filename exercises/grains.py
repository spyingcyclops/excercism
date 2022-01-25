def square(number):
    if 0 < number < 65:
        return 2 ** (number - 1)
    else:
        raise ValueError("Number is out of range.")


def total():
    return 2 ** 64 - 1

