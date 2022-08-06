# 1
def sum_squared_and_sum_of_squares():
    sum1 = sum(range(1, 101)) ** 2
    sum2 = sum(map(lambda x: x ** 2, range(1, 101)))
    return sum1 - sum2


print(sum_squared_and_sum_of_squares())


# 2
def write_new():
    with open('day3_files/1.txt', 'r') as f:
        line = f.readline().split(",")
        new_line = open('day3_files/new_1', 'w')
        for x in line:
            x = x[1:-1]
            x = x.title()
            new_line.write(f"\"{x}\",")
        new_line.close()


write_new()


# 3
def isPalindrome(x: int) -> bool:
    return x == int(str(x)[::-1]) if x >= 0 else False


isPalindrome(121)
