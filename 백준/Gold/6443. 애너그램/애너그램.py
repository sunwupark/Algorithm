N =int(input())
toPrint = []
for _ in range(N):
    toPrint.append(sorted(input()))

## whatToPrint: 어떤것을 출력해야하는지, 
## node 현재 위치한 노드
from collections import defaultdict
def dfs(length, whatToPrint, depth, str_value):
    # print(whatToPrint, depth, str_value)
    ## 만약 길이가 출력해야하는 숫자라면
    if depth == length:
        print(str_value)
    ##그렇지 않다면 하나씩 더해본다
    else:
        for index, val in enumerate(whatToPrint):
            if not visited[str_value+val]:
                visited[str_value+val] = True
                dfs(length, whatToPrint[:index] + whatToPrint[index+1:], depth+1, str_value+val)
## abc중에서 각 알파벳과 알파벳의 개수를 파악해서 리스트를 만들어야한다

for val in toPrint:
    visited = defaultdict(list)
    dfs(len(val), val, 0, "")