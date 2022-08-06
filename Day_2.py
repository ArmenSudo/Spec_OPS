# 1
def strmove_impl(line, step):
    if step >= len(line):
        step = (step - len(line) * (step // len(line)))
    return line[-step:] + line[:-step]


print(strmove_impl("armen", 2002))


# 2
def sum_multiples(below, n1, n2):
    sum_mult = 0
    for x in range(1, below):
        if x % n1 == 0 or x % n2 == 0:
            sum_mult += x
    print(sum_mult)


sum_multiples(1000, 3, 5)


# 3
def sum_even_fib(n):
    sum_n = 2
    n1 = 1
    n2 = 2
    for x in range(2, n):
        n1, n2 = n2, n1 + n2
        if n2 % 2 == 0:
            sum_n += n2
        if n1 >= n:
            break
    return sum_n


print(sum_even_fib(4 * 10 ** 6))
