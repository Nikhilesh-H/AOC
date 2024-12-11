# path = r"AOC15\day-12\test.txt"
path = r"AOC15\day-12\input.txt"

with open(path) as f:
    string = f.read()

import json
string = json.loads(string)

main = ""

for key in list(string.keys()):

    value = str(string[key])

    char = 0

    while char < len(value):

        main += value[char]

        # Remove objects that contain red
        if main[-6:] == ": 'red":

            left = 1
            for i in range(len(main)-1, -1, -1):
                if main[i] == '}':
                    left += 1
                elif main[i] == '{':
                    left -= 1
                if left == 0:
                    main = main[:i]
                    break

            right = 1
            for i in range(char, len(value)):
                if value[i] == '{':
                    right += 1
                elif value[i] == '}':
                    right -= 1
                if right == 0:
                    char = i
                    break
        
        char += 1

main += "."

result = 0

num = ""

for i in main:
    if i.isdigit() or i == "-":
        num += i
    else:
        if num != "":
            result += int(num)
        num = ""

print(result)