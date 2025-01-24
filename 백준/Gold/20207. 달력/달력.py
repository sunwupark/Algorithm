# 처음 넣을때 어디의 일정이 진행중인지 확인한다
# 일정이 진행중이라면 일이 진행중이지 않은 가장 상단에 넣는다
# 시작이 같다면 길이가 긴것 부터 실행을 해야한다!

from collections import defaultdict

## 입력받고 각 시작시간을 기준으로 정렬한다. 또한 시작 시간내의 리스트는 걸리는 시간을 DESC로 정렬한다
startDate = defaultdict(list)
N = int(input())
for _ in range(N):
    date, length = map(int, input().split())
    startDate[date].append(length)
    startDate[date].sort(reverse=True)
sorted_by_key = sorted(startDate.items())

## list 가지고 있다가 들어가 있는 종료시간이 현재 내가 들어가는 시간보다 작으면 교체한다
timetable = defaultdict(int)
## 시작시간이 빠른 것 부터 돌아가면서 리스트에 넣는다
maxPage = 0
pageStart = -1
totalResult = 0
for val in sorted_by_key:
    startTime = val[0]
    endTimeList = val[1]

    ## 페이지의 시작 정해두기
    if pageStart == -1:
        pageStart = startTime

    ## 만약 이번 시작이 한칸이상 떨어져 있다면
    ## 가장 마지막의 endTime을 구한다
    lastEndTime = 0
    count = 0
    for time in timetable.keys():
        if timetable[time] < startTime and startTime - timetable[time] >= 2:
            if timetable[time] > lastEndTime:
                lastEndTime = timetable[time]
            count+=1
    
    ## 타임테이블을 클리어하고 다시 최대 페이지를 1로 수정한다
    ## 또한 전 페이지의 최대값의 코팅지 면적을 미리 구해두고 pageStart도 이번 start로 변경한다!
    if count == len(timetable.keys()):
        totalResult += (lastEndTime - pageStart + 1)*maxPage
        timetable.clear()
        maxPage = 0
        pageStart = startTime

    ## endTime을 통해서 타임테이블을 업데이트 한다
    for endTime in endTimeList:
        changed = False
        for time in timetable.keys():
            if timetable[time] < startTime:
                timetable[time] = endTime
                changed=True
                break
        
        if not changed:
            maxPage +=1
            timetable[maxPage] = endTime
    
if len(timetable) > 0:
    lastEndTime = 0
    for time in timetable.keys():
        if timetable[time] > lastEndTime:
            lastEndTime = timetable[time]
    
    totalResult += (lastEndTime - pageStart + 1) * maxPage

print(totalResult)
       