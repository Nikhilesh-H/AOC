import re

# path = r"AOC15\day-05\test.txt"
path = r"AOC15\day-05\input.txt"

with open(path) as f:
    l = f.read().split("\n")

nice = 0

pattern1 = r"([a-z][a-z]).*\1"
pattern2 = "|".join([chr(i)+".{1}"+chr(i) for i in range(97, 123)])

for string in l:
    if re.search(pattern1, string) and re.search(pattern2, string):
        nice += 1

print(nice)