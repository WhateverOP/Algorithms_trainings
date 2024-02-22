def factorial(n):
    if n == 1:
        return 1
    prev_factorial = factorial(n - 1)
    return n * prev_factorial

print(factorial(4))