a = 0.3 + 0.6
print(a)

if a == 0.9:
    print(True)
else:
    print(False)

# 소수점값을 비교하는 작업이 필요한 문제라면 실수 값을 비교하지 못해서 원하는 결과를 얻지 못할 수 있다. 이럴 때는 round()함수를 이용한다.
# round() 함수를 호출할 때는 인자를 넣는데 첫 번째 인자는 실수형 데이터이고, 두 번째 인자는(반올림하고자하는 위치 -1) 이다. 
# 예를 들어 123.456 을 소수점 셋째 자리에서 반올림하려면 round(123.456, 2)라고 작성하며 결과는 123.46이다. 
# 두번째 인자 없이 인자를 하나만 넣을 때는 소수점 첫째 자리에서 반올림한다.

# round() 함수를 이용해서 소수점 특정 자리수에서 반올림하는 예시이다. 
# 흔히 코딩테스트 문제에서는 실수형 데이터를 비교할 때 소수점 다섯 번째 자리에서 반올림한 결과가 같으면 정답으로 인정하는 식으로 처리한다.

print(round(a, 4))

if round(a, 4) == 0.9:
    print(True)
else: 
    print(False)
