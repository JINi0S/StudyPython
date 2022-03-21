# 2019 국가 교육기관 코딩 테스트

import readline


N, M = map(int, input().split())
result = 0
for _ in range(N):
    card = list(map(int, input().split()))
    card.sort()
    if result < card[0]:
        result = card[0]
    #min_value = min(Data)
    #result = max(min_value, result)
print(result)