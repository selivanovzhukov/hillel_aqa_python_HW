def generate_even_nums(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i


# for num in generate_even_nums(10):
#     print("Even numbers till 10: ", num)


def generate_fibonacci(n):
    a = 0
    b = 1
    while a <= n:
        yield a
        a, b = b, a + b

# for num in generate_fibonacci(10):
#     print("Fibonacci numbers till 10: ", num)

