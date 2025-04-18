from collections import deque
def solution(elements):
    answer = 0
    visited = set()
    n = len(elements)
    circular = deque(elements)
    for i in range(1,n+1):
        for l in range(n):
            # print(list(circular)[:i])
            visited.add(sum(list(circular)[:i]))
            curr = circular.popleft()
            circular.append(curr)
        
    
    return len(visited)