import sys
input = sys.stdin.readline
N = int(input())
ropes = [-1 for _ in range(N)]
for i in range(N):
    ropes[i] = int(input())

ropes = sorted(ropes, reverse=True)

maxValue = 0
for index in range(N):
    current = ropes[index]*(index+1)
    if maxValue < current:
        maxValue = current

print(maxValue)