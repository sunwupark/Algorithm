def findNums(start, cards, visited):
    result = [cards[start]]
    index = start
    while True:
        index = cards[index]-1
        currentVal = cards[index]
        
        if not visited[index]:
            visited[index] = True
            result.append(currentVal)
        else:
            break
    return result
        
from collections import defaultdict
def solution(cards):
    answer = 0
    visited = defaultdict(bool)
    groupList = []
    for i in range(len(cards)):
        if not visited[i]:
            visited[i] = True
            groupList.append(findNums(i, cards, visited))
    
    groupList.sort(key=lambda x : -len(x))
    # print(groupList)
    if len(groupList) > 1:
        answer = len(groupList[0])*len(groupList[1])
    return answer