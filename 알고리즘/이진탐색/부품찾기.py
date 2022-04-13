import sys
m= int(input())

m_array = list(map(int, input().split()))

n= int(input())
n_array = list(map(int, input().split()))

m_array.sort()

def binary_s(array, target, start, end):
    if start>end:
        return None
    mid = (start + end) //2
    if target == array[mid]:
        return mid
    elif target> array[mid]:
        return binary_s(array, target, mid+1, end)
    else:
        return binary_s(array, target, start, mid-1)

for i in n_array:
    res = binary_s(m_array, i, 0, m-1) 

    if res == None:
        print("no")
    else:
        print("yes")