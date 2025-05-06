def solution(orders, course):
    answer = []
    
    from itertools import combinations
    from collections import defaultdict
    
    visited = [defaultdict(int) for _ in range(max(course)+1)]
    
    for order in orders:
        orderList = []
        for char in order:
            orderList.append(char)
        
        for num in course:
            for combination in combinations(orderList, num):
                cur = tuple(sorted(combination))
                if not visited[num].get(cur):
                    visited[num][cur]=1
                else:
                    visited[num][cur]+=1
    
    for cours in course:
        cur = sorted(visited[cours].items(), key=lambda x: -x[1])
        if cur:
            maxVal = cur[0][1]
            if maxVal < 2:
                continue
                
            for element in cur:
                if element[1] == maxVal:
                    answer.append("".join(list(element[0])))
    
    return sorted(answer)