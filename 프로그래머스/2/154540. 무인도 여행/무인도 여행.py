import sys
sys.setrecursionlimit(10**6)

def solution(maps):
    answer = []
    n = len(maps)
    m = len(maps[0])
    visited = [[False for _ in range(m)] for _ in range(n)]
    
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    def dfs(x,y):
        nonlocal n,m,total
        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maps[nx][ny] != 'X':
                visited[nx][ny] = True
                total.append(int(maps[nx][ny]))
                dfs(nx,ny)
                
    for i in range(n):
        for j in range(m):
            if maps[i][j] != 'X' and not visited[i][j]:
                visited[i][j] = True
                total = [int(maps[i][j])]
                dfs(i,j)
                answer.append(sum(total))
                
    if len(answer)>0:
        return sorted(answer)
    else:
        return [-1]
    return answer