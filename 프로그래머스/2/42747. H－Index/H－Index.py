def solution(citations):
    answer = 0
    
    citations.sort()
    n = len(citations)
    ## [0, 1, 3, 5, 6]
    for i in range(n):
        h = min(citations[i], n-i)
        answer = max(answer, h)
        
    return answer