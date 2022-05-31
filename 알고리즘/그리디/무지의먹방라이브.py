# p 316


def solution(food_times, k):
    leng = len(food_times)
    ready = 0
    all_eat = False
    for i in range(k):
        ready = i % leng
        if food_times[ready] != 0:
            food_times[ready] = food_times[ready]-1
        #else:
        #    k = k+1
    
    a = all(food_times,)
    print(food_times,a)
    if a == True:
        return -1
         
    answer = ready
    print(answer)
    return answer

solution([3,1,2], 5)