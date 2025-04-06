from collections import deque

def solution(plans):
    answer = []
    stack = deque([])
    for i in range(len(plans)):
        hour, minute = map(int, plans[i][1].split(":"))
        plans[i][1] = hour*60 + minute

    plans.sort(key=lambda x: x[1])
    
    curTime = 0
    for index in range(len(plans)):
        while stack:
            types, playtime = stack.pop()
            if curTime + playtime > plans[index][1]:
                stack.append([types, playtime - (plans[index][1] - curTime)])
                break
            else:
                answer.append(types)
                curTime = curTime + playtime
        
        curTime = plans[index][1]
        stack.append([plans[index][0], int(plans[index][2])])
    
    for i in range(len(stack)):
        answer.append(stack.pop()[0])
    
    return answer