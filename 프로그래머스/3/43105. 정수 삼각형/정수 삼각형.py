def solution(triangle):
    answer = 0
    ## 가장 밑의 층에서 최대값을 얻기 위해서는 N-1층까지의 최대값에서 더해야하는 것이다.
    ## dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + triangle[i][j]
    
    ## 한번 for loop으로 해보자
    N = len(triangle)
    dp = [[0 for _ in range(N)] for _ in range(N)]
    dp[0][0] = triangle[0][0]
    
    for i in range(1, N):
        for j in range(len(triangle[i])):
            if j > 0:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + triangle[i][j]
            else:
                dp[i][j] = dp[i-1][j] + triangle[i][j]
        
    return max(dp[N-1])