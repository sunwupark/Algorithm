def solution(x, y, n):
    answer = -1
    from collections import deque, defaultdict
    def bfs(x,y,n):
        nonlocal answer
        queue = deque([(x, 0)])
        visited = defaultdict(bool)
        visited[x] = True
        
        while queue:
            cur, count = queue.popleft()
            
            if cur == y:
                answer = count
                return
            
            if cur*3 <= y and not visited[cur*3]:
                visited[cur*3] = True
                queue.append((cur*3, count+1))
            if cur*2 <= y and not visited[cur*2]:
                visited[cur*2] = True
                queue.append((cur*2,count+1))
            if cur+n <= y and not visited[cur+n]:
                visited[cur+n] = True
                queue.append((cur+n, count+1))
            
    bfs(x,y,n)
    return answer