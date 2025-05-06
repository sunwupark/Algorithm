def solution(n):
    answer = [[1]*i for i in range(1, n+1)]
    
    target = 0
    for i in range(1, n+1):
        target += i
    
    ## 1
    ## 2 15
    ## 3 16 14
    ## 4 17 21 13
    ## 5 18 19 20 12
    ## 6  7  8  9 10 11
    
    value = 1
    x = -1
    y = 0
    length = n
    while value <= target:
        for _ in range(length):
            x += 1
            answer[x][y] = value
            value +=1
        
        for _ in range(length-1):
            y += 1
            answer[x][y] = value
            value +=1
        
        for _ in range(length-2):
            y -= 1
            x -= 1
            answer[x][y] = value
            value +=1
            
        length-=3
    
    # answer[x][y]
    
    real = []
    for i in answer:
        real.extend(i)
        # print(i)
    
    return real