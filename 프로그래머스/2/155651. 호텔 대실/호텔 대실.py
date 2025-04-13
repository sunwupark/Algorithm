from collections import deque
def solution(book_time):
    answer = 0
    ## 분단위로 바꾸기
    for i in range(len(book_time)):
        start, end = book_time[i][0], book_time[i][1]
        hour, minute = start.split(":")
        book_time[i][0] = int(hour)*60 + int(minute)
        
        hour, minute = end.split(":")
        book_time[i][1] = int(hour)*60 + int(minute)+10
    ## 시작시간순으로 나열하기
    book_time.sort(key=lambda x: x[0])
    
    queue = deque()
    for i in range(len(book_time)):
        start = book_time[i][0]
        end = book_time[i][1]
        ## 현재 시간보다 전의 것은 모두 퇴실처리해야한다
        n = len(queue)
        for i in range(n):
            exitTime = queue.popleft()
            if exitTime > start:
                queue.append(exitTime)
        
        queue.append(end)
        answer = max(answer, len(queue))

    return answer