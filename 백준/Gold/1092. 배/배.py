import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
crane = sorted(list(map(int, input().split())), reverse=True)
craneAvailable = [1 for _ in range(N)]
M = int(input())
visited = [0 for _ in range(M)]
boxes = sorted(list(map(int, input().split())), reverse=True)

def solve(M, N):
    for k in range(1, M+1):
        for i in range(sum(craneAvailable)):
            for j in range(M):
                if crane[i] >= boxes[j] and not visited[j]:
                    visited[j] = 1
                    break
                elif j == M-1:
                    craneAvailable[i] = 0
        
        if sum(visited) == M:
            return k
    
        if sum(craneAvailable) == 0:
            return -1
    
    return -1

print(solve(M, N))