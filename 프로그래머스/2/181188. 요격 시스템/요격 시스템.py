def solution(targets):
    answer = 0
    
    targets.sort(key=lambda x: x[0])
    
    N = len(targets)
    index = 0
    left = 0
    right = 100000000
    ## 만약 시작의 최대값과 끝의 최소값이 둘다 안에 존재하면 괜찮다
    ## 만약 right < left라면 끝이다
    while index < N:
        left = max(left, targets[index][0])
        right = min(right, targets[index][1])
        if left >= right:
            answer+=1
            left = targets[index][0]
            right = targets[index][1]

        index+=1
            
    return answer+1