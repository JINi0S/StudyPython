
# 모든 원소의 값이 0보다 크거나 같다고 가정
arr = [5,3,2,1,0,9,8,4,5,3,6,7,8,1,0,4,2]
# 모든 범위를 포함하는 리스트 선언(모든 값은 0으로 초기화)
count = [0] * (max(arr) + 1)

for i in range(len(arr)):
    count[arr[i]] += 1 # 각 데이터에 해당하는 인덱스의 값 증가

for i in range(len(count)): # 리스트에 기록된 정렬 저보 확인
    for j in range(count[i]):
        print(i, end =  ' ') # 띄어쓰기를 구분으로 등장한 횟수만큼 인덱스 출력