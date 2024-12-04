# path = r"AOC24\day-01\test.txt"
path = r"AOC24\day-01\input.txt" 

with open(path) as f:
    l = f.readlines()

# Split the numbers into two halves and sort them
left_num = sorted([int(i.split()[0]) for i in l])
right_num = sorted([int(i.split()[1]) for i in l])

# Frequency of each number in the second list
right_freq = {}
for i in set(right_num):
    right_freq[i] = right_num.count(i)

result = 0

# Iteratively add the product of each number in the first list with its corresponding freuquency
for i in left_num:
    if i in right_freq:
        result += i * right_freq[i]

print(result)