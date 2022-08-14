import random

with open("rawfile.txt", "w") as file:
    for line in range(0, 40000000):
        file.write(f"{random.randint(0, 200)}\n")
        
 

dct = {i : 0 for i in range(1, 201)}

with open("rawfile.txt", "r") as file:
    for line in file:
        line = line.strip(' \n')
        lst = list(line.split(" "))
        for i in lst:
            dct[int(i)] += 1

with open('sortedfile.txt', 'w') as file:
    for i in dct.keys():
        for j in range(0, dct[i]):
            file.write(str(i) + " ")
            file.write("\n")
