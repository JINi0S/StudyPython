n = int(input())
a= []
for i in range(n):
    s = int(input())
    a.append(s)
a.sort(reverse= True)
for i in range(n):
    print(a[i], end= ' ')

# 책 코드
arr=[]
for i in range(n):
    arr.append(int(input()))

arr = sorted(arr, reverse=True)
for i in arr:
    print(i, end=' ')