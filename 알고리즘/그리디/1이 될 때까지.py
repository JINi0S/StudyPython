# 2018 E 기업 알고리즘 대회
# 어떠한 수 N이 1이 될 떄까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행하려고 한다.
# 단, 두번째 연산은 N이 K로 나누어 떨어질 때만 선택할 수 있다.
# 1. N에서 1을 뺸다.
# 2. N을 K로 나눈다. 
import re


n, k =map(int, input().split())

result = 0
while True:
    if n%k == 0:
        n = n/k
        result += 1
    else:
        n = n - 1
        result += 1
    
    if n == 1:
        break
print(result)