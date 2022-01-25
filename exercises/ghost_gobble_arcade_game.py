# def eat_ghost(PowPel, TouchGhost):
#     if PowPel and TouchGhost:
#         return True
#     else:
#         return False


# def score(touching_power_pellet, touching_dot):
#     if touching_power_pellet or touching_dot:
#         return True
#     else:
#         return False


# def lose(power_pellet_active, touching_ghost):
#     if not power_pellet_active and touching_ghost:
#         return True
#     else:
#         return False


# def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
#     if has_eaten_all_dots and not (not power_pellet_active and touching_ghost):
#         return True
#     else:
#         return False


def eat_ghost(power_pellet_active, touching_ghost):
    return power_pellet_active and touching_ghost


def score(touching_power_pellet, touching_dot):
    return touching_power_pellet or touching_dot


def lose(power_pellet_active, touching_ghost):
    return not power_pellet_active and touching_ghost


def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
    return has_eaten_all_dots and not (not power_pellet_active and touching_ghost)
