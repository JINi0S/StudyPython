a, b = map(int, input().split())
start_x, start_y, look = map(int, input().split())
li = [[0]*a for _ in range(b)]
for i in range(b):
    li[i] = list(map(int, input().split()))

look_x = [-1, 0, 1]
look_y = [-1, 0, 1]




print(li)


## 아직 못 품