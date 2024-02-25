def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def sum_even_fib(limit):
    a, b = 0, 1
    total = 0
    while a <= limit:
        if a % 2 == 0:
            total += a
        a, b = b, a + b
    return total

limit = 4000000
print('The sum of the even fibs are %d'  % sum_even_fib(limit))

