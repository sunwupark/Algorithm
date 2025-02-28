import math

def calculate(carNumber, outTime, inTime):
    curHour = int(outTime.split(":")[0])
    curMin = int(outTime.split(":")[1])

    inHour = int(inTime.split(":")[0])
    inMin = int(inTime.split(":")[1])

    ## 14:00 11:30
    totalMinutes = 0
    if curMin - inMin < 0:
        curHour -= 1
        totalMinutes += curMin + 60 - inMin
    else:
        totalMinutes += curMin-inMin

    totalMinutes += (curHour - inHour)*60
    
    return totalMinutes

def solution(fees, records):
    from collections import defaultdict
    answer = defaultdict(int)
    ## defaultdict에 저장하고 있으면 출차 없으면 입차인것이다
    graph = defaultdict(int)
    totalList = 0
    
    for record in records:
        time, number, types = record.split()
        if types == "IN":
            graph[number]=time
        else:
            totalMinutes = calculate(number, time, graph[number])
            answer[number] += totalMinutes
            del(graph[number])
    
    for key, value in graph.items():
        totalMinutes = calculate(key, "23:59", graph[key])
        answer[key] += totalMinutes
    
    result = []
    for key, value in sorted(answer.items()):
        totalFee = fees[1]
        if value > fees[0]:
            totalFee = fees[1] + math.ceil((value-fees[0]) / fees[2])*fees[3]
        result.append(totalFee)
        
    print(result)
    
    return result