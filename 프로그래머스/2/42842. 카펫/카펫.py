def solution(brown, yellow):
    answer = []
    
    ## yellow가 x*y라면 brown은 x+2*y+2이다 
    ## 2x+4 + 2y
    
    ## 즉 brown = 2x+2y+4
    ## yello = x*y
    ## return [x+2, y+2] 인것이다
    ## (x, brown - 2x - 4 / 2)
    for x in range(1, yellow+1):
        y = (brown - 2*x - 4)/2
        if x*y == yellow:
            if x > y:
                return [x+2, y+2]
            else:
                return [y+2, x+2]
    
    return answer