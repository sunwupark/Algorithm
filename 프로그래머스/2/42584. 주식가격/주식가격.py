def solution(prices):
    n = len(prices)
    answer = [0]*n
    
    for curr in range(n-1):
        for comp in range(curr+1, n):
            if prices[comp] < prices[curr]:
                answer[curr]+=1
                break
            answer[curr]+=1
    
    return answer