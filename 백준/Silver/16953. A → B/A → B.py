import sys
from collections import deque

a,b = map(int, sys.stdin.readline().strip().split())


queue = deque([(a,0)])
minValue = 99999999999
while queue:
    value, count = queue.popleft()
    if value == b and minValue > count+1:
        minValue = count +1

    if value*10+1 <= b:
        queue.append(((value*10+1), count+1))
    if value*2 <= b:
        queue.append((value*2, count+1))

if minValue == 99999999999:
    print(-1)
else:
    print(minValue)