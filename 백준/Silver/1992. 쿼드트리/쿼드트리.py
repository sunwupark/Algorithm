## 왼쪽 위, 오른쪽 위, 왼쪽 아래, 오른쪽 아래

N = int(input())
video = []
for _ in range(N):
    video.append(input())

# print(video)

def quad(startx, starty, length):
    ## 모두 0인지 1인지 판단한다
    previous = video[startx][starty]
    notQuad = False
    for x in range(startx, startx+length):
        for y in range(starty, starty+length):
            if video[x][y] != previous:
                notQuad = True
                break
            previous=video[x][y]
        
        if notQuad:
            break
    
    if notQuad:
        ## 왼쪽 위
        leftup = quad(startx, starty, length//2)
        ## 오른쪽 위
        rightup = quad(startx, starty+length//2, length//2)
        ## 왼쪽 아래
        leftdown = quad(startx+length//2, starty, length//2)
        ## 오른쪽 아래
        rightdown = quad(startx+length//2, starty+length//2, length//2)
        return f"({leftup}{rightup}{leftdown}{rightdown})"

    if not notQuad:
        return previous

print(quad(0,0,N))