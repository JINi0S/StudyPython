from xml.dom.minidom import CharacterData


N = map(int,input().split())
x, y = 1, 1

arrow = ['L', 'R', 'U', 'D']
arr = [[0, -1], [0, 1], [-1, 0], [1, 0]]

a = list(input().split())

print(a)
for i in range(len(a)):
    pre_x = x
    pre_y = y 
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
   
    if x == 0 or x == len(a)+1 or y == 0 or y == len(a) + 1:
        x = pre_x
        y = pre_y 
        
    else:
        res_x = x
        res_y = y
    print(res_x, res_y)
print("last",res_x, res_y)