from collections import deque

N, M = map(int, input().split())
maze = []
for i in range(N):
    maze.append(input())

visited = [[False for _ in range(M)] for _ in range(N)]
queue = deque([(0,0,1)])
visited[0][0] = True

x_axis = [-1,0,1,0]
y_axis = [0,1,0,-1]

minVal = N*M

while len(queue) != 0:
    x,y, count = queue.popleft()

    if x == N-1 and y == M-1:
        if count < minVal:
            minVal = count

    for temp_x, temp_y in zip(x_axis, y_axis):
        real_temp_x = x+temp_x
        real_temp_y = y+temp_y

        if (0 <= real_temp_x < N) and (0 <= real_temp_y < M) and maze[real_temp_x][real_temp_y] == "1" and visited[real_temp_x][real_temp_y] == False:
            queue.append((real_temp_x, real_temp_y, count+1))
            visited[real_temp_x][real_temp_y] = True

print(minVal)