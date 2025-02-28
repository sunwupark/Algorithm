from collections import deque
def solution(queue1, queue2):
    answer = -1
    
    ## 전체합
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    total = sum1+sum2
    
    if max(queue1 + queue2) > total / 2 or total % 2 != 0:
        return -1
    
    totalLength = len(queue1)+len(queue2)
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    
    count = 0
    ## 큰쪽에서 작은쪽으로 넘어간다
    for _ in range(totalLength*2):
        if sum1 > sum2:
            val = queue1.popleft()
            sum1 -= val
            queue2.append(val)
            sum2 += val
            count+=1
        elif sum1 < sum2:
            val = queue2.popleft()
            sum2 -= val
            queue1.append(val)
            sum1 += val
            count+=1
        else:
            return count
        
    return answer