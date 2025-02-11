N = int(input())
paper = []
for _ in range(N):
    paper.append(list(map(int, input().split())))

blue = 0
white = 0

def dc(length, startx, starty):
    global blue, white

    tempSum = 0
    for val in range(startx, startx+length):
        tempSum += sum(paper[val][starty:starty+length])
    
    # print(length, startx, starty, tempSum)
    
    if tempSum == length**2:
        blue += 1
        return
    
    if tempSum == 0:
        white += 1
        return

    ## 4등분으로 쪼개야한다 0~7/ 0~7이라고 할때
    ## 왼쪽 위
    dc(length//2, startx, starty)

    ## 왼쪽 아래
    dc(length//2, startx+length//2, starty)

    ## 오른쪽 아래
    dc(length//2, startx+length//2, starty+length//2)

    ## 오른쪽 위
    dc(length//2, startx, starty+length//2)

dc(N, 0,0)

print(white)
print(blue)