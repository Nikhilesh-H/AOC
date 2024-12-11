import re

# path = r"AOC15\day-11\test.txt"
path = r"AOC15\day-11\input.txt"

with open(path) as f:
    password = f.read()

def update(password):
    if password[-1] != "z":
        return password[:-1] + chr(ord(password[-1])+1)
    return update(password[:-1]) + "a"

condition1 = "|".join([chr(i)+chr(i+1)+chr(i+2) for i in range(97, 121)])
condition2 = "i|o|l"
condition3 = "|".join([chr(i)+chr(i) for i in range(97, 123)])

while not(re.findall(condition1, password)) or re.findall(condition2, password) or len(re.findall(condition3, password)) != 2:
    password = update(password)

print(password)