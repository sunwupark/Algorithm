N, K = map(int, input().split())

from collections import deque, defaultdict

queue = deque([N])
visited = defaultdict(int)
visited[N] = 1
MAX = 10**5

while len(queue) != 0:
    cur = queue.popleft()

    if cur == K:
        print(visited[cur]-1)
        break

    for index, mov in enumerate([cur*2, cur-1, cur+1]):
        if mov < 0 or mov > MAX:
            continue
        if visited[mov]:
            continue
    
        if index == 0:
            visited[mov] = visited[cur]
        else:
            visited[mov] = visited[cur] + 1
        
        queue.append(mov)