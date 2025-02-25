from collections import deque
def solution(players, m, k):
    answer = 0
    
    ## 나의 queue에 증설한 컴퓨터와 언제까지인지를 적어놓고 유지를 해야한다. 어차피 들어간대로 먼저 나가니 queue가 맞다
    ## 큐에 증설한 컴퓨터를 유지하고 현재 큐에 있는 증설된 컴퓨터수로 감당이 가능한지 안되면 증설을 몇대나 해야하는지
    
    queue = deque([])
    for time, val in enumerate(players):
        ## 각 시간대에 사용자수에 따라서 증설을 해야하는지 확인한다
        ## m명이 늘어나면 서버 1대
        while len(queue) > 0:
            if queue[0] < time:
                queue.popleft()
            else:
                break
        
        extraServer = val // m
        length = len(queue)
        if length < extraServer:
            for amount in range(extraServer-length):
                queue.append(time+k-1)
                answer+=1
    
    return answer