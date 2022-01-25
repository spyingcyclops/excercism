EXPECTED_BAKE_TIME = 40


def bake_time_remaining(minutes_baked):
    """
    Return bake time remaining.

    This function takes minutes baked as an input argument
    and subtracts if from the total expected bake time,
    to return the time remaining.
    """
    return EXPECTED_BAKE_TIME - minutes_baked


def preparation_time_in_minutes(num_of_layers):
    """
    Return elapsed cooking time.

    This function takes two numbers representing the number of layers & the
    time already spent baking and calculates the total elapsed minutes
    spent cooking the lasagna.
    """
    return 2 * num_of_layers


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """
    Return time elapsed.

    This function takes two inputs - number of layers and elapsed bake time
    and calculates the combined time spend on preparing the layers and baking.

    """
    return elapsed_bake_time + (number_of_layers * 2)


print(EXPECTED_BAKE_TIME)  # 1
print(bake_time_remaining(30))  # 2
print(preparation_time_in_minutes(2))  # 3
print(elapsed_time_in_minutes(3, 20))  # 4

# 5 - see comments above
