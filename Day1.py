# 1
with open('day_one_files/ex_1', 'r') as f:
    line_sum = []
    while True:
        line = f.readline()
        if not line:
            break

        line_sum.append(sum(map(int, line.strip().split(" "))))
    print(sum(line_sum))

# 2
new_file = open("day_one_files/ex_2_new", 'w')
with open('day_one_files/ex_2', 'r') as f:
    while True:
        line = f.readline()
        if not line:
            break
        new_file.write(line.title())
    new_file.close()

# 3
with open('day_one_files/ex_1') as f:
    digit_count = dict()
    while True:
        line = f.readline().strip()
        if not line:
            break
        for x in line.split(" "):
            if digit_count.get(x):
                digit_count[x] += 1
            else:
                digit_count[x] = 1
    print(digit_count)

# 4
with open('day_one_files/ex_2') as f:
    symbol_count = dict()
    while True:
        line = f.readline().strip()
        if not line:
            break
        for x in line:
            if x.isascii():
                if symbol_count.get(x):
                    symbol_count[x] += 1
                else:
                    symbol_count[x] = 1
    print(symbol_count)

# 5
string = input()
new_string = ''
ln = 0
while ln < len(string):
    if (ln + 1) % 3 != 0:
        new_string += string[ln]
    ln += 1
print(new_string)

# 6
with open('day_one_files/ex_2') as f:
    digit_count = dict()
    while True:
        line = f.readline().strip()
        if not line:
            break
        for x in line.split(" "):
            if digit_count.get(x):
                digit_count[x] += 1
            else:
                digit_count[x] = 1
    print(digit_count)

# 7
lst = [4, 3, 5, 1, 6, 8, 12, 0, 6]
lst_new = list(map(lambda x: x ** 2, lst))
lst_new.sort()
print(lst_new)


# 8
def sum_of_number(number):
    sum_n = 0
    while number != 0:
        sum_n += number % 10
        number //= 10
    return sum_n


print(sum_of_number(4637))


# 9
def mul_and_sum_subtract(number):
    sum_n = 0
    mul_n = 1
    while number != 0:
        last_n = number % 10
        sum_n += last_n
        mul_n *= last_n
        number //= 10
    return mul_n - sum_n


print(mul_and_sum_subtract(4637))

# 10
from math import ceil, floor


def odd(start, end):
    odd_count = 0
    for x in range(ceil(start), floor(end) + 1):
        if x % 2 == 1:
            odd_count += 1
    print(odd_count)


print(odd(2.7, 7.9))
