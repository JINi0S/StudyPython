a = 0.3 + 0.6
print(a)

if a == 0.9:
    print(True)
else:
    print(False)

# 소수점값을 비교하는 작업이 필요한 문제라면 실수 값을 비교하지 

print(round(a, 4))

if round(a, 4) == 0.9:
    print(True)
else: 
    print(False)