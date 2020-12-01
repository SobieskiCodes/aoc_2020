from itertools import combinations
from math import prod
import time
start = time.time()
with open('day1/input.txt', 'r') as f:
    r = [int(i.strip()) for i in f.readlines()]
print(f"p1: {next(i * r[l] for i in r for l in range(0, len(r)) if i + r[l] == 2020)} time: {time.time() - start}")
print(f"p2: {prod(next(i for i in combinations(r, 3) if sum(i) == 2020), start=1)} time: {time.time() - start}")
