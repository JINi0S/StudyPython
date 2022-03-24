from xml.dom.minidom import CharacterData


N = int(input())
x, y = 1, 1

arrow = ['L', 'R', 'U', 'D']
arr = [[0, -1], [0, 1], [-1, 0], [1, 0]]

a = list(input().split())

print(a)
for i in range(len(a)):
    pre_x = x
    pre_y = y 
    for j in range(4):
        if a[i] == arrow[j]:
            x += arr[j][0]
            y += arr[j][1]
   
    if x == 0 or x > N or y == 0 or y > N:
        x = pre_x
        y = pre_y 
        
    else:
        res_x = x
        res_y = y
    print(res_x, res_y)
print("last",res_x, res_y)