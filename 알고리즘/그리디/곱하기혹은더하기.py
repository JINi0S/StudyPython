#p312


a = str(input())
res = a[0]
#a = a.replace('0', '')
for i in range(1, len(a)):
    num = int(a[i])
    if a[i] <= 1 or res <=1:
        res += num
    else:
        res *= num
print(res)