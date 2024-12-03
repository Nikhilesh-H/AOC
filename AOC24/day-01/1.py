# path = r"AOC24\day-01\test.txt"
path = r"AOC24\day-01\input.txt" 

with open(path) as f:
    l = f.readlines()

# Split the numbers into two halves and sort them
left_num = sorted([int(i.split()[0]) for i in l])
right_num = sorted([int(i.split()[1]) for i in l])

result = 0

# Iteratively add the difference between corresponding numbers
for i in range(len(l)):
    result += abs(left_num[i] - right_num[i])

print(result)