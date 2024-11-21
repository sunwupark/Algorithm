import sys
input = sys.stdin.readline
N = int(input())

mList = sorted(list(map(int, input().split())), reverse=False)

maxValue = mList[N-1]

## 홀수인 경우
if N%2 == 1:
    N-=1
for i in range((N)//2):
    current = mList[i] + mList[N-i-1]
    if maxValue < current:
        maxValue = current

print(maxValue)