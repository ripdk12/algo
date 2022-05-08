def find(u,i):
	if i == u[i]: return i
	return find(u,u[i])

	##u[i] = find(u,u[i]) return u[i] -- path compression

def add(u, size, i, j):
	rooti = find(u,i)
	rootj = find(u,j)
	if size[rooti] < size[rootj]:
		rooti,rootj = rootj,rooti
	u[rootj] = rooti
	size[rooti] += size[rootj]

def connected(u,i,j):
	return find(u,i) == find(u,j)

N,M = [int(i) for i in input().split()]
u = [i for i in range(N)]
size = [i for _ in range(N)]

for _ in range(M):
	line = input().split()
	i,j = [int(i) for i in line[1:]]

	if line[0] == "A":
		add(u,size,i,j)
	else:
		print("YES") if connected(u,i,j) else: print("NO")
