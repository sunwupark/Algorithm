def solution(k, dungeons):
    answer = -1
    n = len(dungeons)
    visited = [False] * n
    
    def dfs(health, count):
        nonlocal answer
        answer = max(answer, count)
        for i in range(n):
            if health >= dungeons[i][0] and not visited[i]:
                visited[i] = True
                dfs(health-dungeons[i][1], count+1)
                visited[i] = False
    
    dfs(k,0)
    
    return answer