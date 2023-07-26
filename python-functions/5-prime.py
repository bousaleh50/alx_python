def is_prime(number):
    if number < 2:
        return False

    root = int(number ** 0.5)

    for i in range(2, root + 1):
        if number % i == 0:
            return False

    return True


print(is_prime(15))
