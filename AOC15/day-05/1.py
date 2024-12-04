import re

# path = r"AOC15\day-05\test.txt"
path = r"AOC15\day-05\input.txt"

with open(path) as f:
    l = f.read().split("\n")

nice = 0

pattern1 = "a|e|i|o|u"
pattern2 = "|".join([chr(i)*2 for i in range(97, 123)])
pattern3 = "ab|cd|pq|xy"

for string in l:
    if len(re.findall(pattern1, string)) >= 3 and len(re.findall(pattern2, string)) >= 1 and len(re.findall(pattern3, string)) == 0:
        nice += 1

print(nice)