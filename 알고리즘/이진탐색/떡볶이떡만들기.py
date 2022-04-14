n, m = map(int,input().split())
height = list(map(int,input().split()))

height.sort()
max = height[-1]

def bina(target, start, end):
 
    sum = 0
    mid = (start + end)//2
    for i in height:
        k = i - mid
        if k>=0:
            sum += k
    if sum == target:
        return mid
    elif sum < target:
        return bina(target, start, mid - 1)
    else:
        if start > end:
                return mid
        return bina(target, mid+1, end)

res = bina(m, 0, max)
print(res)