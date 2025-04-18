def solution(k, tangerine):
    answer = 0
    from collections import Counter
    countList = Counter(tangerine)
    setList = list(set(tangerine))
    setList.sort(key=lambda x: -countList[x])
    
    for val in range(len(setList)):
        if k-countList[setList[val]] <= 0:
            return val+1
        k-=countList[setList[val]]
        
    
    return answer