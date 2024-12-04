# path = r"AOC15\day-02\test.txt"
path = r"AOC15\day-02\input.txt"

with open(path) as f:
    l = f.readlines()

result = 0

for wrapper in l:
    l, w, h = [int(i) for i in wrapper.split('x')]
    result += 2 * min(l+w, w+h, h+l) + l*w*h
    
print(result)