## P X P 인 경우
## P X
## X P 인 경우
## 맨해튼 거리가 2초과인 경우
## 즉 안되는 경우를 생각해보자
## 맨해튼 거리가 1인 경우
## 맨해튼 거리가 2인데 가는 길목에 O가 있어서 도착 가능한 경우
        

def solution(places):
    answer = []
    ## 제대로 지켜지고 있지 않은 경우
    ## P와 P 사이가 2보다 작은데 파티션도 없는 경우 라고 볼 수 있다
    ## 즉 바로 옆에 붙어 있는 경우나, 대각선인데 (x,y) 인데 (x,0) , (0,y) 에 X가 없는 경우를 말한다
    
    dx1 = [-1, 1, 0, 0]
    dy1 = [0, 0, 1, -1]
    dx2 = [-1, -1, 1, 1]
    dy2 = [-1, 1, -1, 1]
    def check(i,j,n,m):
        ## 먼저 거리가 1인 경우를 봐보자. 
        for x,y in zip(dx1, dy1):
            if 0 <= i+x < n and 0 <= j+y < m and place[i+x][j+y] == 'P':
                return False

        ## 먼저 거리가 2인 경우를 봐보자
        for x,y in zip(dx1, dy1):
            if 0 <= i+x*2 < n and 0 <= j+y*2 < m and place[i+x*2][j+y*2] == 'P' and place[i+x][j+y] == 'O':
                return False       

        ## 대각선이 2인 경우를 봐보자
        for x,y in zip(dx2, dy2):
            if 0 <= i+x < n and 0 <= j+y < m and place[i+x][j+y] == 'P' and (place[i+x][j] == 'O' or place[i][j+y] == 'O'):
                return False
        return True
    
    for place in places:
        n = len(place)
        m = len(place[0])
        for i in range(n):
            no = False
            for j in range(m):
                if place[i][j] == 'P':
                    if not check(i,j,n,m):
                        no = True
                        break
            if no:
                answer.append(0)
                break
        if not no:
            answer.append(1)
    
    return answer