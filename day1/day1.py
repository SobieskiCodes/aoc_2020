from itertools import combinations
import operator
import functools
with open('day1/input.txt', 'r') as f:
    r = [int(i.strip()) for i in f.readlines()]
print(f"p1: {[i * r[l] for i in r for l in range(0, len(r)) if i + r[l] == 2020][0]}")
print(f"p2: {functools.reduce(operator.mul, list([c for c in combinations(r, 3) if sum(c) == 2020][0]), 1)}")
