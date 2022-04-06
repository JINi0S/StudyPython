arr = [5, 3, 2, 7, 0, 9, 1, 4, 6, 8]

for i in range(1, len(arr)):
    for j in range(i, 0, -1):
        if arr[j] < arr[j -1]:  
            arr[j], arr[j -1] = arr[j-1], arr[j]
        else : break
print(arr)

