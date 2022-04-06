# N명의 학생정보가 있다. 학생 정보는 학생의 이름과 학생의 성적으로 구분된다. 
# 각 학생의 이름과 정보가 주어졌을 떄 성적이 낮은 순서대로 학생의 이름을 출력하는 프로그램을 작성하시오
def setting(data):
    return data[1]

n = int(input())
N = []
for i in range(n):
    a, b = input().split()
    N.append((str(a), int(b)))

N = sorted(N, key = setting)
for b in N:
    print(b[0], end = ' ')

##