wh = str(input())
res = 0
if 'a' in wh or 'b' in wh or'j' in wh or 'h'in wh:
    print("수평 1번 가능")
    if '1' in wh or '8' in wh:
        print("수직 1번 가능")
        res += 1
    else :
        print("수직 2번 가능")
        res += 2
else:
    print("수평 2번 가능")
    if '1' in wh or '8' in wh:
        print("수직 1번 가능")
        res += 2
    else:
        print("수직 2번 가능")
        res += 4
print(res*2)


