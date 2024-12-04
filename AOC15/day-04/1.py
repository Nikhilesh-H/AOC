import hashlib

# path = r"AOC15\day-04\test.txt"
path = r"AOC15\day-04\input.txt"

with open(path) as f:
    l = f.read().split("\n")

for key in l:
    copy = key
    value = 0
    while not(hashlib.md5(copy.encode()).hexdigest().startswith("00000")):
        value += 1
        copy = key + str(value)
    print(value)