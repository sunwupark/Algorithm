def solution(n, left, right):
    answer = []
    
    ## 1 2 3
    ## 2 2 3 
    ## 3 3 3
    ## 1 2 3 2 2 3 3 3 3
    
    ## 1 2 3 4
    ## 2 2 3 4 
    ## 3 3 3 4
    ## 4 4 4 4
    
    ## 2 ~ 5라는것은
    ## 2/3 = 0..2
    ## 5/3 = 1..2
    
    ## 먼저 몇번쨰 Row가 필요한지 알아야한다
    ## 7 ~ 14 라는 것은 결국 
    ## 7/4 => 1.. 3 이 나올텐데 => 1번째 Row의 3번째 부터 14/4=3..2 3번째 Row의 2번쨰까지 필요하다는거다. 
    
    startRow = left//n
    startCol = left%n
    endRow = right//n
    endCol = right - left
    
    for i in range(startRow, endRow+1):
        answer.extend([(i+1) for _ in range(i+1)] + [(l+1) for l in range(i+1, n)])
    
    return answer[startCol:startCol+endCol+1]