with open('input.txt', 'r') as f:
    r = [int(i.strip()) for i in f.readlines()]
answer = [i * r[l] for i in r for l in range(0, len(r)) if i + r[l] == 2020][0]
print(answer)
