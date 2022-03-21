# 2019 국가 교육기관 코딩 테스트

import readline


N, M = map(int, input().split())
max = 0
for _ in range(N):
    card = list(map(int, input().split()))
    card.sort()
    if max < card[0]:
        max = card[0]

print(max)