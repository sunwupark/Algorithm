def solution(answers):
    answer = []
    
    a = [1,2,3,4,5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    length = len(answers)
    ## answers의 크기에 맞춰서 각자를 만들어야한다
    ## 전체 answers에서 각자의 크기만큼 나눈 몫을 곱하고 나머지까지의 리스트를 만들면 된다
    newA = a*(length//len(a)) + a[:length%len(a)]
    newB = b*(length//len(b)) + b[:length%len(b)]
    newC = c*(length//len(c)) + c[:length%len(c)]
    
    rightList = [0,0,0]
    for valA, valB, valC, ans in zip(newA, newB, newC, answers):
        if valA == ans:
            rightList[0] += 1
        if valB == ans:
            rightList[1] += 1
        if valC == ans:
            rightList[2] += 1
    
    maxValue = max(rightList)
        
    newRightList = []
    for index, i in enumerate(rightList, start=1):
        if i == maxValue:
            newRightList.append(index)
                    
    return newRightList