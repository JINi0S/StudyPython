from re import X


n, m = map(int, input().split())
a = list(map(int, input().split()))
#n * m /2 - X
a.sort()
repeat = 1
minus = 0
for i in range(n-1):
    if a[i] == a[i+1]:
        repeat += 1
    else:
        if repeat > 1:
            print(repeat)
            minus += (repeat*(repeat-1) / 2)
        repeat = 1
    if i == n-2:
        if repeat > 1:
            print(repeat)
            minus += (repeat*(repeat-1) / 2)

            
result = (n * (n-1) / 2) - minus
print(int(result), minus)