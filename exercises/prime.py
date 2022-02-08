def prime_check(num):
    """Returns True if a given number is a prime number."""
    for i in range(2, int(num / 2) + 1):
        return not num % i == 0


print(prime_check(int(input("Enter a number:"))))
