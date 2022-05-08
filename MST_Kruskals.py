N,M = [int(i) for i in input().split()]
adjlist = []

for i in range(M):
    u,v,p = [int(i) for i in input().split()]
    adjlist.append((u,v,p))

#print(adjlist)

def take_third(elem):
    return elem[2]

sortedlist = sorted(adjlist, key=take_third)

#print(sortedlist)

def find(u,i):
	if i == u[i]: return i
	return find(u,u[i])

def connected(u,i,j):
	return find(u,i) == find(u,j)



class UnionFind:
    def __init__(self,n):
        self.p = list(range(n))
        self.s = [1]*N
    
    def find(self,i):
        if self.p[i] != i:
            self.p[i] = self.find(self.p[i])
        return self.p[i]

    def union(self,i,j):
        r_small, r_great = self.find(i), self.find(j)
        if self.s[r_small] > self.s[r_great]:
            r_small, r_great = r_great, r_small
        if r_small != r_great:
            self.s[r_great] += self.s[r_small]
            self.p[r_small] = r_great


N,M = map(int, input.split())

sets = UnionFind(N+1)

#kan bruge sort i stedet for sorted for at lave listen in-place for at spare plads
#edges = [map(int,input().split()) for i in range(M)]
#edges.sort(key=lambda element: element[2])
edges = [tuple(map(int,input().split())) for i in range(M)]

edges = sorted(edges, key=lambda element: element[2]) #lambda function like @ in MATLAB, anonymous function
total_price = 0
for bi,bj,price in edges:
    if sets.find(bi) != sets.find(bj):
        sets.union(bi,bj)
        total_price += price


from heapq import heappush, heappop

adjl = [[].copy() for _ in range(N+1)]

marked = [False]*(N+1)

total_price = 0

for i in range(M):
    bi,bj,price = map(int, input().split())
    adjl[bi].append((price,bj))
    adjl[bj].append((price,bi))

heap = [(0,1)]

#(8,2,4,3,"hej") < 9,2,"kan i set det"

n_marked = 0

#while n_marked < N:
for i in range(M+1):
    price, node = heappop(heap)
    if not marked[node]:
        total_price += price
        marked[node] = True
        #n_marked += 1
        for p,n in adjl[node]:
            heappush(heap, (p,n))

print(total_price)