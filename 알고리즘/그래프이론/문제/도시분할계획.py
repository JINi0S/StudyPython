n, m = map(int, input().split())




edges=[]

for i in range(m):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))