N = int(input())
route = []
for _ in range(N):
    route.append(list(map(int, input().split())))

visited = [False for _ in range(N)]
minVal = 10000000

def dfs(start, node, depth, sum):
    global minVal
    if depth == N-1 and route[node][start] != 0:
        minVal = min(minVal, sum + route[node][start])

    for val in range(N):
        if visited[val] == False and route[node][val] != 0:
            visited[val] = True
            dfs(start, val, depth+1, sum+route[node][val])
            visited[val] = False

for i in range(N):
    visited[i] = True
    dfs(i, i,0,0)
    visited[i] = False

print(minVal)