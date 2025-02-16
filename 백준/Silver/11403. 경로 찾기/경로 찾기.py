N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(str, input().split())))

## 0->1 , 1->2, 2->0 이 있으면 0->0도 있는것이다
from collections import deque
def bfs(node):
    visited = [False for _ in range(N)]
    queue = deque([node])

    while queue:
        cur = queue.popleft()
        for next in range(N):
            if not visited[next] and graph[cur][next] == "1":
                visited[next] = True
                queue.append(next)
                graph[node][next] = "1"
                graph[cur][next] = "1"

for i in range(N):
    bfs(i)

for i in range(N):
    print(" ".join(graph[i]))
    
    
    

