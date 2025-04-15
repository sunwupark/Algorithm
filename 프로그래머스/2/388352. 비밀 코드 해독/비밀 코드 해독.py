def solution(n, q, ans):
    answer = 0
    from itertools import combinations
    numbers = [i for i in range(1, n+1)]
    
    for cur in combinations(numbers, 5):
        curRow = sorted(list(cur))
        correct = True
        for row in range(len(q)):
            count =0 
            for i in range(5):
                if curRow[i] in q[row]:
                    count+=1
            
            if count != ans[row]:
                correct = False
                break
        
        if correct:
            answer+=1

    return answer