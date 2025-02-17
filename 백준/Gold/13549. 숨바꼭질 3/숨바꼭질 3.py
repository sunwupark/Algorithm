from collections import deque

N, K = map(int, input().split())
visited = [False for _ in range(max(N,K) * 2 + 1)]

def bfs(node, end):
    queue = deque([(node, 0)])
    visited[node] = True

    while queue:
        curr, time = queue.popleft()

        if curr == end:
            print(time)
            return

        if 0 <= curr * 2 < len(visited) and not visited[curr * 2]:
            visited[curr * 2] = True
            queue.append((curr * 2, time))
        if curr - 1 >= 0 and not visited[curr - 1]:
            visited[curr - 1] = True
            queue.append((curr - 1, time + 1))
        if 0 <= curr + 1 < len(visited) and not visited[curr + 1]:
            visited[curr + 1] = True
            queue.append((curr + 1, time + 1))

bfs(N, K)