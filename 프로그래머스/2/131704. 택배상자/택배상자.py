def solution(order):
    answer = 0
    from collections import deque
    stack = deque([])
    n = len(order)
    
    for i in range(1,n+1):
        if i == order[answer]:
            answer+=1
            continue
        
        while stack:
            if order[answer] == stack[-1]:
                stack.pop()
                answer+=1
            else:
                break
        
        if i == order[answer]:
            answer+=1
        else:
            stack.append(i)
                
    while stack:
        cur = stack.pop()
        if cur == order[answer]:
            answer+=1
        else:
            break
    
    return answer