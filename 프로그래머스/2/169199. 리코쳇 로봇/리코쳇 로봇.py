from collections import deque
def solution(board):
    answer = 0
    ## 각 방향에서 D가 있으면 D전까지가고 아니면 끝까지 간다
    ## 각 방향에서 끝을 정하는 방법. 현재 위치 [현재위치:X쪽끝] or [0:현재위치] or [현재위치:Y쪽끝] or [0:현제위치]
    
    ## 먼저 R의 위치를 찾는다.
    n = len(board)
    m = len(board[0])
    
    visited = [[False for _ in range(m)] for _ in range(n)]
    
    queue = deque()
    end = (0,0)
    for i in range(n):
        if 'R' in board[i]:
            j = board[i].index('R')
            queue.append((i,j, 0))
            visited[i][j] = True
        if 'G' in board[i]:
            end = (i, board[i].index('G'))
    
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    while queue:
        x,y, count = queue.popleft()
        if x == end[0] and y == end[1]:
            return count
        else:
            for i in range(4):
                nx = x
                ny = y
                while 0 <= nx+dx[i] < n and 0 <= ny+dy[i] < m and board[nx+dx[i]][ny+dy[i]] != 'D':
                    nx+=dx[i]
                    ny+=dy[i]
                
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx,ny,count+1))
    return -1