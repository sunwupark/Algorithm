def solution(storey):
    answer = 0
    storey = str(storey)
    
    while storey:
        curr = int(storey[-1])
        print(storey, curr)
        if curr <= 4:
            answer += curr
        elif curr > 5:
            answer +=  10 - curr
            storey = str(int(storey[:-1] + "0") + 10)
        else:
            if len(storey) > 1 and int(storey[-2]) >= 5:
                answer +=  10 - curr
                storey = storey[:-2] + str(int(storey[-2])+1) + "0"
            elif len(storey) > 1 and int(storey[-2]) < 5:
                answer += curr
            else:
                answer+=curr
        storey=storey[:-1]
        
    return answer