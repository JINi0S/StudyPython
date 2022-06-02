# p321
m = str(input())
l = int(len(m)/2)
left, right = 0, 0
for i in range(l):
    left += int(m[i])
    right += int(m[i+l])
if left == right:
    print("LUCKY")
else:
    print("READY")
