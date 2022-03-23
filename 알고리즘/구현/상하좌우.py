from xml.dom.minidom import CharacterData


N = map(int,input().split())
x, y = 1, 1

arrow = ['L', 'R', 'U', 'D']
arr = [[0, -1], [0, 1], [-1, 0], [1, 0]]

a = list(input().split())

print(a)
for i in range(len(a)):
    if a[i] == arrow[0]:
        x += arr[0][0]
        y += arr[0][1]
    elif a[i] == arrow[1]:
        x += arr[1][0]
        y += arr[1][1]
    elif a[i] == arrow[2]:
        x += arr[2][0]
        y += arr[2][1]
    elif a[i] == arrow[3]:
        x += arr[3][0]
        y += arr[3][1]
print(x, y)