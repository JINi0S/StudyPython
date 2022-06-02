# p 316
import numpy as np

def solution(food_times, k):
    leng = len(food_times)
    ready = 0
    all_eat = False
    """
    for i in range(k):
        ready = i % leng
        if food_times[ready] != 0:
            food_times[ready] = food_times[ready]-1
        #else:
        #    k = k+1
    """
    i = 0
    while(i < k):
        ready = i % leng
        if food_times[ready] != 0:
            food_times[ready] = food_times[ready]-1
        else:
            k = k + 1
        print(i, ready, food_times)
        i = i + 1

    a = np.all(food_times==0)
    print(food_times,a)
    if a == True:
        return -1

    while True:
        if food_times[(ready +1) % leng] == 0:
            ready += 1
        else:
            break
    answer = ((ready +1) % leng ) + 1
    
    print(answer)
    return answer

solution([3,1,2], 4)