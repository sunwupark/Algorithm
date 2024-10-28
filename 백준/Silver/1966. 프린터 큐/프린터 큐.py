import sys
from collections import deque

## Input받기
## 큐에 저장한다
## 큐에 저장할때 최대값을 저장한다
## 큐의 첫번째값이 최대값이랑 같다면 출력 아니라면 넘긴다

T = int(sys.stdin.readline())
result = []

for _ in range(T):
    N, index = map(int, input().split())
    queue = deque(list(map(int, input().split())))
    count = 0
    cursor = index

    while(len(queue) > 0):
        maxValue = max(queue)
        currentValue = queue.popleft()
        if(currentValue < maxValue):
            queue.append(currentValue)
        elif (currentValue >= maxValue and cursor == 0):
            result.append(str(count+1))
            break
        else:
            count +=1

        if cursor == 0:
            cursor = len(queue) -1
        else:
            cursor -= 1

print("\n".join(result))
