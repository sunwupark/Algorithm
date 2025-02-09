def dfs(node, sumVal):
    global maxVal

    if node == 11:
        maxVal = max(maxVal, sumVal)
        return
    
    else:
        ## 여기서 depth로 정하는것이 아니라 자신한테 점수가 주어진 어떠한 포지션이든 가봐야한다
        for position in range(11):
            if stats[node][position] != 0 and visited[position] == False:
                visited[position] = True
                dfs(node+1, sumVal+stats[node][position])
                visited[position] = False

N =int(input())
for _ in range(N):
    stats = []
    for i in range(11):
        stats.append(list(map(int, input().split())))

    visited = [False] * 11
    maxVal = 0  
    dfs(0, 0)
    print(maxVal)