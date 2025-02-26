from itertools import combinations, product

def solution(dice):
    answer = []
    
    ## 주사위의 반을 A가 가져가고 반을 B가 가져간다음에 거기서 두개를 뽑았을때 A가 B보다 클 확률을 구하는 것이다
    ## A가 어떤것을 뽑았을때 더 클까?
    ## 주사위를 가져갈 수 있는 모든 경우의 수를 for loop로 돌린다음
    ## 그 구성내에서 A의 모든 조합과 B의 모든 조합을 리스트한다음에
    ## 그 리스트에서 A가 B보다 큰 개수 
    
    ## A: [6,7,8,9,10,11,12,13,14]
    ## B: [10,9,8,7,6,5,4,3,2,1]
    
    ## 라고할때 6은 1~5까지 크고 7은 1~6나올때까지 크고 하니 사실 
    ## 6이 어떠한 인덱스보다 큰지까지 계산하면 된다 결국은 승률이 높아야하니 전체는 리스트의 크기끼리 곱한값이 될것이고
    ## A는 asc, B는 desc로 정렬을 하여 A가 더 큰 인덱스를 구한다음 그 크기만큼 빼면 된다
    
    # 자 그럼 먼저 A와 B를 각자 N/2개씩 고르게 해보자
    N = len(dice)
    diceNumList = [i for i in range(1, N+1)]
    
    ### total Number list
    totalNumList = list(combinations(diceNumList, N//2))
    for AList in totalNumList:
        ## A가 type을 가진다면 B는 diceNumList - type을 가져야한다
        realAList = list(AList)
        realBList = list(set(diceNumList)-set(list(AList)))
        
        ## 각자 다이스의 결과 리스트를 만든다
        totalAList = [dice[valA-1] for valA in realAList]
        totalBList = [dice[valB-1] for valB in realBList]
        
        arrA = [sum(combination) for combination in product(*totalAList)]
        arrB = [sum(combination) for combination in product(*totalBList)]
        
        arrA.sort()
        arrB.sort()
        
        lenB = len(arrB)
        indexB = 0  # B 리스트의 포인터
        win_count = 0  # A가 B보다 큰 경우의 수

        for AVal in arrA:
            # B에서 A보다 작은 원소의 개수를 찾기 위해 indexB를 이동
            while indexB < lenB and arrB[indexB] < AVal:
                indexB += 1
            win_count += indexB  # indexB 개수만큼 A가 승리한 경우
        
        answer.append([win_count,AList])
    answer.sort(key=lambda x: -x[0])                    

    return list(answer[0][1])