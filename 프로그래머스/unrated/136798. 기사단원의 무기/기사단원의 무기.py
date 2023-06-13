import math

def solution(number, limit, power):
    answer = 0
    for i in range(1, number+1):
        count = 0
        for j in range(1, int(math.sqrt(i))+1):
            if i % j == 0:
                count += 1
                if j != i // j:  # 중복 제거
                    count += 1
        if count > limit:
            count = power
        answer += count
    
    return answer
