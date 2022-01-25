def score(x, y):
    d = (x ** 2 + y ** 2) ** (1 / 2)
    if d > 10:
        return 0
    elif 10 >= d > 5:
        return 1
    elif 5 >= d > 1:
        return 5
    elif d <= 1:
        return 10

