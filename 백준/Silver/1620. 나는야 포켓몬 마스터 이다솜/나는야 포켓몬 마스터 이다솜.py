import sys

N, M = map(int, sys.stdin.readline().strip().split())
mapList = dict()
orderList = [""] * (N+1)
searchList = []
result = []

for i in range(N):
    pokemon = sys.stdin.readline().strip()
    mapList[pokemon] = i+1
    orderList[i+1] = pokemon

for j in range(M):
    value = sys.stdin.readline().strip()

    ## 여기서 숫자인지 문자열인지 판단을 해야한다 어떻게 할 수 있을까?
    ## 가장 앞의 단어가 대문자라면? 가능하다
    if (0 <= ord(value[0]) - 65 < 26) or (0 <= ord(value[-1]) - 65 < 26):
        result.append(str(mapList[value]))
    else:
        result.append(str(orderList[int(value)]))

print("\n".join(result))
