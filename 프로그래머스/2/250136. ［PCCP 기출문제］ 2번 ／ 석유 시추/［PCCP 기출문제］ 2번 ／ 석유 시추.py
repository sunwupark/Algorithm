from collections import defaultdict, deque

def solution(land):
    answer = 0
    n = len(land)
    m = len(land[0])
    
    visited = [[False] * m for _ in range(n)]
    oilPerList = {}
    toMove = [(0,1), (1,0), (-1,0), (0,-1)]
    
    def bfs(row, col, group):
        queue = deque([(row, col)])
        visited[row][col] = True
        totalList = [(row, col)]
        
        while queue:
            curX, curY = queue.popleft()
            for dx, dy in toMove:
                nextX, nextY = curX + dx, curY + dy
                if 0 <= nextX < n and 0 <= nextY < m and not visited[nextX][nextY] and land[nextX][nextY] == 1:
                    visited[nextX][nextY] = True
                    queue.append((nextX, nextY))
                    totalList.append((nextX, nextY))
        
        length = len(totalList)
        for x, y in totalList:
            oilPerList[(x, y)] = (group, length)
        return length
    
    group = 0
    groupSizes = defaultdict(int)
    
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and not visited[i][j]:
                length = bfs(i, j, group)
                groupSizes[group] = length
                group += 1

    for j in range(m):
        groupSet = set()  # 중복을 피하기 위해 set 사용
        temp = 0
        for i in range(n):
            if (i, j) in oilPerList:
                group, length = oilPerList[(i, j)]
                if group not in groupSet:
                    groupSet.add(group)
                    temp += groupSizes[group]
        answer = max(answer, temp)
    
    return answer