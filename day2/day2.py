import re
with open('./input.txt', 'r') as f:
    r = [i.strip() for i in f.readlines()]

valid = 0
p2_valid = 0
for i in r:
    matches = re.search("^([0-9]+)-([0-9]+) ([a-z])(?::) ([a-z]+)", i, re.IGNORECASE)
    min_v, max_v = int(matches.group(1)), int(matches.group(2))
    if min_v <= matches.group(4).count(matches.group(3)) <= max_v:
        valid += 1
    a = matches.group(4)[min_v - 1]
    b = matches.group(4)[max_v - 1]
    if not a == matches.group(3) and b != matches.group(3) or a != matches.group(3) and b == matches.group(3):
        p2_valid += 1

print(f"p1: {valid}")
print(f"p2: {p2_valid}")
