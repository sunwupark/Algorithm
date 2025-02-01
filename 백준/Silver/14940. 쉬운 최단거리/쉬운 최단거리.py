N, M = map(int, input().split())  # Read N and M
grid = []  # Initialize an empty list
target = (0,0)
for i in range(N):
    line = list(map(int, input().split()))
    grid.append(line)  # Read each row and convert to a list of integers
    if 2 in line:
        target = (i, line.index(2), 0)

visited = [[False for _ in range(M)] for i in range(N)]
from collections import deque
from copy import deepcopy
queue = deque([target])
visited[target[0]][target[1]] =True
distanceGrid = deepcopy(grid)

x_axis = [-1, 0, 1, 0]
y_axis = [0, 1, 0, -1]
while len(queue) != 0:
    x,y, val = queue.popleft()
    distanceGrid[x][y] = val

    for a,b in zip(x_axis, y_axis):
        if x+a >= 0 and x+a < N and y+b >= 0 and y+b < M:
            if visited[x+a][y+b] == False and grid[x+a][y+b] == 1:
                queue.append((x+a, y+b, val+1))
                visited[x+a][y+b] = True

for i in range(N):
    for j in range(M):
        if visited[i][j] == False and grid[i][j] == 1:
            distanceGrid[i][j] = -1

for i in range(N):
    print(" ".join(list(map(str, distanceGrid[i]))))