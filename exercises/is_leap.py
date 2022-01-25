def leap_year(year):
    return (year % 4 == 0) and not (year % 100 == 0) and (year % 4 == 0)


print(leap_year(2000))
