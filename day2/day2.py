import re
r = [i.strip() for i in open('./input.txt', 'r').readlines()]
matches = [re.search("^([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)", i, re.IGNORECASE) for i in r]  # (\d+)-(\d+) (.): (\w+)
p1_valid = f"p1: {len([i for i in matches if int(i.group(1)) <= i.group(4).count(i.group(3)) <= int(i.group(2))])}"
p2_valid = f"p2: {len([i for i in matches if (i.group(4)[int(i.group(1)) - 1] == i.group(3) and i.group(4)[int(i.group(2)) - 1] != i.group(3)) or (i.group(4)[int(i.group(1)) - 1] != i.group(3) and i.group(4)[int(i.group(2)) - 1] == i.group(3))])}"
print(f"{p1_valid}\n{p2_valid}")
