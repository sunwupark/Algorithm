def solution(numbers):
    from collections import defaultdict
    from itertools import permutations
    sosu = defaultdict(bool)
    
    strList = []
    for val in numbers:
        strList.append(val)
    
    values = []
    # permutations
    for i in range(1,len(strList)+1):
        # values.append(permutations(strList, i))
        for value in set(permutations(strList, i)):
            temp = ""
            for str in value:
                temp+=str
            values.append(int(temp))
        
    maxValue = max(values)
    ## 최대 값 까지 아리스토 체를 한다
    
    sosu[0] = True
    sosu[1] = True
    for i in range(2, maxValue+1):
        if not sosu[i]:
            for val in range(i+i, maxValue+1, i):
                sosu[val] = True
    
    count =0 
    for last in set(values):
        if not sosu[last]:
            count+=1
    
    return count