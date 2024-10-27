def is_prime(func):
    def wrapper(*numbers):
        number = func(*numbers)
        prime = True
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                prime = False
        if prime:
            print("Простое")
        else:
            print("Составное")

        return number

    return wrapper


@is_prime
def sum_three(a, b, c):
    _sum = a + b + c
    return _sum


result = sum_three(2, 3, 6)
print(result)
