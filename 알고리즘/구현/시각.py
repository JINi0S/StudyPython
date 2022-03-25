num = int(input())
res = 0
for i in range(num+1):
    if i % 10==3:
        res +=3600
    else: 
        for j in range(60):
            if j % 10==3 or 30 <= j < 40:
                res += 60
            else:
                for m in range(60):
                    if(m % 10==3 or 30 <= m <40): 
                        res += 1
print(res)