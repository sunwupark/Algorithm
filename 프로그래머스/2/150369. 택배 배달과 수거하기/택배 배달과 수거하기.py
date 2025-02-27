def solution(cap, n, deliveries, pickups):
    ## 뒤에서 부터 하나씩 인덱스를 앞으로 가면서 
    ## [2,1,3,0,1]
    ## [0,4,0,3,0]
    ## cap만큼 빼고 while문으로 합이 그것보다 크면 더해준다
    
    deliveries = deliveries[::-1]
    pickups = pickups[::-1]
    
    delSum = 0
    pickSum = 0
    
    answer = 0
    
    for i in range(n):
        delSum += deliveries[i]
        pickSum += pickups[i]
        
        while delSum > 0 or pickSum > 0:
            delSum -= cap
            pickSum -= cap
            answer+= (n-i)*2
    
    return answer