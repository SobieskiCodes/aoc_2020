from itertools import combinations
import operator
import functools
with open('day1/input.txt', 'r') as f:
    r = [int(i.strip()) for i in f.readlines()]

answer = functools.reduce(operator.mul, list([c for c in combinations(r, 3) if sum(c) == 2020][0]), 1)
# for c in combinations(r, 3):
#     if sum(c) == 2020:
#         print(c)
#         for i in c:
#             answer *= i
print(answer)
