with open('day1/input.txt', 'r') as f:
    r = [int(i.strip()) for i in f.readlines()]
answer = [i * r[l] for i in r for l in range(0, len(r)) if i + r[l] == 2020][0]
# an = 0
# for i in r:
#     for l in range(0, len(r)):
#         if i + r[l] == 2020:
#             an = i * r[l]
# print(an)
print(answer)
