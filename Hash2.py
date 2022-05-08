h = dict()
N = int(input())
duplicates = 0

for _ in range(N):
    inp = input()
    value = h.setdefault(inp,1)
    if value == 2:
        duplicates += 1

    h[inp] = value + 1
