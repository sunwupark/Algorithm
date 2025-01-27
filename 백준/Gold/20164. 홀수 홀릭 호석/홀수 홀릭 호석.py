## 일단 수의 length가 3이상이면 3개로 쪼갠다
## 2면 두개로 쪼갠다.
# 이때 나오는 모든 홀수를 기록해서 BFS로 돌린다
## 전에 나왔던 것은 visited로 기록을 하여 가지고 있는데

from collections import deque, defaultdict
import sys
## 큐를 만들고 큐에는 현재 숫자와 홀수가 지금까지 몇개가 나왔는지를 기록한다!
queue = deque([(input(), 0)])
visited = defaultdict(bool)

maxValue = -1
minValue = sys.maxsize

while len(queue) != 0:
    current_value, odd_count = queue.popleft()
    length = len(current_value)

    if length == 1:
        if int(current_value)%2==1:
            odd_count+=1
        maxValue = max(maxValue, odd_count)
        minValue = min(minValue, odd_count)
        continue
    ## 길이가 3이상이면 가능한 모든 방법으로 3가지로 쪼개야한다!. 하지만 기존 순서는 유지를 하기때문에
    ## 이중 for loop으로 돌려도 될듯 하다
    if length >= 3:
        ## 만약 50261이라고 한다면
        ## 1의 위치인 0에서부터 짜르거나
        ## 2의 위치에서 첫번째로 짤라도 된다!
        for i in range(1, length-1):
            ## 두번째 짜르는 위치는 적어도 두번째부터 짤라야한다. 그리고 마지막은 length-1
            for j in range(i+1, length):
                ## 82, 01, 9 를 더한값이 들어간다
                tempSum = int(current_value[:i])+int(current_value[i:j])+int(current_value[j:])
                ## 82, 01, 9에서의 홀수 개수를 찾아본다
                tempOddCount = odd_count
                for val in current_value[:i] + current_value[i:j] + current_value[j:]:
                    if int(val)%2 == 1:
                        tempOddCount +=1

                queue.append((str(tempSum), tempOddCount))
    else:
        tempSum = 0
        tempOddCount = odd_count
        for val in current_value:
            if int(val)%2==1:
                tempOddCount+=1
            tempSum+= int(val)
        queue.append((str(tempSum), tempOddCount))

    
print(minValue, maxValue)

                
                

