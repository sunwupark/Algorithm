def solution(want, number, discount):
    answer = 0
    
    ## discount초반 10개에 대해서 counter사용
    ## 되면 +1, 
    ## index넘어가기
    
    from collections import Counter
    currentList = Counter(discount[:10])
    
    myDict = {}
    for k in range(len(want)):
        myDict[want[k]] = number[k]
    
    for i in range(len(discount)-9):
        buy = True
        # print(i, currentList, answer)
        for key, vals in myDict.items():
            if currentList[key] < vals:
                buy = False
                break
        if buy:
            answer+=1
        
        if i+10 >= len(discount):
            break
        
        if currentList[discount[i]] > 1:
            currentList[discount[i]] -=1
        else:
            del currentList[discount[i]]
        if not currentList.get(discount[i+10]):
            currentList[discount[i+10]] = 1
        else:
            currentList[discount[i+10]] += 1
        
    return answer