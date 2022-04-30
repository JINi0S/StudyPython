INF = int(1e9)

n,m = map(int, input().split())
gra=[[INF] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            gra[i][j]=0
            

for _ in range(m):
    a, b = map(int, input().split())
    gra[a][b] = 1
    gra[b][a]=1

x, k =map(int, input().split())

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            gra[a][b] = min(gra[a][b], gra[a][k]+gra[k][b])

dis = gra[1][k]+gra[k][x]

if dis >= INF:
    print("-1")
else:
    print(dis)