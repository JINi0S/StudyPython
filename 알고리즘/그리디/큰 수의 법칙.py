# 단순하게 생각
N, M, K =map(int, input().split())
li = list(map(int, input().split()))
import math
print(li)

li.sort(reverse= True)
print(li)

sum = 0
"""
while M > 0:
    for _ in range(K):
        if(M == 0):
            break
        else:
            sum += li[0]
            M  -= 1 
    if(M == 0):
        break
    else:
        sum += li[1]
        M -= 1
print(sum)"""


# 정답 코드
sum = (K * li[0] + li[1] )  * ( M // ( K + 1))
sum += li[0] * (M % ( K + 1))
print(sum)