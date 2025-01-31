N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [[False, False] for _ in range(N+1)]
for _ in range(M):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for index in range(1, N+1):
    graph[index] = sorted(graph[index], reverse=False)

dfs_result = []
visited[V][0] = True
def dfs(node):
    dfs_result.append(str(node))

    for cur in graph[node]:
        if visited[cur][0] == False:
            visited[cur][0] = True
            dfs(cur)

dfs(V)
print(" ".join(dfs_result))

from collections import deque
queue = deque([V])
visited[V][1] = True
bfs_result = []
while len(queue) != 0:
    node = queue.popleft()
    bfs_result.append(str(node))

    for val in graph[node]:
        if visited[val][1] == False:
            visited[val][1] = True
            queue.append(val)

print(" ".join(bfs_result))