N = int(input())
pool = []
for _ in range(N):
    pool.append(list(map(int, input().split())))

from copy import deepcopy

while N != 1:
    pooling = []

    for x in range(0, N, 2):
        tempList = []
        for y in range(0, N, 2):
            valList = sorted([pool[x][y], pool[x][y+1], pool[x+1][y], pool[x+1][y+1]], reverse=True)
            tempList.append(valList[1])
        
        pooling.append(tempList)
    
    N = N//2
    pool = deepcopy(pooling)
    # print("N: ", N)
print(pool[0][0])



