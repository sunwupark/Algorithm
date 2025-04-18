from collections import Counter
def solution(topping):
    answer = 0
    countDict = Counter(topping)
    bro = len(countDict)
    myDict = {}
    my = 0
    
    for i in range(len(topping)):
        if not myDict.get(topping[i]):
            myDict[topping[i]] = 1
            my+=1
        
        if countDict[topping[i]] == 1:
            del countDict[topping[i]]
            bro -= 1
        else:
            countDict[topping[i]] -=1
        
        if my==bro:
            answer+=1    
    
    return answer