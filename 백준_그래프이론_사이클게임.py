# 백준 사이클 게임
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
parent = [0] * (n + 1)
cycle = 0

for i in range(1, n + 1):
    parent[i] = i 

for i in range(1, m + 1):
    a, b = map(int, input().split())
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = i 
        break
    else:
        union_parent(parent, a, b)

print(cycle)
