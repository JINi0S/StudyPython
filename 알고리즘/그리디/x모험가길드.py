import re
from traceback import print_tb


n = int(input())
a=list(map(int, input().split()))
a.sort(reverse=True)
print(a)
result = 0

#a[a[0]-1]
if a[0] == 1:
    print(n)
else:
    i = 0
    while i < n:
        # a[0]의 값이 a[0]보다 큰가.
        if a[a[i-1]] < a[i]:
            result += 1

        print(i,result)    
        i += a[i]
        

print("res", result)