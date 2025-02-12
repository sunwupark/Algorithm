N = int(input())

## 27이라는 숫자가 들어오면 9의 크기의 정사각형을 8개 배치를 해야한다
## 9라는 숫자가 들어오면 3이라는 크기의 정사각형을 만들어야한다
## 변이 3의 사각형을 만든다고 해보자
## x,y의 리스트로 나타낸다고해볼때

dx = [0,0,0,1,1,1,2,2,2]
dy = [0,1,2,0,1,2,0,1,2]

startList = [[" " for _ in range(N)] for _ in range(N)]

def printStar():
    for i in range(len(startList)):
        print("".join(startList[i]))

def dc(N, startx, starty):
    # print(N, startx, starty)
    if N == 3:
        for x,y in zip(dx, dy):
            if x == 1 and y == 1:
                continue
            startList[startx+x][starty+y] = "*"
    else:
        dc(N//3, startx, starty)
        dc(N//3, startx, starty+N//3)
        dc(N//3, startx, starty+N//3*2)
        dc(N//3, startx+N//3, starty)
        # dc(N//3, startx+N//3, starty+N//3)
        dc(N//3, startx+N//3, starty+N//3*2)
        dc(N//3, startx+N//3*2, starty)
        dc(N//3, startx+N//3*2, starty+N//3)
        dc(N//3, startx+N//3*2, starty+N//3*2)

dc(N, 0,0)
printStar()
