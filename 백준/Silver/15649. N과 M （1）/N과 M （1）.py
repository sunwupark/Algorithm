N, M = map(int, input().split())

def dfs(inputList: str, count: int):
    if count == M:
        print(inputList)
    for i in range(1, N+1):
        if str(i) not in inputList:
            dfs(inputList + str(i) + " ", count+1)

dfs("", 0)