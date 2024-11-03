import sys

N, M = map(int, sys.stdin.readline().strip().split())
sumOfStrings = []
inputList = []
count = 0

for _ in range(N):
    sumOfStrings.append(sys.stdin.readline().strip())

for i in range(M):
    inputList.append(sys.stdin.readline().strip())

    if inputList[i] in sumOfStrings:
        count+=1

print(count)