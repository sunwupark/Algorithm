def solution(rows, columns, queries):
    answer = []
    maps = [[i + j * columns + 1 for i in range(columns)] for j in range(rows)]
    
    for query in queries:
        x1, y1, x2, y2 = [i-1 for i in query]  # 0-based index 변환
        temp = []
        
        # 회전 대상 좌표 및 값 수집
        # 상단
        for y in range(y1, y2):
            temp.append((x1, y))
        # 우측
        for x in range(x1, x2):
            temp.append((x, y2))
        # 하단
        for y in range(y2, y1, -1):
            temp.append((x2, y))
        # 좌측
        for x in range(x2, x1, -1):
            temp.append((x, y1))
        
        # 회전시키기: 한 칸씩 오른쪽으로 밀기
        values = [maps[x][y] for x, y in temp]
        rotated = [values[-1]] + values[:-1]
        for (x, y), val in zip(temp, rotated):
            maps[x][y] = val
        
        # for i in range(rows):
        #     print(maps[i])
        
        answer.append(min(rotated))
            
    return answer