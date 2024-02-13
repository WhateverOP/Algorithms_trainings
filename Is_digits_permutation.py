def is_digits_permutation(x, y):
    def count_digits(n):
        digits = [0]*10
        while n != 0:
            digits[n % 10] += 1
            n = n // 10
        return digits
    
    digits_x = count_digits(x)
    digits_y = count_digits(y)
    for digit in range(10):
        if digits_x[digit] != digits_y[digit]:
            return False
    return True