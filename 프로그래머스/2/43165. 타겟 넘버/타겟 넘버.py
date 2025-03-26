from collections import deque

def solution(numbers, target):
    answer = 0
    
    def bfs(N, target):
        nonlocal answer
        queue = deque([(0,0)])
        while queue:
            index, total = queue.popleft()
            if index == N:
                if total == target:
                    answer+=1
            else:
                queue.append((index+1, total+numbers[index]))
                queue.append((index+1, total-numbers[index]))
    
    bfs(len(numbers), target)

    return answer