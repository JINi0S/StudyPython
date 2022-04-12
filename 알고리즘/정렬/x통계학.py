"""2108
문제
수를 처리하는 것은 통계학에서 상당히 중요한 일이다. 통계학에서 N개의 수를 대표하는 기본 통계값에는 다음과 같은 것들이 있다. 단, N은 홀수라고 가정하자.

산술평균 : N개의 수들의 합을 N으로 나눈 값
중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
최빈값 : N개의 수들 중 가장 많이 나타나는 값
범위 : N개의 수들 중 최댓값과 최솟값의 차이
N개의 수가 주어졌을 때, 네 가지 기본 통계값을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 수의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 단, N은 홀수이다. 그 다음 N개의 줄에는 정수들이 주어진다. 입력되는 정수의 절댓값은 4,000을 넘지 않는다.

출력
첫째 줄에는 산술평균을 출력한다. 소수점 이하 첫째 자리에서 반올림한 값을 출력한다.
둘째 줄에는 중앙값을 출력한다.
셋째 줄에는 최빈값을 출력한다. 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.
넷째 줄에는 범위를 출력한다"""
import sys
a = []
i_len = 1
long_len = 1
long_li=[]
n = int(input())
for _ in range(n):
    i = int(sys.stdin.readline().rstrip())
    a.append(i)
#su = sum(a)
#print(round(su/n))

avg = (sum(a) / n)

if avg > 0:
    if avg%1 >= 0.5:
        avg = int(avg) + 1
    else: 
        avg = int(avg)
else:
    if avg %1 >= 0.5:
        avg = int(avg)
    else:
        avg = int(avg) - 1

print(avg)

a.sort()
print(a[(n//2)])

data = dict()
for i in range(n):
    if str(a[i]) in data:
        data[str(a[i])] += 1 
    else:
        data[str(a[i])] = 1 

data = sorted(data.items(),key=lambda x:x[1], reverse=True)
#print(data)

count = 0

if n == 1: 
    print(a[0])
else:
    if data[0][1] == data[-1][1]:
        print(a[1])
    else:
        for i in range(len(data)-1): 
            if data[i][1]>data[i+1][1]:
                count = i 
                break
            

        if count == 0: #인덱스 0이 최빈값, 최빈값이 하나뿐이란소리
            print(int(data[0][0]))
        else: # count > 0: # 0~count이 모두 최빈값이란 소리
            """li=[]
            for i in range(count+1):
                li.append(int(data[i][0]))
            li.sort()"""
            print(int(data[1][0]))

print(abs(a[0]-a[-1]))
