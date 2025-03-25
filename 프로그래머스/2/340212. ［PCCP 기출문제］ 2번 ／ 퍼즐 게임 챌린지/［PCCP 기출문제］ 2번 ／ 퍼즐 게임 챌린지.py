def solution(diffs, times, limit):
    answer = 1
    N = len(diffs)
    lowLevel = 1
    highLevel = max(diffs)
    
    while lowLevel <= highLevel:
        curLevel = (lowLevel+highLevel)//2
        totalTime = 0
        for index in range(N):
            time_cur = times[index]
            diff = diffs[index]
            if diff <= curLevel:
                totalTime+=time_cur
            else:
                ##한번 틀리면 이번거랑 저번거를 다시 풀어야한다
                if index > 0: 
                    totalTime+=(time_cur+times[index-1])*(diff-curLevel)+time_cur
                else:
                    totalTime+=time_cur*(diff-curLevel)+time_cur
        
        if totalTime <= limit:
            answer = curLevel
            highLevel = curLevel-1
        else:
            lowLevel=curLevel+1
        
    return answer