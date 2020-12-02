import re
with open('./input.txt', 'r') as f:
    r = [i.strip() for i in f.readlines()]

valid = 0
for i in r:
    matches = re.search("^([0-9]+)-([0-9]+) ([a-z])(?::) ([a-z]+)", i, re.IGNORECASE)
    min_v, max_v = int(matches.group(1)), int(matches.group(2))
    if min_v <= matches.group(4).count(matches.group(3)) <= max_v:
        valid += 1

print(valid)
