def solution(n, computers):
    from collections import deque
    def bfs(start):
        queue = deque([start])
        visited[start]=True
        while queue:
            cur = queue.popleft()
            for nx, num in enumerate(computers[cur]):
                if num == 1 and not visited[nx]:
                    visited[nx] = True
                    queue.append(nx)
    
    count = 0
    visited = [False] *(n)
    for i in range(n):
        if not visited[i]:
            bfs(i)
            count +=1
    
    return count
