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


# answer
"""
# 현재 나이트의 위치 입력받기
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

#나이트가 이동할 수 있는 8가지 방향 정의
result = 0
for step in steps:
    #이동하고자 하는 위치 확인
    next_row = row + steps[0]
    next_column = column + step[1]
    # 해당 위치로 이동이 가능하다면 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <=8:
        result += 1
print(result)
"""