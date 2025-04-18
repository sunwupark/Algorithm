def wubak(k):
    result = [(0, k)]
    count = 0 
    while k != 1:
        if k%2==0:
            k/=2
        else:
            k=k*3+1
        count+=1
        result.append((count, k))
    return result, count

def solution(k, ranges):
    answer = []
    wubakList, n = wubak(k)
    wubakArea = []
    for i in range(n):
        wubakArea.append((wubakList[i][1]+wubakList[i+1][1])/2)
    # print(wubakList)
    # print(wubakArea)

    for x,y in ranges:
        start = x
        end = n+y
        if start > end:
            answer.append(-1)
        elif start == end:
            answer.append(0)
        else:
            answer.append(sum(wubakArea[start:end]))

    return answer