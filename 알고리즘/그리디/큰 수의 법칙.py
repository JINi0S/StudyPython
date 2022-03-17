# 입력 조건 : 째 줄에 N(2<= N <=1000)
N, M, K =map(int, input().split())
li = list(map(int, input().split()))
import math
print(li)

li.sort(reverse= True)
print(li)
#mx = math.max(li)
#li.remove(mx)
sum = 0
while M > 0:
    for _ in range(K):
        sum += li[0]
        M  -= 1 
    sum += li[1]
    M -= 1
print(sum)