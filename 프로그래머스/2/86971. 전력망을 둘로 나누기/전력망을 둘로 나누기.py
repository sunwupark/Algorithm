from collections import deque
import math
def solution(n, wires):
    answer = math.inf
    
    for i in range(n-1):
        graph = {k: set() for k in range(1, n+1)}
        for j in range(n-1):
            if i == j:
                continue
            a = wires[j][0]
            b = wires[j][1]
            graph[a].add(b)
            graph[b].add(a)
        
        queue = deque([1])
        visited = [False] * (n+1)
        visited[1] = True
        count = 1
        while queue:
            node = queue.popleft()
            for value in graph[node]:
                if not visited[value]:
                    visited[value] = True
                    queue.append(value)
                    count += 1
        
        answer = min(answer, abs(n - count*2))
                    
    return answer